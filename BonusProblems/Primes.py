# Primes are numbers only divisible by 1 and itself
# https://www.codewars.com/kata/gap-in-primes/train/python

def isprime(x):
  root=round(x**0.5)
  for i in range(2,root+1):
    if x==2:
      return x
    elif x%i==0:
      return
  return x


def prime_list(start,finish):
  prime_list=[]
  for x in range(start,finish+1):
    if isprime(x)!=None:
      prime_list.append(x)
  return prime_list

def prime_gap(gap,start,finish):
  x=0
  a=prime_list(start,finish)
  while True:
    if (x + 1) == len(a):
      return None
    elif a[x+1] - a[x] == gap:
      return [a[x],a[x+1]]
    x+=1

print(prime_gap(4,1,100))
    

