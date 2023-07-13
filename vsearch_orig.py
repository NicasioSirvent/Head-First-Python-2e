def search4vowels():
  """Display tal y tal."""
  vowels = set('aeiou')
  word = input('dime tal');
  found = vowels.intersection(set(word))
  for vowel in found:
    print(vowel)
