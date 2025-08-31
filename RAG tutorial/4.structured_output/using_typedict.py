from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()



class inform(TypedDict):
    gender : str
    age: int
    type_of_surgery : str
    location : str
    policy_info : str

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-pro')
struct_op = model.with_structured_output(inform)


result = struct_op.invoke("""46-year-old male, knee surgery in Pune, 3-month-old insurance policy""")

print(result) 