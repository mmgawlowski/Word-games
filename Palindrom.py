import re    
def Palindrome(word):
    n = len(word)

    for i in range(n):
        if word[i] != word[-1-i]:
            return False
    return True

while True:
    
    word = input('Wprowadź wyrażenie, które chcesz sprawdzić:\n')

# Palindrome by definition should contain only letter, spaces and punctuation marks.

    if re.search(r'[0-9~@#$%^&*+=<>{}~/|\[\]\\]', word) != None:
        print('Wprowadzone wyrażenie powinno zawierać jedynie litery alfabetu i znaki interpunkcyjne')
        continue
    else:
        word_t = ''.join(x for x in word if x.isalpha()).lower() # With this line, the program is almost completely insensitive to case and non-alphabetic characters.
    
    if Palindrome(word_t) == False:
        print(word + ' nie jest palindromem')
        continue
    elif re.search('[a-zA-Z]', word) == None :
        print('Znak interpunkcyjny nie jest palindromem')
    else:
        print(word + ' jest palindromem')
        continue
