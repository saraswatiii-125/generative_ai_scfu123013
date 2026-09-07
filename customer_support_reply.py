def generate_support_reply(customer_message, company_name, max_words):
    prompt = f"""
You are a professional customer support representative for {company_name}.

Generate a helpful, polite, and professional reply to the customer's message.

Rules:
1. Keep the tone friendly, empathetic, and professional.
2. Address the customer's concern clearly.
3. Do not make up information or promises.
4. Keep the reply within {max_words} words.
5. Return only the customer support reply.
6. Do not include a subject line or explanation.

Customer message:
{customer_message}
"""

    # For this exercise, the prompt is generated and displayed.
    # Replace this section with an API call if an LLM API is required.
    print("\nGenerated Prompt:\n")
    print(prompt)


# Taking input from the user
customer_message = input("Enter customer message: ")
company_name = input("Enter company name: ")
max_words = int(input("Enter maximum words: "))

generate_support_reply(customer_message, company_name, max_words)