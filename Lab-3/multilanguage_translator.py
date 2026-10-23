import os
from groq import Groq


def translate_sentence(sentence, target_language, formality):
    prompt = f"""
Translate the following sentence into {target_language}.

Formality level: {formality}

Rules:
1. Preserve the original meaning.
2. Match the requested formality level.
3. Do not add explanations.
4. Return only the translated sentence.

Sentence:
{sentence}
"""

    api_key = os.environ["GROQ_API_KEY"]

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()


sentence = input("Enter sentence: ")
target_language = input("Enter target language: ")
formality = input("Enter formality (formal/informal/neutral): ")

translation = translate_sentence(
    sentence,
    target_language,
    formality
)

print("\nTranslation:")
print(translation)