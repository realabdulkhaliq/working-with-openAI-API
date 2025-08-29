from openai import OpenAI

client = OpenAI(api_key="OPENAI_API_KEY")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
)

print(response.choices[0].message.content)