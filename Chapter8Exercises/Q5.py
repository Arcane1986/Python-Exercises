def workout_coach(lift_name):
  wt = 10
  print("Time to", lift_name, wt, "pounds! You got this!")
  keep_going = input("Keep doing {lift_name}? ".format(lift_name=lift_name))
  while keep_going == "Yes" or keep_going == "yes":
    if lift_name != "bench":
      wt+=10
      print("Time to", lift_name, wt, "pounds! You got this!")
      keep_going = input("Keep doing {lift_name}? ".format(lift_name=lift_name))
    elif lift_name == "bench" and wt <= 190:
      wt+=10
      print("Time to", lift_name, wt, "pounds! You got this!")
      keep_going = input("Keep doing {lift_name}? ".format(lift_name=lift_name))
    else:    
      print("Time to", lift_name, wt, "pounds! You got this!")
      keep_going = input("Keep doing {lift_name}? ".format(lift_name=lift_name))

def main():
    lifts = ["squat", "bench", "deadlift"]
    for lift in lifts:
      workout_coach(lift)

if __name__ == "__main__":
    main()
