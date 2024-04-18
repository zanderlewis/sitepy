from profanity import profanity

# Load custom profanity words from a text file
with open('list.txt', 'r') as f:
    custom_profanity_words = f.read().splitlines()

# Add custom profanity words to the profanity list
profanity.load_words(custom_profanity_words)

def check_profanity(text):
    if profanity.contains_profanity(text):
        return 1
    else:
        return 0
