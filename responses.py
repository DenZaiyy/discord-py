from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice([
            'I don\'t know what you mean...',
            'I don\'t understand...',
            'I\'m sorry, I don\'t know what you mean...',
            'I\'m sorry, I don\'t understand...',
            'I\'m sorry, I can\'t help you with that...',
            'I\'m sorry, I can\'t understand that...'
        ])