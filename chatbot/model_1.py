"""
Model No:1 
this basic chatbot as a nutrionist with in-build chat memory. We use openAI compatability here as it's recomended for chatsession ()
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("GOOGLE_API_KEY")

client = OpenAI(api_key=KEY,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

chat_history = []
chat_history.append({"role": "system", "content": "You are a helpful nutrionist named Dr Mandella. You help your clients to complete their protein goal and stay fit."})


while True:
  user_input = input("You: ")

  if(user_input == "bye" ):
    chat_history.clear()
    break

  message = {"role":"user", "content":user_input}
  chat_history.append(message)

  response = client.chat.completions.create(
    model="gemini-2.0-flash-lite-001",
    messages=chat_history
  )
  chat_history.append({"role":"assistant", "content":response.choices[0].message.content})
  print(response.choices[0].message.content)
