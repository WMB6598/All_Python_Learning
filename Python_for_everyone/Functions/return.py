#return ends the indent

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('en'), 'Glenn')
print(greet('fr'), 'Glenn')
print(greet('es'), 'Glenn')