import openai


def gpt(key, engine, max_tokens, text):
    openai.api_key = key
    response = openai.Completion.create(
        engine=f"{engine}", prompt=text, max_tokens=max_tokens
    )
    return response.choices[0].text
