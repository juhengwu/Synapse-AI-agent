@echo off

:: 激活虚拟环境
call .venv\Scripts\activate.bat

:: 切换到 src 目录
cd src

:: 运行 streamlit
streamlit run app_web.py


