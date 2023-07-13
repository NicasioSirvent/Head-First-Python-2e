vocales = ['a', 'e', 'i', 'o', 'u']
#palabra = "piratamalapata"
palabra = input("Dime una palabra:")
found = []

for letra in palabra:
  if letra in vocales:
    print(letra)
    if letra not in found:
      found.append(letra)

print(found)
    
    
