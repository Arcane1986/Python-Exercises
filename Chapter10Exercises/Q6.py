def sum_of_squares(xs):
  squares_sum=0
  for num in xs:
    squares_sum+=num**2
  return squares_sum

def main():
  print(sum_of_squares([12,4,5]))
  print(sum_of_squares([2,3,4]))
  print(sum_of_squares([4,4,4]))
if __name__ == '__main__':
  main()