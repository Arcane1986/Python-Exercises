def initials():
  name = input("What is your full name? ")
  name1=name[:name.find(" ")]
  name2=name[name.find(" ")+1:]
  name_initials = (name1[0] + name2[0])
  return name_initials.upper()
def main():
  print(initials())

if __name__ == '__main__':
  main()