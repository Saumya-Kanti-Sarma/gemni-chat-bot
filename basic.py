'''
This is the basic use of gemni to crreate a simple chatbot 
'''
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=KEY)

response = client.models.generate_content(
  model="gemini-2.0-flash-lite-001",
  contents="make a simple hello world pogramme in python"
)
print(response.text)
#response:
'''
```python
print("Hello, world!")
```
This single line of code does the following:

1.  `print()` is a built-in Python function that displays output.
2.  `"Hello, world!"` is a string literal, which is the text you want to display.

When you run this code, it will print "Hello, world!" to your console.
'''