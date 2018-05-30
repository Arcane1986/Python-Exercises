print("Problem Three Program")
CurrentTime = int(input("What is the current time in hours rounded to the nearest hour? "))
TimetoAlarm = int(input("How many hours until you want your alarm to go off? "))
AlarmTime = (CurrentTime+TimetoAlarm)%24
print("Your alarm will go off at {AlarmTime}:00".format(AlarmTime=AlarmTime))