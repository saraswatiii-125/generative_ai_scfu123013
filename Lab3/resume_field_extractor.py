import json
import re


def extract_fields(resume_text, fields_to_extract):
    result = {}

    for field in fields_to_extract:
        field_lower = field.lower().strip()

        if field_lower == "name":
            lines = [line.strip() for line in resume_text.split("\n") if line.strip()]
            result[field] = lines[0] if lines else None

        elif field_lower == "email":
            match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', resume_text)
            result[field] = match.group() if match else None

        elif field_lower == "phone":
            match = re.search(r'\b\d{10}\b', resume_text)
            result[field] = match.group() if match else None

        elif field_lower == "skills":
            match = re.search(
                r'Skills?\s*[:\-]\s*(.*?)(?:\n|$)',
                resume_text,
                re.IGNORECASE
            )
            if match:
                result[field] = [
                    skill.strip()
                    for skill in re.split(r',|;', match.group(1))
                    if skill.strip()
                ]
            else:
                result[field] = None

        elif field_lower == "education":
            match = re.search(
                r'Education\s*[:\-]\s*(.*?)(?:\n|$)',
                resume_text,
                re.IGNORECASE
            )
            result[field] = match.group(1).strip() if match else None

        elif field_lower == "experience":
            match = re.search(
                r'Experience\s*[:\-]\s*(.*?)(?:\n|$)',
                resume_text,
                re.IGNORECASE
            )
            result[field] = match.group(1).strip() if match else None

        else:
            result[field] = None

    return result


# Input
resume_text = input("Enter resume text: ")

fields_input = input(
    "Enter fields to extract (comma-separated): "
)

fields_to_extract = [
    field.strip()
    for field in fields_input.split(",")
    if field.strip()
]

# Extract and print JSON
result = extract_fields(resume_text, fields_to_extract)

print("\nOutput:")
print(json.dumps(result, indent=2))