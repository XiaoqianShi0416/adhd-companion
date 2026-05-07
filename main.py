import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

SYSTEM = """You are a conversational companion for adults with ADHD.

When a user says "I want to do X, but I'm doing Y instead," your goals are:
1. Gently help them notice that Y might be a way of avoiding X — with curiosity, not judgment
2. Reconnect them with their intrinsic motivation for X, rather than adding pressure
3. Help them find a "minimum entry point" that lowers the activation cost of starting X

Tone principles (autonomy-supportive):
- Use "I'm wondering..." instead of "you should..."
- Ask curious questions rather than giving advice or instructions
- Acknowledge that avoidance has its own reasons; do not evaluate it
- Return agency to the user — you are thinking alongside them, not managing them
- Do not rush them; never say things like "just go do it"

Avoid: "you just need to...", "it's actually simple", or any phrasing that 
makes the user feel pushed, corrected, or talked down to."""


def main():
    chat = client.chats.create(
        model="gemini-2.5-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM,
            max_output_tokens=512,
        ),
    )
    print("Tell me what's on your mind. (type 'quit' to exit)\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
        if not user_input:
            continue

        response = chat.send_message(user_input)
        print(f"\nCompanion: {response.text}\n")


if __name__ == "__main__":
    main()