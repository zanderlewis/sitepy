import requests

def recaptcha(key, recaptcha_response):
    data = {
        'secret': f'{key}',
        'response': recaptcha_response
    }
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result = r.json()
    
    if result['success']:
        return True
    else:
        return False