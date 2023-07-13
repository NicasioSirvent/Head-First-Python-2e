def search4letters(phrase:str, letters:str='aeiou') -> set:
  """Return any passed letter in the passed phrase"""
  return set(phrase).intersection(set(letters))
