from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model= 'gemini-2.5-pro')

parser =  JsonOutputParser()

template2 = PromptTemplate(
    template= "Give the name and legacy of {text}",
    input_variables= [],
    partial_variables= {'text' : parser.get_format_instructions()}
)

prompt = template2.format()
# cahin will just make this as a pipeline
chain = template2 | model | parser

result =chain.invoke({'text':"max mullen"})

print(result.content)