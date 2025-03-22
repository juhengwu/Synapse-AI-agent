import streamlit as st
import asyncio
import subprocess
from ai_agent_core import AIAgentCore
from dotenv import load_dotenv
import re

def _extract_code_block(text):
    matches = re.findall(r"```python\s*(.*?)```", text, re.DOTALL)
    return matches[0].strip() if matches else text.strip()


load_dotenv()
agent = AIAgentCore()

st.set_page_config(page_title="AI UI Generator", layout="centered")

st.title("🧠 AI Dev: 一键生成 Streamlit 可视化 App")
user_input = st.text_area("💡 输入你的产品需求（如：健身计划 App）")

if st.button("🚀 生成 App 代码") and user_input.strip():
    with st.spinner("AI Dev 正在生成 Streamlit 可视化界面代码..."):
        try:
            result = asyncio.run(agent.process_request(user_input))
            code = _extract_code_block(result["dev_output"])
            
            with st.expander("📌 产品经理输出（PM Output）", expanded=True):
                st.markdown(f"```\n{result['pm_output']}\n```")

            with st.expander("💻 工程师输出（Dev Output）", expanded=True):
                st.markdown(f"```\n{result['dev_output']}\n```")
                
            # 保存代码为可执行文件
            file_path = "generated_code.py"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code)

            st.success("✅ 代码生成成功！你现在可以点击下方按钮运行它")

            st.code(code, language="python")


            subprocess.Popen(["streamlit", "run", file_path])
            st.info("🌐 App 正在运行中！请打开浏览器访问： http://localhost:8501")

        except Exception as e:
            st.error(f"❌ 出错了：{e}")
else:
    st.info("输入产品需求，然后点击按钮生成可视化 App")

