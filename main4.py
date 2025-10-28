from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool


load_dotenv()

@tool
def get_weather(location: str) -> str:
    """Get weather at a location"""
    return f"Its sunny in {location}"

model = ChatOpenAI(model="gpt-4")


model_with_tools = model.bind_tools([get_weather])

response = model_with_tools.invoke("Whats the weather in India?")

for tool_call in response.tool_calls:
    print(f"Tool: {tool_call['name']}")
    print(f"Args: {tool_call['args']}")


