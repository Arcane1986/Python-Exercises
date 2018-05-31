print("Chapter 3 Exercise: Thermostat")

Clicks=int(input("How many clicks did you turn the thermostat?"))
ClicksLeft=Clicks%50
if ClicksLeft < 0:
  print("The Temperature is",90-ClicksLeft)
elif ClicksLeft > 0:
  print("The Temperature is",40+ClicksLeft)
else:
  print("The Temperature is 40")