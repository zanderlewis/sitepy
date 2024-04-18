import openai

def gpt(key, engine, text):
    openai.api_key = key
    response = openai.Completion.create(
        engine=f"{engine}",
        prompt=text,
        max_tokens=100
    )
    return response.choices[0].text