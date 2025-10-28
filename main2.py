from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI




load_dotenv()

class Movie(BaseModel):
    title:str
    director:str 
    actor:str
    year:int 
    rating:float

model = ChatOpenAI(model="gpt-4", temperature=0)

model_with_structure = model.with_structured_output(Movie) 
response = model_with_structure.invoke("Provide details about the movie Dude")
print(response)

# agents = create_agent(model=model)



