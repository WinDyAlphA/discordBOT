import random

def handleResponse(msg) -> str:
    p_message = msg.lower()
    
    if p_message.startswith('hello'):
        return 'Hello, world!'
    elif p_message.startswith('roll'):
        return str(random.randint(1, 100))
    elif p_message.startswith('help'):
        return 'Help is on the way!'

    return 'wtf'