while True:
    word = input('Wprowadź słowo, które chcesz sprawdzić\n')
    rev = word[::-1] # [::-1] reverses whole string
    if word.lower() != rev.lower():
        print(word + ' nie jest palindromem')
        continue
    else:
        print(word + ' jest palindromem')
        continue
