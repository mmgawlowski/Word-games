import re

def anagram(word_1, word_2):
  if len(word_1) != len(word_2):
    return False
  
  n = len(word_1)
  
  for i in range(n):
    if re.findall(word_1[i], word_1) != re.findall(word_1[i], word_2,):
      return False
  return True

while True:
  
  while True:
    word_1 = input('Wprowadź wyrażenie, które chcesz sprawdzić:\n')
    if re.search(r'[0-9~@#$%^&*+=<>{}~/|\[\]\\]', word_1) != None:
      print('Wprowadzone wyrażenie powinno zawierać jedynie litery alfabetu i znaki interpunkcyjne')
      continue
    elif re.search('[a-zA-Z ]|^$', word_1) == None:
      print('Wyrażenie nie powinno składać się wyłącznie ze znaków interpunkcyjnych')
      continue
    else:
      word_1_t = ''.join(x for x in word_1 if x.isalpha()).lower()
      break

  while True:
    word_2 = input('Wprowadź wyrażenie, które ma być porównane z pierwszym:\n')
    if re.search(r'[0-9~@#$%^&*+=<>{}~/|\[\]\\]', word_2) != None:
      print('Wprowadzone wyrażenie powinno zawierać jedynie litery alfabetu i znaki interpunkcyjne')
      continue
    elif re.search('[a-zA-Z ]|^$', word_2) == None:
      print('Wyrażenie nie powinno składać się wyłącznie ze znaków interpunkcyjnych')
      continue
    else:
      word_2_t = ''.join(x for x in word_2 if x.isalpha()).lower()
      break
  
  if anagram(word_1_t, word_2_t) == False:
    print(word_1 + ' nie jest anagramem ' + word_2)
    continue
  else:
    print(word_1 + ' jest anagramem ' + word_2)
    continue
