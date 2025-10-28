from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage, SystemMessage

load_dotenv()

system_message = SystemMessage("""You are an expert in stock marketing.Give me advice for stock market how to invest and list out the best stocks.""")

messages = [
    system_message,
    HumanMessage("how can i start on investing stocks")
]

model = ChatOpenAI(model="gpt-4")

response = model.invoke(messages)
print(response.content)