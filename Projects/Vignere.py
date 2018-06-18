def alphabet_position(letter):
  lower_letters = "abcdefghijklmnopqrstuvwxyz"
  upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  if letter.isalpha():
    if letter.islower():
      return lower_letters.index(letter)
    else:
      return upper_letters.index(letter)
  else:
    return 0

def encrypt(text, codeword):
  encrypted_string = ""
  lower_letters = "abcdefghijklmnopqrstuvwxyz"
  upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  incrementer = 0
  for char in text:
    if char.isalpha():
      rotated_char_position = (alphabet_position(char)+alphabet_position(codeword[(incrementer%(len(codeword)))]))%26
      if char.islower():
        encrypted_string += lower_letters[rotated_char_position]
        incrementer+=1
      else:
        encrypted_string += upper_letters[rotated_char_position]
        incrementer+=1
    else:
      encrypted_string += char
  return encrypted_string

def main():
  text = input("Please write the statement you wish to encrypt:\n>>> ")
  codeword = input("Please input codeword:\n>>> ")
  print(encrypt(text,codeword))
if __name__ == '__main__':
  main()
