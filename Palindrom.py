def Palindrome(word):
    n = len(word)

    for i in range(n):
        if word[i] != word[-1-i]:
            return False
    return True

while True:
    
    word = input('Wprowadź słowo, które chcesz sprawdzić\n')
    word_t = ''.join(x for x in word if x.isalpha()).lower() # With this line, the function is completely insensitive to case and non-alphabetic characters.
    
    if Palindrome(word_t) == False:
        print(word + ' nie jest palindromem')
        continue
    else:
        print(word + ' jest palindromem')
        continue
