import random

def roll_dice(num_dice, num_rolls):
  return [[random.randrange(1,7) for dice in num_dice] for roll in num_rolls]

def sum_of_roll(double_list):
  return [sum(roll) for roll in double_list]

def yahtzee(double_list):
  count = 0
  for roll in double_list:
    if roll.count(roll[0])==len(roll):
      count+=1
  return count

print(sum_of_roll([[4, 5, 2],[6,2,1],[4,4,4]]))
print(sum_of_roll([[3, 4, 6],[2,6,1],[3,4,3]]))
print(yahtzee([[3, 4, 6],[2,6,1],[3,4,3]]))
print(yahtzee([[4, 5, 2],[6,2,1],[4,4,4]]))