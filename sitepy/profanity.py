from .word_list import words as w


def check_profanity(text):
    # Check for profane phrases
    for phrase in w:
        if phrase.lower() in text.lower().split():
            return 1

    # Check for profane words
    words = text.split()
    for word in words:
        if word.lower() in w:
            return 1

    return 0
