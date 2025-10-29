from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_tavily import TavilySearch


load_dotenv()

@tool
def web_search(query: str) -> str:
    """ Search the web using Tavily for upto date information"""
    tavily_tool = TavilySearch(max_result = 3)
    results = tavily_tool.invoke({"query": query})
    formatted = str(results)
    return f"Top search results for' {query}':\n\n{formatted} "

model = ChatOpenAI(model="gpt-4", temperature=0.3)

agent = create_agent(
    model=model, 
    tools=[web_search],
    system_prompt="You are an intelligent search assistant who gives me accurate information"
    )

query = "Who is the prime minister of india?"
response = agent.invoke({
    "messages": [{"role": "user", "content": query}]
})
final_response = response["messages"][-1].content

print(final_response)

