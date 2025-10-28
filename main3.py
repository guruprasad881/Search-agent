from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy


load_dotenv()

class UserInfo(BaseModel):
    name: str
    contact:int
    address:str
    location: str

model = ChatOpenAI(model="gpt-4")


agent = create_agent(
    model=model,
    response_format=ToolStrategy(UserInfo)
)

result =  agent.invoke({"messages":[{"role":"user", "content" : "Extract userinfo from : Guru, 919380735764,JP Nagar Banglore, India"}]})

print(result)
