# https://www.codewars.com/kata/gap-in-primes/train/python

def isprime(x):
  root=round(x**0.5)
  for i in range(2,root+1):
    if x==2:
      return x
    elif x%i==0:
      return
  return x


def gap(gap,start,finish):
  prime_list=[]
  for x in range(start,finish+1):
    if isprime(x)!=None:
      prime_list.append(x)
      if prime_list.index(x)>0:
        y = prime_list[prime_list.index(x)-1]
        difference = x - y
        if difference == gap:
          return [y,x]
  return None