def split_line(input):
  line_list = input.split("\n")
  new_line_list =[]
  newer_line_list = []
  newest_line_list = []
  for line in range(len(line_list)):
    new_line_list.append(line_list[line].split(","))
  for item in range(len(new_line_list[0])):
    for lst in range(len(new_line_list)):
      newer_line_list.append(new_line_list[lst][item])
    newest_line_list.append(newer_line_list)
    newer_line_list = []
  return sorted(newest_line_list, key = lambda person:person[0].upper())

input = "rich,azhar,Patrick\n1,2,3\n3,2,1\na,b,c"

print(split_line(input))

def print_list(input):
  new_string = ""
  lst = split_line(input)
  for index_c in range(len(lst[0])):
    for index_r in range(len(lst)):
      new_string+=lst[index_r][index_c]
      if index_r + 1 < len(lst):
        new_string+=","
    new_string+="\n"
  return new_string

print(print_list(input))

