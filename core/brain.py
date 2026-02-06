import requests
from config.settings import OLLAMA_URL, MODEL, SYSTEM_PROMPT

def generate_reply(message, context=None):
    # Build conversation history
    conversation = ""
    if context:
        for msg in context[-10:]:  # Use last 10 messages for context
            role = "You" if msg["role"] == "assistant" else "User"
            conversation += f"{role}: {msg['text']}\n"
    
    # Add current message
    conversation += f"User: {message}\n"
    
    # Combine system prompt with conversation
    prompt = f"{SYSTEM_PROMPT}\n\nConversation:\n{conversation}\nYou:"

    try:
        r = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=30  # 30 second timeout
        )
        
        if r.status_code == 200:
            return r.json()["response"].strip()
        else:
            print(f"Ollama error: {r.status_code}")
            return "Sorry, I'm having trouble thinking right now 🤔"
            
    except requests.exceptions.Timeout:
        print("Model timed out after 30 seconds")
        return "Taking too long to think... maybe ask something simpler? 😅"
    except Exception as e:
        print(f"Error generating reply: {e}")
        return "Oops, something went wrong 😬"