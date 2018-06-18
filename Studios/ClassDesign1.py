class Student:
  def __init__(self, name, id, gp = 0, credits = 0):
    self.name = name
    self.id = id
    self.gradepoints = gp
    self.credits = credits
    self.gpa = self.gradepoints/self.credits if credits > 0 else 0

  def report_grade(self,grade,class_credits):
    grade_modifier = 0
    
    if grade == "A":
      grade_modifier = 4
    if grade == "B":
      grade_modifier = 3
    if grade == "C":
      grade_modifier = 2
    if grade == "D":
      grade_modifier = 1

    self.gradepoints += (grade_modifier * class_credits)
    self.credits += class_credits
    self.gpa = self.gradepoints / self.credits

  def get_class_standing(self):
    if self.credits < 30:
      return f"{self.name} is currently a Freshman."
    elif self.credits >= 30 and self.credits < 60:
      return f"{self.name} is currently a Sophmore."
    elif self.credits >= 60 and self.credits < 90:
      return f"{self.name} is currently a Junior."
    elif self.credits >= 90 and self.credits < 120:
      return f"{self.name} is currently a Senior."
    else:
      return f"{self.name} is graduating!!!"

  def __str__(self):
    return f"{self.name}"
    
  def __repr__(self):
    return f"Student({self.name},{self.id},{self.gradepoints},{self.credits})"

class Course:
  def __init__(self, name, course_number, seats=30):
    self.name = name
    self.course_number = course_number
    self.seats = seats
    self.roster = []
    self.seats_filled = len(self.roster)

  def add_student(self,student):
    if self.seats_filled < self.seats:
      self.roster+=[student]
      self.seats_filled+=1
      return f"{student} has been added to course {self.name} {self.course_number}"
    else:
      return f"{student} could not be added to course {self.name} {self.course_number} at this time since all {self.seats} seats have been filled."

  def get_student_average_gpa(self):
    total_gpa = 0
    for student in self.roster:
      total_gpa += student.gpa
    return round(total_gpa/len(self.roster),2)

a = Student("Richard",1,20,6)
b = Student("Azhar",2,40,12)
c = Student("Patrick",3,110,30)
d = Student("Kim",4,50,20)
e = Student("Megan",5,75,25)
f = Student("Joanne",6,10,4)

CHM = Course("Chemistry","CHM2201",5)

print(CHM.add_student(a))
print(CHM.add_student(b))
print(CHM.add_student(c))
print(CHM.add_student(d))
print(CHM.add_student(e))
print(CHM.add_student(f))

print(CHM.get_student_average_gpa())