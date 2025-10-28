from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI


load_dotenv()

@tool
def search(query:str) -> str:
    """Search the web for information."""
    return f"Results for: {query}"

@tool
def get_weather(location:str) -> str:
    """Get the weather information for a given location."""
    return f"Weather in {location}: Sunny, 72°F"

model = ChatOpenAI(model="gpt-4", temperature=0)

agent = create_agent(model=model, tools=[search, get_weather])

response = agent.invoke({"messages": [{"role": "user", "content": "Whats the weather in india"}]})

final_response = response['messages'][-1].content

print(final_response)