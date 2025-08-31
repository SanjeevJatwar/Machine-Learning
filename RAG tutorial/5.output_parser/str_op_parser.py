from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model= 'gemini-2.5-pro')

template1 = PromptTemplate(
    template= " Wite 1 line summary of given{Topic}",
    input_variables= ['Topic']
)

template2 = PromptTemplate(
    template= "write detailed report ofr these with title on {Topic}.",
    input_variables= ['Topic']
)

parser =  StrOutputParser()

# cahin will just make this as a pipeline
chain = template1 | model | parser | template2 | model | parser

result =chain.invoke({'Topic' : "Virat Kohli"})

print(result)