def count_after_prep_phrase(string):
  a = (string.index(",")+1)
  b = (len(string))
  c = b-a
  return c

print(count_after_prep_phrase("After the game, wash the dishes."))