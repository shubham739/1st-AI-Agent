import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What is the capital of France?"}]
)

print(response['choices'][0]['message']['content'])
# This code uses the OpenAI API to get a response from the GPT-3.5-turbo model.