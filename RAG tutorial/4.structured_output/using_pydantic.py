from pydantic import BaseModel, EmailStr,Field
from typing import Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-pro")

class inform(BaseModel):
    gender : Literal["Male", "Female"] = Field(description= "Return gender fromt the text whom the text refers to.")
    age: int
    type_of_surgery : str
    location : str
    policy_info : str
    email : EmailStr

struc_output = model.with_structured_output(inform)

result = struc_output.invoke("""46-year-old male, knee surgery in Pune, 3-month-old insurance policy ans the emailis sanjeec@iiitnr.edu.in""")

#print(result)

data = result.model_dump()  # or .dict() 
print(data['age'])

