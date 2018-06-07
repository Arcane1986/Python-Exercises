def number_of_integer(integer):
  if type(integer) != type(1):
    return "Value provided is not an integer, please insert appropriate value"
  else:
    return len(str(integer))

def main():

  print(number_of_integer(0))
  print(number_of_integer("Seven"))
  print(number_of_integer(908231798327102))
  print(number_of_integer(12.01))

if __name__ == '__main__':
  main()