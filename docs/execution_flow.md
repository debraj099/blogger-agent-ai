# 🔁 Execution Flow — AI Blog Prompt Agent

This document explains how user input flows through the system using the 9-layer DT AI Agent architecture.

---

## 🧭 Step-by-Step Execution Flow

### 🟦 1. Input Layer – User Input Collection
- The user enters data in the chat UI:
  - Blog niche (e.g., "tech", "travel")
  - Tone preference (e.g., "witty")
  - Prompt length (e.g., "headline")
- This input is sent via Flask routes to the backend.

---

### 🟨 2. Context & Memory Layer – Personalized Recall
- The backend checks `users.json` for:
  - Past tone and length preferences (IP-based session memory)
- It checks `prompts.json` for:
  - Previously generated prompts to avoid repetition
- These are loaded to personalize the current request.

---

### 🟩 3. Lens Selector Engine – Frame the Right View
- System maps user input to lenses:
  - **Tone lens**: casual, witty, or formal
  - **Niche lens**: user-defined niche like "finance" or "fashion"
- No emotional lens (yet), but logic allows for future integration.

---

### 🔴 4. Agent Stack – Intelligent Prompt Generation
- The **Prompt Generator Agent** uses the OpenRouter API (DeepSeek-Chat) to generate creative blog prompts.
- No Reframer or QA Agent yet (planned for future).

---

### 🟧 5. Prompt Compiler – Final Prompt Formatting
- Compiles structured prompt:
Give me a [length] for a blog about [niche] in a [tone] tone. Date: [today]"


- Example:
"Give me a headline for a blog about tech in a witty tone. Date: 2025-07-05"



---

### 🟪 6. QA + Explainability Layer – Safe Output
- Prompt quality is controlled by:
- Token limits (max_tokens=200)
- Clear formatting and minimal vagueness
- Option to regenerate prompts
- No full explainability UI yet (planned).

---

### 🧩 7. Agent Dispatcher – Entry Point Logic
- Since the prompt is triggered from a user click/input in the chat UI, the **execution mode is set to real-time**.
- The Flask route serves as the dispatcher.

---

### ⚙️ 8. Agent Orchestrator – Agent Flow Execution
- Orchestrator logic is handled inside `app.py`:
- Compiles prompt
- Sends to OpenRouter
- Collects and stores output
- Simple linear agent path (compiler → agent → writer)

---

### 📦 9. Output Writer – Save and Display
- Final prompt is:
- Shown in chat UI
- Appended to `prompts.json`
- Displayed in a history panel for user reference

---

## 🧪 Future Upgrades (Optional Flow Enhancements)
- Add QA Validator Agent (to check prompt variety & relevance)
- Add Emotion lens using sentiment detection from input
- Add feedback loop (like/dislike prompts → tune generations)
- Implement persistent user login beyond IP memory

---

## ✅ Summary

| Layer | Role in Your Project |
|-------|----------------------|
| Input Layer | Takes tone, niche, length from user |
| Context Layer | Loads `users.json`, `prompts.json` |
| Lens Selector | Applies tone + niche |
| Agent Stack | Uses OpenRouter to generate prompt |
| Prompt Compiler | Formats prompt string |
| QA Layer | Controls quality via format + token limits |
| Dispatcher | Flask route triggered in real-time |
| Orchestrator | Executes prompt flow in `app.py` |
| Output Writer | Displays in UI + saves to JSON |