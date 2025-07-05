from flask import Flask, render_template, request, jsonify
import requests
import json
from datetime import datetime

app = Flask(__name__)

OPENROUTER_API_KEY = "Bearer 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"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
USER_FILE = "users.json"
PROMPT_HISTORY_FILE = "prompts.json"


def load_users():
    try:
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_users(data):
    with open(USER_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def save_prompt_history(user_id, prompt):
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        with open(PROMPT_HISTORY_FILE, 'r') as f:
            data = json.load(f)
    except:
        data = {}

    if user_id not in data:
        data[user_id] = []

    data[user_id].append({
        "date": today,
        "prompt": prompt
    })

    with open(PROMPT_HISTORY_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/message', methods=['POST'])
def handle_message():
    user_id = request.remote_addr
    msg = request.json.get("message", "").strip().lower()

    default_user = {"step": "niche", "niches": [], "niche_index": 0, "tone": "", "length": ""}
    users = load_users()
    user = users.get(user_id, default_user)

    response = ""

    if user["step"] == "niche":
        user["niches"] = [x.strip() for x in msg.split(",") if x.strip()]
        user["niche_index"] = 0
        user["step"] = "tone"
        response = "Cool! What tone do you prefer? (e.g., casual, witty, formal)"

    elif user["step"] == "tone":
        valid_tones = ["casual", "witty", "formal"]
        if msg not in valid_tones:
            response = "❗ That doesn't seem like a valid tone. Please choose: casual, witty, or formal."
        else:
            user["tone"] = msg
            user["step"] = "length"
            response = "What type of prompt do you want? (one-liner, headline, detailed)"

    elif user["step"] == "length":
        valid_lengths = ["one-liner", "headline", "detailed"]
        if msg not in valid_lengths:
            response = "❗ That doesn't seem like a valid option. Please choose: one-liner, headline, or detailed."
        else:
            user["length"] = msg
            user["step"] = "done"
            niche = user["niches"][user["niche_index"]]
            prompt = generate_prompt(niche, user["tone"], user["length"])
            save_prompt_history(user_id, prompt)
            response = f"Awesome! Here’s your first writing prompt:\n📝 {prompt}\n\n(Reply with 'generate' for another or 'reset' to start over.)"

    elif user["step"] == "done":
        if msg in ["generate", "next", "another", "again", "prompt"]:
            niche = user["niches"][user["niche_index"]]
            prompt = generate_prompt(niche, user["tone"], user["length"])
            save_prompt_history(user_id, prompt)
            user["niche_index"] = (user["niche_index"] + 1) % len(user["niches"])
            response = f"📝 Here's another prompt for '{niche}':\n{prompt}"
        elif msg == "reset":
            user = default_user.copy()
            response = "Let's start fresh! What’s your blog niche?"
        else:
            response = "Type 'generate' for another prompt or 'reset' to start over."

    users[user_id] = user
    save_users(users)
    return jsonify({"reply": response})


def generate_prompt(niche, tone, length):
    today = datetime.now().strftime("%B %d, %Y")

    if length == "headline":
        style = "a catchy blog post title"
    elif length == "detailed":
        style = "a detailed and imaginative blog idea with some context"
    else:
        style = "a brief 1-2 line writing prompt"

    if tone == "casual":
        persona = "a friendly blogger who writes like they’re chatting with a friend"
        emoji = "💬"
    elif tone == "witty":
        persona = "a snappy, humorous writer who uses punchlines"
        emoji = "😄"
    else:
        persona = "a professional content strategist who writes with authority"
        emoji = "✍️"

    input_prompt = (
        f"You are {persona}. Suggest {style} for a blog on the topic '{niche}' "
        f"with the tone '{tone}'. Make it relevant to today’s date: {today}. "
        f"Do not include any explanations. Begin directly with the blog idea. Keep it creative. {emoji}"
    )

    headers = {
        "Authorization": OPENROUTER_API_KEY,
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5000",
        "X-Title": "AI Blog Prompt Bot"
    }

    payload = {
        "model": "deepseek/deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a creative and engaging blog assistant who helps bloggers write better."},
            {"role": "user", "content": input_prompt}
        ],
        "temperature": 0.9,
        "max_tokens": 250
    }

    try:
        res = requests.post(OPENROUTER_URL, headers=headers, json=payload)
        res.raise_for_status()
        output = res.json()
        text = output['choices'][0]['message']['content'].strip()
        print("[DeepSeek ✅] Prompt generated:", text)
        return text
    except Exception as e:
        print("[DeepSeek ❌ ERROR]:", e)
        return "Sorry, I couldn’t generate a prompt right now. Please try again later."


@app.route("/history")
def view_history():
    user_id = request.remote_addr
    try:
        with open(PROMPT_HISTORY_FILE, 'r') as f:
            data = json.load(f)
            history = data.get(user_id, [])
    except:
        history = []
    return render_template("history.html", history=history)


@app.route("/history/json")
def get_history_json():
    user_id = request.remote_addr
    try:
        with open(PROMPT_HISTORY_FILE, 'r') as f:
            data = json.load(f)
            return jsonify(data.get(user_id, []))
    except:
        return jsonify([])


if __name__ == '__main__':
    app.run(debug=True)
