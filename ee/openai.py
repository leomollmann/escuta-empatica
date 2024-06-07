import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_embedding(text):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model="text-embedding-3-small").data[0].embedding

def prompt(prompt, initial=None):
    # Set the parameters for the completion
    messages = [{
        "role": "user",
        "content": prompt,
    }]
    if initial:
        messages.insert(0, {
            "role": "system",
            "content": initial,
        })
    try:
        completion = client.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",
        )

        return completion.choices[0].message.content
    except Exception as e:
        # Handle error if the API request fails
        print(f"Error: {e}")
        return None