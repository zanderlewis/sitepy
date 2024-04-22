# Profanity Check

Example of checking for profane words:

```python
from sitepy import SitePy
from sitepy.profanity import check_profanity

app = SitePy()

@app.route('/' methods=['GET', 'POST'])
def index():
    if check_profanity("some string"):
        return "Contains Profanity"
    else:
        return "Does Not Contain Profanity"

app.run()
```

In this example, the string `"some string"` will return `False`.