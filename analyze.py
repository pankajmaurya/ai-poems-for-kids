from initopenai import openai

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [
        {"role": "system", "content":
            "Your are an AI assistant tutor for teaching coding. Keep your responses in word limit of 100 words."},
        {"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def analyzeCode(code):
    # Implement your code analysis logic here
    # This is just a placeholder example
    hints = [get_completion(code)[:1000]]

    if 'for' not in code:
        hints.append("Consider using a 'for' loop to iterate over elements.")

    if 'if' not in code:
        hints.append("Consider using an 'if' statement to add conditional logic.")

    # Add more analysis and hints as needed

    return hints
