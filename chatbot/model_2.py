"""
Model No:2
This is an advance chatbot for an ecommerce website that sells shoes. It has tool calling ability and chat history
"""

from openai import OpenAI
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
KEY = os.getenv("GOOGLE_API_KEY")

client = OpenAI(api_key=KEY,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

chat_history = []
chat_history.append({"role": "system", "content": "You are Tulio, a supportive yet straightforward AI assistant for customers of a e commerce website called ALL Time SHoes. Your main goal is to support customer queries and show them product according to their. You do not answer questions outside these topics."})


# functions
def getData(category="", brand="", minPrice="", maxPrice="", page=""):
  base_url = "http://localhost:5000/shoes"
  params = []
  if(category): params.append(f"category={category}")
  elif(brand): params.append(f"brand={brand}")
  elif(minPrice): params.append(f"minPrice={minPrice}")
  elif(maxPrice): params.append(f"maxPrice={maxPrice}")
  elif(page): params.append(f"page={page}")
  url = base_url + "?" + "&".join(params)
  response = requests.get(url=url)
  return response.json()

tools = [
  {
    "type": "function",
    "function": {
      "name": "getData",
      "description": "Get the shoes data",
      "parameters": {
        "type": "object",
        "properties": {
          "category": {
            "type": "string",
            "description": "category of the shoe. All lower case and saperate by _",
            "enum":["sneakers","trail_shoes","running_shoes","one_one_walking_shoes","walking_shoes","hiking_boots","training_shoes","casual_shoes","basketball_shoes"],
            "default":"",
          },
          "brand": {
            "type": "string",
            "description": "Shoe brand. Like: Nike, Addidas, Puma, Asian etc.",
            "enum":["Saucony","Puma","Brooks","Hoka","Birkenstock","Mizuno","Timberland","Under","Jordan","Converse","Clarks","Reebok","Fila","Adidas","ECCO","Merrell","Columbia","Nike","Asian"],
             "default":"",
          },
          "minPrice": {
            "type": "string",
            "description": "minimum price of the shoe",
             "default":"",
          },
          "page": {
            "type": "string",
            "description": "page number of the web api page. Each page has 7 products.",
             "default":"",
          },
        },
      },
    }
  }
]
while True:
  if(len(chat_history) >=10):
      chat_history.remove(chat_history[1])

  user_input = input("You: ")

  if(user_input == "bye" ):
    chat_history.clear()
    break

  message = {"role":"user", "content":user_input}
  chat_history.append(message)

  response = client.chat.completions.create(
    model="gemini-2.0-flash-lite-001",
    messages=chat_history,
    max_tokens=500,
    tools=tools,
    tool_choice="auto"
  )
  message = response.choices[0].message

  if message.tool_calls:
      for tool_call in message.tool_calls:
          name = tool_call.function.name
          args = json.loads(tool_call.function.arguments)
          
          if(name=="getData"):
             result = getData(**args)
          else:
              result = "Unknown tool"
          session =[]
          # add tool call in chats
          session.append({
             "role":"assistant",
             "tool_calls":[
                {
                   "id":tool_call.id,
                   "type":"function",
                   "function":{
                      "name":name,
                      "arguments": tool_call.function.arguments
                   }
                }
             ]
          })
          # Add the tool's output
          session.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })
          
          chat_history.append(session)
          # Ask the model again for the final response
          final_response = client.chat.completions.create(
                model="gemini-2.0-flash",
                messages=chat_history
            )
          print("Assistant: ",final_response.choices[0].message.content)
          chat_history.pop()
          session.append({
             "role":"assistant",
             "content":final_response.choices[0].message.content
          })
          chat_history.append(session)
  else:
        print("Assistant:", message.content)
  
