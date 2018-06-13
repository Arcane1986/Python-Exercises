def initials():
  valid_input = False
  while valid_input == False:
    name = input("What is your full name?(name can only contain letters and spaces) ")
    for char in name:
      if char.isalpha() or char ==" ":
        valid_input = True
      else:
        valid_input = False
        break
  name=name.strip()
  name_list = [name for name in name.split(" ")]
  initial_list = [name_part[0] for name_part in name_list]
  final_string =""
  for initial in initial_list:
    final_string+=initial
  return final_string.upper()

def main():
  print(initials())

if __name__ == '__main__':
  main()