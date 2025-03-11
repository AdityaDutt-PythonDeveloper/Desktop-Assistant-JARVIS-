from openai import OpenAI

client = OpenAI(
    api_key = "openai-api-key-and it is paid"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role" : "system", "content" : "You are a virtual Assistant named jarvis  skilled in general tasks like Alexa and Google"},
        {"role" : "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message.content)