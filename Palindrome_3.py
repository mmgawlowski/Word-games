# Simpler version of Palindrome.py without defining a new function
while True:
  word = input('Wprowadź słowo, które chcesz sprawdzić\n')
  n = len(word)
  result = (word + ' jest palindromem')

  for i in range(n):
    if word[i] != word[-1-i]:
      result = (word + ' nie jest palindromem')

  print(result)
  continue
