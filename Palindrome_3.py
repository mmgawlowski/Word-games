# Simpler version of Palindrome.py without defining a new function
while True:
  word = input('Wprowadź słowo, które chcesz sprawdzić\n')
  word_t = word.lower().replace(' ', '')
  n = len(word_t)
  result = (word + ' jest palindromem')

  for i in range(n):
    if word_t[i] != word_t[-1-i]:
      result = (word + ' nie jest palindromem')

  print(result)
  continue
