import os
from google import genai


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

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()


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