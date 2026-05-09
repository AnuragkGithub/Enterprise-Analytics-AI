import ollama
import re

def detect_query(question):

    response = ollama.chat(
        model="stdatabuddy",
        messages=[{"role": "user", "content": question}]
    )

    raw_output = response["message"]["content"]

    # extract query id like query_01
    match = re.search(r"query_\d+", raw_output)

    if match:
        return match.group(0)

    return None