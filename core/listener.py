import subprocess
import sqlite3
import time
import os
from collections import defaultdict

DB = os.path.expanduser("~/.wacli/wacli.db")

def get_latest_rowid():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT MAX(rowid) FROM messages")
    row = cur.fetchone()
    conn.close()
    return row[0] or 0

def sync_once():
    proc = subprocess.Popen(["wacli", "sync"])
    time.sleep(3)   # let it pull messages
    proc.terminate()
    proc.wait()
    time.sleep(0.5)  # Give DB time to release lock after process ends

def listen(callback):
    last_id = get_latest_rowid()  # start from NOW
    print("Starting from row:", last_id)
    
    # Store context per chat
    chat_contexts = defaultdict(list)

    while True:
        sync_once()

        try:
            conn = sqlite3.connect(DB, timeout=10)  # Increased timeout
            cur = conn.cursor()

            cur.execute("""
                SELECT rowid, chat_jid, text
                FROM messages
                WHERE text IS NOT NULL
                AND from_me = 0
                AND rowid > ?
                ORDER BY rowid ASC
            """, (last_id,))

            rows = cur.fetchall()
            
            # Fetch history for each chat BEFORE closing connection
            messages_with_context = []
            for rowid, jid, text in rows:
                # Get history using the same connection
                cur.execute("""
                    SELECT text, from_me, ts
                    FROM messages
                    WHERE chat_jid = ?
                    AND text IS NOT NULL
                    ORDER BY rowid DESC
                    LIMIT ?
                """, (jid, 10))
                
                history_rows = cur.fetchall()
                history = []
                for h_text, from_me, ts in reversed(history_rows):
                    role = "assistant" if from_me else "user"
                    history.append({"role": role, "text": h_text, "ts": ts})
                
                messages_with_context.append((rowid, jid, text, history))
            
            conn.close()  # Close connection after ALL DB operations

            # Process messages after DB is closed
            for rowid, jid, text, history in messages_with_context:
                print("NEW MSG:", text)
                
                # Pass message with its chat-specific context
                callback({
                    "from": jid,
                    "text": text,
                    "context": history  # Chat-specific history
                })
                
                last_id = rowid

        except sqlite3.OperationalError as e:
            print(f"DB busy... retry ({e})")
            time.sleep(0.5)  # Wait before retry

        time.sleep(2)  # Increased sleep between sync cycles