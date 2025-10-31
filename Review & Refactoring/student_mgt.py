# Question 1b: Refactor the student record system using OOP


#Define a Student class with properties and methods
class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark                           # Initialize student details

    def display(self):
        print(f"{self.name} => {self.mark}")


#Define a function to compute the average marks
def compute_average(students):
    #list comprehension to sum up all student marks
    total = sum(student.mark for student in students)
    
    return total / len(students)


#Create and store multiple student objects in a list
students = [
    Student("Alice", 80),
    Student("Bob", 90),
    Student("Chris", 75)
]

#Display each student's details using the class method
for s in students:
    s.display()

#Compute and display the class average
avg = compute_average(students)
print(f"Average Mark: {avg:.2f}")
