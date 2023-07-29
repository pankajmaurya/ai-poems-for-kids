from initopenai import openai

def get_completion_kids(prompt, model="gpt-3.5-turbo"):
    messages = [
        {"role": "system", "content":
            "The answer is intended for a 4 year old boy. Format your answer like a poem using html <br/> tags for indentation. Keep your responses in word limit of 100 words and return response as a valid html fragment."},
        {"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"].replace("\n", "<br/>")

def analyzeCodeKids(code):
    # Implement your code analysis logic here
    # This is just a placeholder example
    hints = [get_completion_kids(code)[:1000]]
    return hints