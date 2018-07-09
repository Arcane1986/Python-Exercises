def Descending_Order(num):
    list = sorted(str(num),reverse=True)
    num_string = ""
    for num in list:
      num_string+=num
    return int(num_string)

print(Descending_Order(83242834))
