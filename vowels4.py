vowels = ['a', 'e', 'i', 'o', 'u' ]
word = input("Palabro??:")

found = {}
#for i in vowels:
#  found[i] = 0

for letter in word:
  if letter in vowels:
    if letter not in found:
      found[letter] = 1
    else:
      found[letter] += 1

for k,v in sorted(found.items()):
  print('He encontrado la',k, v, 'veces!')

        
