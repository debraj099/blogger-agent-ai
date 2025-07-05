# 🧪 Use Case Example — AI Blog Prompt Agent

This document presents a real-world example of how a blogger interacts with the system to receive a tailored writing prompt.

---

## 👩‍💻 User Profile
**Name:** Priya  
**Type:** Travel & Lifestyle Blogger  
**Blog Niche(s):** Travel, Mindfulness  
**Tone Preference:** Witty  
**Prompt Length:** Headline  

---

## 🟦 Step 1: User Opens the Chat Interface
Priya visits the AI prompt assistant in her browser.  
She is asked a series of quick questions:

- **Niche:** `Travel`
- **Tone:** `Witty`
- **Length:** `Headline`

---

## 🟧 Step 2: Prompt Compiler Builds the Request

The system formats a structured prompt:

"Give me a headline for a blog about travel in a witty tone. Date: 2025-07-05"


---

## 🔴 Step 3: AI Agent Generates a Prompt

The agent (using OpenRouter → DeepSeek-Chat) returns:

"Passport, Please: 5 Places So Cool They Should Be Illegal"


---

## 🟨 Step 4: Output is Shown in the Chat UI

The prompt is:

- Displayed instantly in the UI
- Stored in `prompts.json` under Priya’s session
- Available in the prompt history panel

---

## 🟩 Step 5: Multi-Niche Rotation

Priya selects a second niche: `Mindfulness` (still Witty tone, Headline style)

The system builds a new prompt:

"Give me a headline for a blog about mindfulness in a witty tone. Date: 2025-07-05"



The response:

"Zen and the Art of Not Throwing Your Phone at People"


---

## 🟪 Step 6: Memory Kicks In

The system automatically remembers:
- Priya prefers witty tone
- Headline-style prompts
- Niche rotation between Travel and Mindfulness

This enables a smoother experience on future visits (via `users.json`).

---

## 🔁 Optional User Actions

- Priya clicks “Regenerate Prompt” to get a new idea
- She adds the prompt to favorites (planned feature)
- Next session, system auto-selects previous tone/niche

---

## ✅ Result

Priya walks away with **creative, high-quality blog prompt ideas**, all tailored to her preferences, and she didn't even have to think of a topic herself.
