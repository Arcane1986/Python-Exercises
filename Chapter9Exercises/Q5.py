from Q4 import reverse_string

def palindrome(string1):
  if reverse_string(string1)==string1:
    return True
  else:
    return False

def main():
  print(palindrome("banana"))
  print(palindrome("abba"))
  print(palindrome("AbbA"))
  print(palindrome("Abba"))
  print(palindrome("ABBA"))

if __name__ == '__main__':
  main()