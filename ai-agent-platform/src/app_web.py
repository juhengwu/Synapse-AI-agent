import streamlit as st
import asyncio
import subprocess
import time
from ai_agent_core import AIAgentCore
from dotenv import load_dotenv
import re

def _extract_code_block(text):
    matches = re.findall(r"```python\s*(.*?)```", text, re.DOTALL)
    return matches[0].strip() if matches else text.strip()


load_dotenv()
agent = AIAgentCore()

st.set_page_config(page_title="AI UI Generator", layout="centered")

st.title("🧠 Synapse: AI Dev — Instantly Generate a Streamlit App")
user_input = st.text_area("💡 Describe your app idea (e.g., a workout planner)")

loading_messages = [
    "🤔 AI PM is thinking about what the client really wants...",
    "🧠 AI PM is pitching the idea to the dev team...",
    "👨‍🍳 AI Dev is cooking up some code...",
    "🛠️ AI Dev is building the Streamlit UI...",
    "📦 AI Dev is packaging the app for delivery..."
]

async def show_dynamic_loading(placeholder, stop_event):
    """Show rotating loading messages until stop_event is set."""
    i = 0
    while not stop_event.is_set():
        placeholder.info(loading_messages[i % len(loading_messages)])
        await asyncio.sleep(3)
        i += 1

if st.button("🚀 Generate App Code") and user_input.strip():
    placeholder = st.empty()
    stop_event = asyncio.Event()

    async def run_pipeline():
        # Start dynamic loading message loop
        loading_task = asyncio.create_task(show_dynamic_loading(placeholder, stop_event))

        try:
            result = await agent.process_request(user_input)
            code = _extract_code_block(result["dev_output"])

            with st.expander("📌 Product Manager Output", expanded=True):
                st.markdown(f"```\n{result['pm_output']}\n```")

            with st.expander("💻 Developer Output", expanded=True):
                st.markdown(f"```\n{result['dev_output']}\n```")

            # Save generated code
            file_path = "generated_code.py"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code)

            st.success("✅ Code generated! Click the button below to launch your app.")
            st.code(code, language="python")

            subprocess.Popen(["streamlit", "run", file_path])
            st.info("🌐 App is now running. Visit it in your browser: http://localhost:8501")

        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")
        finally:
            stop_event.set()
            await loading_task

    asyncio.run(run_pipeline())


