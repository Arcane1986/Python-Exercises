def caught_speeding(speed,is_birthday):
  if is_birthday and speed <= 65:
    if speed <= 65:
      return 0
    elif speed >= 66 and speed <=85:
      return 1
    else:
      return 2
  else:
    if speed <= 60:
      return 0
    elif speed >= 61 and speed <=80:
      return 1
    else:
      return 2

print(caught_speeding(84,True))
print(caught_speeding(66,False))
print(caught_speeding(84,False))
print(caught_speeding(55,False))
print(caught_speeding(65,True))