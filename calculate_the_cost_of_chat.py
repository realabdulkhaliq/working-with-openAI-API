from openai import OpenAI

# Initialize client
client = OpenAI(api_key="OPENAI_API_KEY")

# Define prompt
prompt = """Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. 
It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. 
Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, 
such as commuting, travel, and transportation of goods. 
Cars are often associated with freedom, independence, and mobility."""

# Define max tokens
max_completion_tokens = 150

# Generate response
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=max_completion_tokens
)

# Pricing (adjust based on official rates)
input_token_price = 0.15 / 1_000_000   # $0.15 per 1M input tokens
output_token_price = 0.60 / 1_000_000  # $0.60 per 1M output tokens

# Extract token usage
input_tokens = response.usage.prompt_tokens
output_tokens = response.usage.completion_tokens

# Calculate cost
cost = (input_tokens * input_token_price) + (output_tokens * output_token_price)

print("Generated text:\n", response.choices[0].message.content)
print(f"\nEstimated cost: ${cost:.8f}")
