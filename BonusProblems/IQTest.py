def iq_test(numbers):
  num_list = numbers.split(" ")
  odd_list=[]
  even_list=[]
  x=1
  for num in num_list:
    num = int(num)
    if num%2==0:
      even_list.append(x)
      x+=1
    else:
      odd_list.append(x)
      x+=1
  if len(even_list)==1:
    return even_list[0]
  else:
    return odd_list[0]

print(iq_test("2 4 7 8 10"))