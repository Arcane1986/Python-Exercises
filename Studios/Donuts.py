print("Donut Studio\n")

GreetingMessage="Welcome to the Loop Hole!\nToday's Manager's Special is: "
ManagerSpecial="Crunch Jelly: A traditional jelly donut in which the jelly filling is made\
 entirely of Capn' Crunch Oops! All Berries\n"

print(GreetingMessage+ManagerSpecial)

DonutTotal=float(input("How many donuts would you like to purchase? "))
DonutPrice=float(input("How much would you like to pay per donut (suggested price is $4.35 each)? "))
TaxCost=1.05
DonutCost=round(DonutTotal*DonutPrice*TaxCost,2)

print("Ok, let me prepare that for you....\n\
After tax, your total is: ${DonutCost}\n\
Thank you for snacking! Loop back around here soon!".format(DonutCost=DonutCost))