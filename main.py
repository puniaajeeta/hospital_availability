import openai
import langchain
#export OPENAI_API_KEY="Medicine"
import os
from langchain.llms import OpenAI


# llm = OpenAI(temperature=0.3)
# print(llm.predict("what is the capital of delhi"))
import os 
import openai

openai.api_key = os.getenv("openai_api_key")



from langchain.llms import OpenAI

llm = OpenAI(openai_api_key="openai_api_key")

from langchain.llms import OpenAI

llm = OpenAI()

print(type(llm.predict("Medical store phone numbers  in Hisar ")))
