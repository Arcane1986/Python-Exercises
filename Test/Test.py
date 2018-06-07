def func(a):
  str1=''
  for b in range(a+1):    
    for c in range(a+1):
      d=b*c
      str1 = str1+str(d)+ ' '
    str1 = str1+"\n"
  return str1

print(func(3))