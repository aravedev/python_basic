
my_student = {

    'name':'Rolf Smith',
    'grades':[70,88,90,99]

}

# Average grade of student
"""
def average_grade(student):
    sum =0
    total_grades = len(student['grades'])
    for x in student['grades']:
        sum = sum + x
    return f'Average grade for {student["name"]} : {sum/total_grades}'

"""
def average_grade(student):
    return (sum(my_student['grades'])/len(student['grades']))

print(average_grade(my_student))

# Defining an object

class Student: # Class 
    def __init__(self, new_name, new_grade): # Defining our constructor
        self.name=new_name
        self.grades=new_grade

    def average(self):
        return (sum(self.grades)/len(self.grades))
    
    def total_grades(self):
        return len(self.grades)

    def message(self):
        return f'{self.name} : took this semester {self.total_grades()} subject(s) with an average of : {self.average()}/100'


# Creating our stduent object -> self is a blanck object
student_one = Student("Danny Rave",[70,88,90,99])
print(student_one.name)
print(student_one.grades)
print(student_one.average())
print(student_one.total_grades())
print(student_one.message())
