class Dog:
  def __init__(self,color, age, weight, name = "George", happiness = 100, breed = "Labrador Retriever"):
    self.color = color
    self.age = age
    self.weight = weight
    self.name = name
    self.happiness = happiness
    self.breed = breed
    
    
  def eat(self,dog_food_brand):
    if dog_food_brand == "Kirkland":
      self.weight+=1
      self.happiness+=5
    elif dog_food_brand == "Purina" or "Pedigree":
      self.weight-=1
      self.happiness-=5
    else:
      pass

  def __repr__ (self):
    return f"Dog({self.color}, {self.age}, {self.weight}, {self.name}, {self.happiness}, {self.breed})"  

class Dog_Food:
  def __init__(self,brand = "Kirkland",size = "medium", taste = "Good"):
    self.brand=brand
    self.size=size
    self.taste=taste

  def __repr__(self):
    return f"Dog_Food({self.brand}, {self.size}, {self.taste})"

Georgey = Dog("black",0.5 ,49)
food = Dog_Food()

print(Georgey)
print(food)