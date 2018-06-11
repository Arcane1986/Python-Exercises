def new_list(string1):                          #step 1 creates list from string
  new1_list = [letter for letter in string1]
  return new1_list

def replace(string1,old,new):                   #step 2: removes old value and adds new value
  list_string = new_list(string1)
  replace_list = []
  for item in list_string:
    if item == old:
      replace_list+=new
    else:
      replace_list+=item
  final_list = combine_list(replace_list)
  return final_list
  
def combine_list(replace_list):                 #step 3: creates string from list
  final_list = ""
  for item in replace_list:
    final_list+=item
  return final_list

def main():
  print(replace("What in the world!","w","v"))

if __name__ == '__main__':
  main()