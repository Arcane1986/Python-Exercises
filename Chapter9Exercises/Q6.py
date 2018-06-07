from Q4 import reverse_string

def mirror_string(string1):
  mirrored_string = string1+reverse_string(string1)
  return mirrored_string

def main():
  print(mirror_string("Richard"))
  print(mirror_string("Banana"))
  print(mirror_string("Coagulation"))

if __name__ == '__main__':
  main()