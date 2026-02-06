def normalize(jid):
    return jid.split("@")[0]

ALLOWED_CONTACTS = {
    # <-- paste EXACT number or id here, without the @c.us or @g.us -->
}

ALLOWED_GROUPS = {
    # <-- paste EXACT number or id here, without the @c.us or @g.us -->
}

def should_reply(msg):
    jid = msg["from"]
    base = normalize(jid)

    print("CHECKING:", base)
    print("CONTACTS:", ALLOWED_CONTACTS)

    if jid.endswith("@g.us"):
        return False

    return base in ALLOWED_CONTACTS
