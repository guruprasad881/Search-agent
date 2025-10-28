# from dotenv import load_dotenv
# load_dotenv()


# # from langchain.agents import AgentExecutor
# from langchain_agents import create_react_agent
# from langchain_openai import ChatOpenAI
# from langchain_tavily import TavilySearch
# from langchain import hub

# tools = [TavilySearch()]

# llm = ChatOpenAI(model="gpt-4")
# react_prompt = hub.pull("hwchase17/react")



# # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# def main():
#     print("Hello from langchain!")


# if __name__ == "__main__":
#     main()
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

load_dotenv()


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}! and today its 30 degrees Celsius."


model = ChatOpenAI(
    model_name="gpt-4",  
    temperature=0,
    
)


agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a weather agent that always gives temperature in Celsius.",
)


response = agent.invoke(
    {"messages": [{"role": "user", "content": "whats the weather in india"}]}
)

final_response = response['messages'][-1].content

print(final_response)
