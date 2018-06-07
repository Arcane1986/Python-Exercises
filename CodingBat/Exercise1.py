def combo_string(string1,string2):
  string1=str(string1)
  string2=str(string2)
  if len(string1)>len(string2):   # Parameter 1 > Parameter 2
    return string2+string1+string2
  elif len(string1)==len(string2):  # Parameter 1 = Parameter 2
    return "Strings are the same length, please submit different length strings"
  else: # Parameter 1 < Parameter 2
    return string1+string2+string1

def main():

  print(combo_string("January","June"))
  print(combo_string(21,333))
  print(combo_string(444,"MMM"))

if __name__ == "__main__":
  main()