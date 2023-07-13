def search4vowels(word):
  """Return any vowel found in a supplied word."""
  vowels = set('aeiou')
  return vowels.intersection(set(word))

def search4letters(phrase:str, letters:str='aeiou') -> set:
  """Return any passed letter in the passed phrase"""
  return set(phrase).intersection(set(letters))
