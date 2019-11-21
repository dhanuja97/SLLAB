
Skip to content
Pull requests
Issues
Marketplace
Explore
@dhanuja97

1
0

    2

sach999/ScriptingLab
Code
Issues 0
Pull requests 0
Actions
Projects 0
Wiki
Security
Insights
ScriptingLab/ScriptingLab/PyCol/AssignmentQ9.py /
@sach999 sach999 Update AssignmentQ9.py 11f7ce8 on Sep 6
48 lines (33 sloc) 1.01 KB
You're using jump to definition to discover and navigate code.
Learn more or give us feedback
# i)Create class having attributes name, age and marks of 3 subjects
class Student:

    # ii) Create a constructor accepting the values
    def __init__(self, name, age, marks):

        self.name = name
        self.age = age
        self.marks = marks[:]

    # iii) Member function to display the details
    def display(self):
        print("NAME: ", self.name)
        print("AGE: ", self.age)
        i = 1
        for mark in self.marks:
            print("Mark ", i, ") = ", mark)
            i += 1


# iv) Ask user for the inputs
marks = []


def accept():
    name = input("Enter name of the student: ")
    age = input("Enter age of the student: ")
    print("Enter 3 marks")
    for i in range(3):
        marks.append(input())

    return name, age, marks


name, age, marks = accept()

s1 = Student(name, age, marks)

marks = []

name, age, marks = accept()

s2 = Student(name, age, marks)

# v) calling display function
print(s1.display())
print()
print(s2.display())

    © 2019 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

    Contact GitHub
    Pricing
    API
    Training
    Blog
    About


