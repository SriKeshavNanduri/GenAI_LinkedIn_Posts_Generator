# import the required modules. 
import os
from dotenv import load_dotenv
load_dotenv()
import warnings 
warnings.filterwarnings("ignore")
from langchain_openai import ChatOpenAI

# setting up the environmental variables. 

# create the openapi_key and assign that value in the .env file. 
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
## Create the langchain api keys from langsmith and assign those values in the .env file. 
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")


# creating the llm variable. 
llm=ChatOpenAI(model="gpt-4o")
# result=llm.invoke("What are ingredients of samosa?")
# print(result.content)

