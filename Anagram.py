import re

def anagram(word_1, word_2):
  if len(word_1) != len(word_2):
    return False
  
  n = len(word_1)
  
  for i in range(n):
    if re.findall(word_1[i], word_1) != re.findall(word_1[i], word_2):
      return False
  return True

while True:
  
  word_1 = input('Wprowadź wyrażenie, które chcesz sprawdzić:\n')
  word_2 = input('Wprowadź wyrażenie, które ma być porównane z pierwszym:\n')
  
  word_1_t = ''.join(x for x in word_1 if x.isalpha()).lower()
  word_2_t = ''.join(x for x in word_2 if x.isalpha()).lower()
  
  if anagram(word_1_t, word_2_t) == True:
    print(word_1 + ' jest anagramem ' + word_2)
    continue
  else:
    print(word_1 + ' nie jest anagramem ' + word_2)
    continue
