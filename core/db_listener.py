import sqlite3
import os

DB = os.path.expanduser("~/.wacli/wacli.db")
from core.memory import load_last_ts, save_last_ts
last_id = load_last_ts()

def db_loop_once(callback):
    global last_id

    conn = sqlite3.connect(DB)
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
    conn.close()

    for rowid, jid, text in rows:
        callback({"from": jid, "text": text})
        last_id = rowid
        save_last_ts(last_id)

