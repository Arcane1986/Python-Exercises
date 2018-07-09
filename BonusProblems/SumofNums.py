# http://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

def get_sum(a,b):
  sum_of_nums=0
  if a > b:
    for num in range(b,a+1):
      sum_of_nums+=num
  elif a < b:
    for num in range(a,b+1):
      sum_of_nums+=num
  else:
    sum_of_nums=a
  return sum_of_nums