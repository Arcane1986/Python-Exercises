for beers in range(99,0,-1):
  beerslessone = beers-1
  if beerslessone>0:
    print("{beers} bottles of beer on the wall,\n {beers} bottles of beer,\n Take one down, pass it around, {beerslessone} bottles of beer on the wall!".format(beers=beers,beerslessone=beerslessone))
  else:
    print("{beers} bottle of beer on the wall,\n {beers} bottle of beer,\n Take one down, pass it around, no bottles of beer on the wall!".format(beers=beers,beerslessone=beerslessone))