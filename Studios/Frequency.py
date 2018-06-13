string1 ="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."
my_list=[(char,string1.count(char)) for char in string1]
new_list = set(my_list)

for data in new_list:
  (letter,count)=data
  print(f"{letter}\t{count}\n")