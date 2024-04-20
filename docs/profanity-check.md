# Profanity Check

Example of checking for profane words:

```python
from sitepy import SitePy

app = SitePy()

@app.route('/' methods=['GET', 'POST'])
def index():
    if profanity_check("some string"):
        return "Contains Profanity"
    else:
        return "Does Not Contain Profanity"

app.run()
```