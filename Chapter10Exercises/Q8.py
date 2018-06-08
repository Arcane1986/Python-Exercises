def five_letter_words(xs):
  five_word_count = 0
  for word in xs:
    if len(word) == 5:
      five_word_count+=1
  return five_word_count

def main():
  print(five_letter_words(["black","brown","red","blue","purple","yellow"]))
  
if __name__ == '__main__':
  main()