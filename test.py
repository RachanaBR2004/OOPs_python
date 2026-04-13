"""Create a base class Person:

Attributes: name, age
Method: display()

Create a child class Student:

Additional attribute: marks
Method: grade()
marks >= 90 → A
marks >= 75 → B
else → C """

#inheritance
"""class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print("name",self.name)
        print("age",self.age)
        
class student(person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        #super().display()
        self.marks=marks
        
    def grade(self):
        if self.marks>=90:
            print("A")
        elif self.marks>=75:
            print("B")
        else:
            print("c")
stu=student('rachana',15,50)
stu.display()
stu.grade()"""

'''class employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def display(self):
        print(f"name of the emp {self.name}")
        print(f"sal of the emp{self.sal}")
class manager(employee):
    def __init__(self,name,sal,bonus):
        super().__init__(name,sal)
        self.bonus=bonus

    def total_salary(self):
        print(f"total_sal{self.sal+self.bonus}")

class devloper(manager):
    def __init__(self,name,sal,overtime_pay,bonus):
        super().__init__(name,sal,bonus)
        self.overtime_pay=overtime_pay
    
    def total_sal(self):
        print(f"total_sal {self.sal+self.overtime_pay}")
d=devloper("rachh",50000,1500,500)
d.display()
d.total_salary()
d.total_sal()'''

#polymorphism
"""class dog:
    def sound(self):
        print("barking")
class cat:
    def sound(self):
        print("meow")
def talk(animal):
    animal.sound()

d=dog()
talk(d)
c=cat()
talk(c)"""

'''from abc import ABC,abstractmethod
class vechile(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vechile):
    def start(self):
        print("car is started")
class bike(vechile):
    def start(Self):
        print("bike is started")

def work(sound):
    sound.start()
        
c=car()
work(c)
b=bike()
work(b)

#c.start()
#b.start()'''

"""def student_result(marks):
    total_marks=sum(marks)
    avg=total_marks/len(marks)
    print(total_marks)
    print(avg)
    if avg>90:
        print("A")
    elif avg>70:
        print("B")
    else:
        print("c")
student_result([10,20,30])"""

def check_pwd(pwd):
    if len(pwd)<6:
        print("weak pwd")
    elif len(pwd)>=6 :
        print("medium")
    else:
        print("strong")
check_pwd('1235')





        
        
        
        
    










































            
            
