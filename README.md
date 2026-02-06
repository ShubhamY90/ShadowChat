# ShadowChat 🤖💬

A personal WhatsApp auto-reply bot powered by **Ollama (Qwen2.5)**.  
Reads live messages, adds short-term memory, applies filters, and replies like a human.

⚠️ Personal-use research project. Not affiliated with WhatsApp.

---

## ✨ Features

- Live WhatsApp message listener
- AI replies using **Qwen2.5 (local LLM via Ollama)**
- Per-chat rolling context memory
- Contact & group filtering
- Spam / link ignore rules
- Round-robin sync architecture
- SQLite DB tail watcher
- Fully offline AI (no cloud APIs)
- Persona customization via `skills.md`

---

## 🧠 Architecture

```
WhatsApp → wacli → SQLite DB → Python listener → Ollama (Qwen2.5) → reply
```

The bot:

1. Pulls short sync bursts
2. Reads only new DB rows
3. Builds chat context
4. Injects persona rules
5. Generates reply with local LLM
6. Sends message back

No history replay. Only live messages.

---

## 🛠 Requirements

- macOS / Linux
- Python 3.10+
- Ollama installed
- wacli installed
- Git

---

## 🚀 Setup

### 1. Clone repo

```
git clone https://github.com/YOUR_USERNAME/whatsapp-ai-agent
cd whatsapp-ai-agent
```

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Install AI model

```
ollama run qwen2.5
```

(Model downloads once)

---

### 4. Connect WhatsApp

```
wacli sync
```

Scan QR. Let it sync briefly, then stop.

---

### 5. Run bot

```
python main.py
```

Done ✅

---

## ⚙️ Configuration

Edit:

```
core/decision.py
```

to control:

- allowed contacts
- group behavior
- spam filters
- mention rules

Edit:

```
config/settings.py
```

to change:

- AI model
- personality prompt
- reply delays

---

## 🧩 Model Improvements (Persona System)

You can improve the bot’s personality without touching Python code.

Create a file:

```
skills.md
```

This file acts as a behavior/persona layer injected into the AI prompt.

You can define:

- tone of speaking
- humor level
- reply length
- emotional behavior
- politeness rules
- sarcasm level
- group chat etiquette

Examples:

- friendly sibling assistant
- sarcastic coder friend
- calm therapist tone
- professional work assistant
- meme-heavy Gen Z style

Future versions may support per-contact personas and dynamic switching.

---

## 🔒 Privacy

- No cloud APIs
- No external servers
- All messages stay local
- SQLite DB stored on your machine
- Ollama runs fully offline

---

## ⚠️ Disclaimer

Uses unofficial WhatsApp interfaces.

Use responsibly.  
Not intended for spam or abuse.

Personal experimentation only.

---

## 🔮 Future Ideas

- Persistent long-term memory
- Persona switching per contact
- Emotion tracking
- Message batching
- Typing delay realism
- Voice message support
- Web dashboard
- Docker deployment

---

## 📜 License

MIT License

This means:

- anyone can use the code
- modify it
- redistribute it
- use it commercially

The only requirement is keeping the copyright notice.

Copyright (c) 2026 Shubham Yadav

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files to deal in the Software
without restriction…

Full license text: https://opensource.org/licenses/MIT

---

## ❤️ Credits

Built with:

- Ollama
- Qwen2.5
- wacli
- SQLite
- Python

---

Made for learning, experimentation, and fun 🚀
