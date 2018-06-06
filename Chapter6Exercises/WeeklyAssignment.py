def is_leap(year):
    if year%100==0 and year%400!=0:
        return False
    if year%4==0:
        return True
    else:
        return False
  
print(is_leap(1944), True)
print(is_leap(2011), False)
print(is_leap(1986), False)
print(is_leap(1956), True)
print(is_leap(1957), False)
print(is_leap(1800), False)
print(is_leap(1900), False)
print(is_leap(1600), True)
print(is_leap(2056), True)