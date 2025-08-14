"""
Model No:2
This is an advance chatbot for an ecommerce website that sells shoes. It has tool calling ability and chat history
"""

from openai import OpenAI
import os
from dotenv import load_dotenv
import requests

load_dotenv()
KEY = os.getenv("GOOGLE_API_KEY")

client = OpenAI(api_key=KEY,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

chat_history = []
chat_history.append({"role": "system", "content": "You are Tulio, a supportive yet straightforward AI assistant for customers of a e commerce website called ALL Time SHoes. Your main goal is to support customer queries and show them product according to their. You do not answer questions outside these topics."})


# functions
def getData(category,brand,minPrice,maxPrice,page):
  base_url = "http://localhost:5000/shoes"
  params = []
  if(category): params.append(f"category={category}")
  elif(brand): params.append(f"brand={brand}")
  elif(minPrice): params.append(f"minPrice={minPrice}")
  elif(maxPrice): params.append(f"maxPrice={maxPrice}")
  elif(page): params.append(f"page={page}")
  url = base_url + "?" + f"{"&".join(params)}"
  response = requests.get(url=url)
  return response.content


while True:
  user_input = input("You: ")

  if(user_input == "bye" ):
    chat_history.clear()
    break

  message = {"role":"user", "content":user_input}
  chat_history.append(message)

  response = client.chat.completions.create(
    model="gemini-2.0-flash-lite-001",
    messages=chat_history,
    max_tokens=500
  )
  chat_history.append({"role":"assistant", "content":response.choices[0].message.content})
  print(response.choices[0].message.content)
  if(len(chat_history) >=10):
    chat_history.remove(chat_history[1])
