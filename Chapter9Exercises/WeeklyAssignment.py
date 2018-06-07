import string
string1 = "This is a test"

def analyze_text(string1):
  E_count = string1.count("e")+string1.count("E")
  letter_count = 0
  for char in string1:
    if char in string.ascii_letters:
      letter_count+=1
  E_percent = round((E_count/letter_count*100),2)
  
  return f"The text contains {letter_count} alphabetic characters, of which {E_count} ({E_percent}%) are ‘e’"

def main():
  print(analyze_text("Where can I find the nearest gas station?"))
  print(analyze_text("123456789999TtttttTTTTTT"))

if __name__ == '__main__':
  main()