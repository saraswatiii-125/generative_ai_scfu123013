from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

response = client.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",
    messages=[
        {
            "role": "user",
            "content": "Say hello"
        }
    ]
)

print(response.choices[0].message.content)