def is_sorted(string):
  for x in range(len(string)+1):
    if ord(string[x])<=ord(string[x+1]):
      return True
    else:
      return False

print(is_sorted("abcdefghi"))