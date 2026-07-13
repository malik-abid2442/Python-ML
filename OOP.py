class MyClass:
    def __init__(self,name):
        self.name = name
    
    def greetings(self):
        return f"Hello, {self.name}!"
    
myname = MyClass("Alice")
print(myname.greetings())

class Student:
    def __init__(self,subjects="Math"):
        self.subjects = subjects


stu1 = Student()
stu1.subjects = "Science"
print(stu1.subjects)
print(stu1)

