def bubble_sort(alist):
    is_sorted = False
    while is_sorted == False:
      num_swaps = 0
      for a in alist:
        index_a=alist.index(a)
        if index_a<(len(alist)-1):
          b=alist[index_a+1]
          if a > b:
            alist[index_a+1]=a
            alist[index_a]=b
            num_swaps+=1
      if num_swaps == 0:
        is_sorted = True
    return alist

print(bubble_sort([1, 2, 3, 4, 5]))
print(bubble_sort([5, 4, 3, 2, 1]))
print(bubble_sort([4, 5, 3, 1, 2]))
print(bubble_sort([4, 5, -1, 1, 2]))

alist=[1, 2, 3, 4, 5]
alist.count