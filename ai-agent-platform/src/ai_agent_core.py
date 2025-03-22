import os
from dotenv import load_dotenv
import subprocess
import re
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# 初始化环境
load_dotenv()
llm = ChatOpenAI(model="gpt-4-1106-preview")

# 角色系统实现
class AIAgentCore:
    def __init__(self):
        self.pm_prompt = ChatPromptTemplate.from_template("""
            You are a professional product manager (AI-PM). Given the following request: {user_input}
            Please do the following:
            1. List 3 key clarification questions.
            2. Write a user story.
            3. Output a JIRA-style task description.
        """)

        self.dev_prompt = ChatPromptTemplate.from_template("""
            You are a full-stack engineer (AI-Dev). Your job is to generate **runnable Python code** only.
            ---
            {task}
            ---

            Please:
            1. Use Python only. Do not use JavaScript or Node.js.
            2. Use **Streamlit** to create a visual UI (single-file app).
            3. Output a complete Python file with Streamlit components.
            4. Make sure it's self-contained and can be run as: `streamlit run app.py`
            5. Do not split code into multiple files.
        """)

        self.repair_prompt = ChatPromptTemplate.from_template("""
            The following code caused an error when executed:
            ---
            {code}
            ---
            Error message:
            ---
            {error_msg}
            ---
            Please fix the code and output the entire corrected version.
        """)
        
        
    def _parse_pm_output(self, pm_output):
        # 直接取整段文本作为任务内容
        return pm_output.content.strip()
    
    async def _enqueue_task(self, task):
        # 模拟入队，可打印日志
        print(f"[Queue] Task enqueued: {task[:60]}...")
        
    def _save_code_to_file(self, code: str, filename="generated_code.py"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)
        return filename
    
    def _run_code_and_capture(self, filename):
        try:
            result = subprocess.run(["python", filename], capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                return {"success": True, "output": result.stdout}
            else:
                return {"success": False, "error": result.stderr}
        except Exception as e:
            return {"success": False, "error": str(e)}
        
    def _extract_code_block(self, text):
        matches = re.findall(r"```python\s*(.*?)```", text, re.DOTALL)
        return matches[0].strip() if matches else text.strip()
    
    async def process_request(self, user_input: str):
        # PM 阶段
        pm_chain = self.pm_prompt | llm
        pm_output = await pm_chain.ainvoke({"user_input": user_input})

        task = self._parse_pm_output(pm_output)
        await self._enqueue_task(task)

        # Dev 阶段 - 初始生成
        dev_chain = self.dev_prompt | llm
        dev_output = await dev_chain.ainvoke({"task": task})
        code = self._extract_code_block(dev_output.content)

        filename = self._save_code_to_file(code)
        result = self._run_code_and_capture(filename)

        # 如果失败，尝试修复一次
        if not result["success"]:
            print("[Error] Code failed, sending back to GPT for repair...")
            repair_chain = self.repair_prompt | llm
            repair_output = await repair_chain.ainvoke({"code": code, "error_msg": result["error"]})
            fixed_code = self._extract_code_block(repair_output.content)

            filename = self._save_code_to_file(fixed_code)
            result = self._run_code_and_capture(filename)

            dev_output = repair_output

        return {
            "pm_output": pm_output.content,
            "dev_output": dev_output.content,
            "run_result": result.get("output") if result["success"] else f"Failed to run: {result['error']}"
        }
        
