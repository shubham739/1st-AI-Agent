from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")
response = llm.invoke("What is the capital of France?")
print(response)