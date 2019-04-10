def Palindrome(word):
    n = len(word)

    for i in range(n):
        if word[i] != word[-1-i]:
            return False
    return True

while True:
    
    word = input('Wprowadź słowo, które chcesz sprawdzić\n')

    if Palindrome(word.lower().replace(' ', '') == False: # .lower and .replace are used to make our function case and whitespace insensitive
        print(word + ' nie jest palindromem')
        continue
    else:
        print(word + ' jest palindromem')
        continue
