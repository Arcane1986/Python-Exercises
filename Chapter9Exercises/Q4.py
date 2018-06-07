def reverse_string(string1):
  reversed_string1=""
  for char in string1:
    reversed_string1=char+reversed_string1
  return reversed_string1

def main():
  print(reverse_string("This is a string"))
  print(reverse_string("So is this"))
if __name__ == '__main__':
  main()