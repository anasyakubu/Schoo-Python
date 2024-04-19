import json
import openai


def get_recommended_fruits(q1_answer, q2_answer, q3_answer, q4_answer):
    prompt = f"""
You are a helpful assistant that recommends fruits based on user preferences.
Below are the answers to four questions about the user's fruit preferences:
Question 1: {q1_answer}
Question 2: {q2_answer}
Question 3: {q3_answer}
Question 4: {q4_answer}
Based on these answers, please provide a list of recommended fruits for the user.
Your response should be a list of fruit names, separated by commas.
"""
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100,
        n=1,
        stop=None,
        echo=False,
    )
    recommended_fruits = response.choices[0].text.strip().split(",")
    return recommended_fruits