def word_count(string1):
  my_dict={}
  for word in string1.split(" "):
    if my_dict.get(word)==None:
      my_dict[word]=1
    else:
      my_dict[word]+=1
  return my_dict

print(word_count("Today the weather looks very fine and tomorrow the weather looks great too."))