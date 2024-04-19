import sitepy
import sitepy.profanity as p

app = sitepy.SitePy()

@app.route('/')
def main():
    return str(p.check_profanity('some-word-here'))