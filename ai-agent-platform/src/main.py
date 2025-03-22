import asyncio
from ai_agent_core import AIAgentCore  # Make sure the file is named ai_agent_core.py or adjust the import
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    agent = AIAgentCore()

    print("🤖 Welcome to AI Agent Core (PM + Dev)\nType 'exit' to quit.\n")
    while True:
        user_input = input("📥 Enter your product idea or feature request:\n> ")
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        # Call the async function in sync context
        try:
            result = asyncio.run(agent.process_request(user_input))
            print("\n📌 PM Output:\n" + result["pm_output"])
            print("\n💻 Dev Output:\n" + result["dev_output"])
            print("\n" + "-"*50 + "\n")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()