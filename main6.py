from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
import os
import requests


load_dotenv()

@tool
def web_search(query: str) -> str:
    """ Search the web using Tavily for upto date information"""
    tavily_tool = TavilySearch(max_result = 3)
    results = tavily_tool.invoke({"query": query})
    formatted = str(results)
    return f"Top search results for' {query}':\n\n{formatted} "

@tool
def weather_report(city:str) -> str:
    """ Fetct weather report of the current city using OpenWeatherMap API """
    api_key= os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "Api key not found"
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    data = response.json()
    print(data)
    desc = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]

    return f"Weather in {city} : {desc}, {temp}C, (feels like {feels_like}°C), humidity {humidity}%."


model = ChatOpenAI(model="gpt-4", temperature=0.3)

agent = create_agent(
    model=model, 
    tools=[web_search, weather_report],
    system_prompt="You are an intelligent search assistant who gives me accurate information"
    )

query = "whats the weather in France?"
response = agent.invoke({
    "messages": [{"role": "user", "content": query}]
})
final_response = response["messages"][-1].content

print(final_response)

