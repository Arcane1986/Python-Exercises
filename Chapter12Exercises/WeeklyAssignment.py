class Car:
  def __init__(self,gas_level):
    self.gas_level=gas_level

  def add_gas(self,gas_added):
    return self.gas_level + gas_added

  def fill_up(self):
      gas_needed=0
      while self.gas_level < 13.0:        
        self.gas_level+=0.5
        gas_needed+=0.5
      return gas_needed

print(Car(10).fill_up() == 3 )
print(Car(20).fill_up() == 0 )
print(Car(5.5).fill_up() == 7.5 )
print(Car(12.5).fill_up() == 0.5 )
print(Car(13).fill_up() == 0 )