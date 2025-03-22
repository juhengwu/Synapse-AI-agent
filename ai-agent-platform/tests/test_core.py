import pytest
from src.app import AIAgentCore

@pytest.mark.asyncio
async def test_basic_flow():
    core = AIAgentCore()
    response = await core.process_request("需要开发一个TODO List应用")
    assert "用户故事" in response["pm_output"]
    assert "技术栈" in response["dev_output"]