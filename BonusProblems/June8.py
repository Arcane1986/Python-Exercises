def neg_list(xs):
  opp_list = []
  for num in xs:
    opp_list.append(num * -1)
  return opp_list

def main():
  print(neg_list([4,3,2,1,0,-1]))
  print(neg_list([]))

if __name__ == '__main__':
  main()
