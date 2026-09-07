from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)


# INPUT: ENTER MULTI-LINE MEETING TRANSCRIPT


print("Enter the meeting transcript.")
print("Type END when you are finished:")

lines = []

while True:
    line = input()

    if line == "END":
        break

    lines.append(line)

transcript = "\n".join(lines)


# STEP 1: EXTRACT WHAT WAS DISCUSSED


prompt1 = f"""
You are a meeting analysis assistant.

Analyze the following raw meeting transcript.

Extract:
1. Main topics discussed
2. Key points
3. Decisions made
4. Problems or issues mentioned

Return the result as structured JSON.

Transcript:
{transcript}
"""

response1 = client.chat.completions.create(
    model="YOUR_MODEL",
    messages=[
        {"role": "user", "content": prompt1}
    ]
)

step1 = response1.choices[0].message.content

print("\n========== STEP 1: DISCUSSION EXTRACTION ==========")
print(step1)


# STEP 2: IDENTIFY ACTION ITEMS

prompt2 = f"""
You are an action-item extraction assistant.

From the meeting discussion below, identify every action item.

For each action item, extract:
- task
- owner
- deadline

If the owner is not mentioned, write "OWNER MISSING".

If the deadline is not mentioned, write "DEADLINE MISSING".

Also include a flag:
- "OK" when owner and deadline are available
- "OWNER MISSING" when owner is missing
- "DEADLINE MISSING" when deadline is missing
- "OWNER AND DEADLINE MISSING" when both are missing

Return the result as structured JSON.

Meeting discussion:
{step1}
"""

response2 = client.chat.completions.create(
    model="YOUR_MODEL",
    messages=[
        {"role": "user", "content": prompt2}
    ]
)

step2 = response2.choices[0].message.content

print("\n========== STEP 2: ACTION ITEMS ==========")
print(step2)


# STEP 3: FINAL MEETING REPORT

prompt3 = f"""
You are a meeting summary assistant.

Create a clear final meeting report using the discussion and
action items below.

Include:
1. Meeting Summary
2. Topics Discussed
3. Key Decisions
4. Action Items
5. Missing Information

Clearly highlight missing owners and deadlines.

Discussion:
{step1}

Action Items:
{step2}
"""

response3 = client.chat.completions.create(
    model="YOUR_MODEL",
    messages=[
        {"role": "user", "content": prompt3}
    ]
)

step3 = response3.choices[0].message.content

print("\n========== STEP 3: FINAL MEETING REPORT ==========")
print(step3)