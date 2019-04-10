while True:
    word = input('Wprowadź słowo, które chcesz sprawdzić\n')
    rev = word[::-1] # [::-1] reverses whole string
    if word.lower().replace(' ', '') != rev.lower().replace(' ', ''): # .lower() and .replace() make function case and whitespace insensitive
        print(word + ' nie jest palindromem')
        continue
    else:
        print(word + ' jest palindromem')
        continue
