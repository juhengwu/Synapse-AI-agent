# 🤖 Synapse AI Agent

Welcome to **Synapse AI Agent**, an all-in-one autonomous product builder powered by LLMs (like GPT-4). This AI is designed to **transform a simple idea into a real, runnable app** — without any manual coding.

---

## 🚀 What Does It Do?

Just give it a plain English idea, like:

> "I want an app that helps people build a daily fitness routine."

Synapse will:

1. 🧠 **Become your AI Product Manager (PM)**  
   - It thinks like a PM and asks smart clarifying questions.
   - It writes a user story.
   - It even formats a JIRA-style task for developers.

2. 👨‍💻 **Become your AI Developer (Dev)**  
   - It takes the PM's task and picks a tech stack.
   - It writes full runnable Python code using **Streamlit**.
   - It runs and checks the code.
   - If the code breaks? It **fixes it automatically**.

3. ✅ **Delivers a working application**  
   - Code is saved and ready to run.
   - A Streamlit app is created in one file.
   - You can launch it locally with a single click.

---

## 🛠 How To Use

### 1. Clone the repo & set up environment

```bash
git clone https://github.com/your-repo/synapse-ai-agent.git
cd synapse-ai-agent
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Add your OpenAI API key

Create a `.env` file:

```
OPENAI_API_KEY=your-api-key-here
```

### 3. Run the Streamlit interface

```bash
streamlit run app_web.py
```

Then just type your idea into the box, and watch magic happen 🎩✨

---

## 🔍 Example

You type:

> "I want a tool that lets students generate a study plan."

Synapse will:
- Think like a PM.
- Write up the task.
- Hand it off to the AI Dev.
- Generate a Python app using Streamlit.
- Run it.
- Let you launch the working app right from your browser.

---

## 🌟 Why This Is Cool

This is not just another chatbot.

Synapse AI Agent is a **multi-role agent system** that:
- Understands product design.
- Plans development.
- Codes intelligently.
- Tests & fixes bugs.
- And gives you real, usable output.

All from just **one instruction**.

---

## 🔮 What’s Next?

We're just getting started. Coming soon:

- 🌈 Beautiful custom UI for better user experience
- ☁️ One-click deployment to cloud (host your apps online!)
- 🧠 Deeper reasoning and smarter decision-making
- 📂 Multi-file architecture for building more complex projects

---

## ❤️ Credits

Built with love and curiosity by humans + AI.

---

Let Synapse be your PM. Your dev team. Your prototype machine.
Just give it an idea — it’ll handle the rest. ✨

