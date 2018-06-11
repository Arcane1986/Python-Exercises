def new_count(item,lst):
  item_count=0
  for element in lst:
    if element == item:
      item_count+=1
  return item_count

print(new_count(2,[1,2,3,4,5,6,7,8,9,2]))

def new_is_in(item,lst):
  item_count=0
  for element in lst:
    if element == item:
      item_count+=1
  return item_count>0
print(new_is_in(2,[1,2,3,4,5,6,7,8,9,2]))

def new_reverse(lst):
  new_lst=[]
  for i in range(len(lst)-1,-1,-1):
    new_lst+=[lst[i]]
  return new_lst

print(new_reverse([1,2,3,4,5,6,7,8,9,2]))

def new_insert(item,lst,insertpoint):
  new_lst=lst[:insertpoint]+[item]+lst[insertpoint:]
  return new_lst

print(new_insert("Camel",[1,2,3,4,5,6,7,8,9,2],3))

def new_index(item,lst):
  index_count=-1
  index_lst=[]
  for element in lst:
    if element==item:
      index_count+=1
      index_lst+=[index_count]
    else:
      index_count+=1
  return index_lst
print(new_index(2,[1,2,3,4,5,6,7,8,9,2]))