import subprocess

WACLI = "/Users/shubhamyadav/go/bin/wacli"

def send_message(number, text):
    subprocess.run([
        WACLI,
        "send", "text",
        "--to", number,
        "--message", text
    ])
