# 🧠 AI Agent for Daily Writing Prompts (Bloggers Edition)

Welcome to your intelligent writing buddy! This AI Agent helps bloggers generate creative, niche-specific, and tone-personalized blog prompts every day. Designed to fight writer’s block, it remembers your style and evolves with you.

---

## 🎯 Project Goal

The goal is to help bloggers beat writer’s block by generating **daily blog prompts** tailored to their **niche**, **tone**, and **desired length**. The agent acts like a writing partner—asking for light input and giving smart, relevant prompts instantly. It remembers past preferences (session-based) and supports switching between multiple blog niches.

---

## 🚀 Features

- ✍️ Daily blog prompt generation
- 🧠 Personalized suggestions based on:
  - Niche (tech, fashion, psychology, etc.)
  - Tone (casual, witty, formal)
  - Prompt length (headline, one-liner, detailed)
- 🗃 Prompt memory using `prompts.json`
- 🧑 Session memory using `users.json`
- 🔁 Multi-niche cycling support
- 💬 Simple chat interface (HTML + Flask)
- 🔐 API-based generation via OpenRouter

---

## 🧠 DT AI Agent Architecture Mapping

| DT Layer | Implemented In This Project |
|----------|-----------------------------|
| **1. Input Layer** | Chat UI captures tone, niche, and length preferences |
| **2. Context & Memory Layer** | `users.json` and `prompts.json` store user session and prompt history |
| **3. Lens Selector Engine** | Applies tone and niche as lenses for generation |
| **4. Agent Stack** | Uses OpenRouter API with DeepSeek-Chat model to generate prompts |
| **5. Prompt Compiler** | Formats: "Give me a [style] for a blog about [niche] in a [tone] tone. Date: [today]" |
| **6. QA + Explainability Layer** | Ensures prompt quality with token limits and regeneration options |
| **7. Agent Dispatcher** | Triggered via chat input (real-time request handling) |
| **8. Agent Orchestrator** | Sequential flow: compiler → OpenRouter agent → output |
| **9. Output Writer** | Prompt shown in UI and stored in JSON history |

---

## 🧾 Example Flow

1. **User Input:**
   - Niche: `Travel`
   - Tone: `Witty`
   - Length: `Headline`

2. **Prompt Compiler Output:**
"Give me a headline for a blog about travel in a witty tone. Date: 2025-07-05"
3. **AI Response:**
"Wanderlust Wonders: 7 Places You’ll Regret Not Visiting in Your 20s"
4. **Storage:**
- Saved to `prompts.json`
- User preferences remembered via `users.json`

---

## 📁 Project Structure

ai-prompt-agent-blogger/
│
├── app.py # Core Flask backend logic
├── prompts.json # Prompt history storage
├── users.json # User session memory
│
├── static/
│ └── style.css # Chat UI styles
│
├── templates/
│ ├── index.html # Main UI
│ └── history.html # Past prompts display
│
├── configs/
│ ├── lens-config.json # (Optional) Lens options
│ └── prompt_templates/ # (Optional) Prompt structure templates
│
├── docs/
│ ├── execution_flow.md # Flow across agent layers (optional)
│ └── use_case_example.md # Sample user session (optional)
│
└── README.md # Project overview (this file)

yaml
Copy
Edit

---

## 💻 How to Run (Locally)

> **Prerequisites:** Python 3.10+, Flask, and internet connection for OpenRouter API

```bash
git clone https://github.com/your-username/ai-prompt-agent-blogger.git
cd ai-prompt-agent-blogger
pip install -r requirements.txt
python app.py
Then open your browser at:
http://127.0.0.1:5000/

🌱 Planned Improvements
👍 👎 Prompt rating system (Like/Dislike)

🔐 User login (email-based persistence)

🧾 Generate full blog drafts

📈 Analytics dashboard (popular niches, tones, usage stats)

✨ Emotion-aware prompt suggestions

🧪 Sample Prompt Template
txt
Copy
Edit
Give me a [length] for a blog about [niche] in a [tone] tone. Date: [today]
📬 Author
Project by: Debraj Roy
Contact: debrajroy099@gmail.com
Powered by: OpenRouter + Flask

