def char_count(string1):
  my_dict={}
  for char in string1:
    if my_dict.get(char)==None:
      my_dict[char]=1
    else:
      my_dict[char]+=1
  return my_dict

def word_count(string1):
  my_dict={}
  for word in string1.split(" "):
    if my_dict.get(word)==None:
      my_dict[word]=1
    else:
      my_dict[word]+=1
  return my_dict

def combined_dict(string1):
  return (word_count(string1),char_count(string1))
  
print(combined_dict("Today the weather looks very fine and tomorrow the weather looks great too."))