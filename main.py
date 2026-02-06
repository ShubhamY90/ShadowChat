from core.listener import listen
from core.brain import generate_reply
from core.sender import send_message
from core.decision import should_reply

def handle_message(msg):
    if not should_reply(msg):
        return

    text = msg["text"]
    sender = msg["from"]
    context = msg.get("context", [])  # Get chat-specific context

    print("Incoming:", text)

    reply = generate_reply(text, context)  # Pass context to brain

    print("Reply:", reply)

    send_message(sender, reply)

listen(handle_message)

# from core.listener import listen
# from core.decision import should_reply

# def handle_message(msg):
#     allowed = should_reply(msg)

#     print("SENDER:", msg["from"])
#     print("TEXT:", msg["text"])
#     print("ALLOWED:", allowed)
#     print("-----")

# listen(handle_message)