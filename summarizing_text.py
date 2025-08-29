from openai import OpenAI

client = OpenAI(api_key="OPENAI_API_KEY")

finance_text = """
The stock market has seen significant fluctuations in recent months, with major indices experiencing both gains and losses. Investors are closely monitoring economic indicators, such as inflation rates and employment figures, to gauge the market's direction. Additionally, geopolitical tensions and supply chain disruptions continue to impact investor sentiment.
"""

# Use an f-string to format the prompt
prompt = f"""Summarize the following text into two concise bullet points:
{finance_text}"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_tokens=100
)

print(response.choices[0].message.content)