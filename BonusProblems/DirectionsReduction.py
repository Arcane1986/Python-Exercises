# http://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

def dirReduc(arr):
  new_list=arr
  count = 0
  while True:
    count = 0
    for item in range(len(new_list)):
      if item + 1 < len(new_list):
        if new_list[item] == 'NORTH' and new_list[item+1] == 'SOUTH':
          new_list = new_list[:item]+new_list[item+2:]
          count+=1
        elif new_list[item] == 'SOUTH' and new_list[item+1] == 'NORTH':
          new_list = new_list[:item]+new_list[item+2:]
          count+=1
        elif new_list[item] == 'EAST' and new_list[item+1] == 'WEST':
          new_list = new_list[:item]+new_list[item+2:]
          count+=1
        elif new_list[item] == 'WEST' and new_list[item+1] == 'EAST':
          new_list = new_list[:item]+new_list[item+2:]
          count+=1
    if count == 0:
      return new_list
    else:
      continue

print(dirReduc(["NORTH",'SOUTH',"NORTH",'SOUTH','NORTH',"NORTH",'SOUTH','NORTH','SOUTH','EAST']))
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))