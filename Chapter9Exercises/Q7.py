def cipher(string1,cipher):
  ciphered_string=""
  for char in string1:
    ASCII_number = ord(char)
    if ASCII_number <= 122 and ASCII_number >=97:
      ciphered_string+=cipher[ASCII_number-97]
    elif ASCII_number <= 90 and ASCII_number >=65:
      ciphered_string+=cipher[ASCII_number-65]
    else:
      ciphered_string+=char
  return ciphered_string

def main():
  print(cipher("abcdefghijklmnopqrstuvwxyz","qwertyuiopasdfghjklzxcvbnm"))

if __name__ == '__main__':
  main()