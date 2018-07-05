# https://www.hackerrank.com/challenges/2d-array/problem

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
  # define bounds
  #   -left number can be between index 1 between 1-4 and 4 between 1-4
  #   -use one index as reference point for sum
  hourglass_list=[]
  sum_of_hourglass=0
  for row in range(4):
    for column in range(4):
      for index_c in range(column,column+3):
        sum_of_hourglass+=arr[row][index_c]
        sum_of_hourglass+=arr[row+2][index_c]
      sum_of_hourglass+=arr[row+1][column+1]
      hourglass_list.append(sum_of_hourglass)
      sum_of_hourglass=0
  return max(hourglass_list)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()