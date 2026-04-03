'''class person:
    """simple demo"""
    name="rachana"
    age=21

    def talk(self):
        print("name is =",self.name)
        print("age is =",self.age)
    
p=person()
print(f"{p.name}\n {p.age}")
p.talk()'''



'''class person:
    """ simple demo"""
    def data(self):
        self.name='rachana'
        self.age=21

    def talk(self):
        print("name is =",self.name)
        print("age is =",self.age)
    
p=person()
p.data()
print(f"{p.name}\n {p.age}")

p.talk()'''


'''class person:
    """ simple demo"""
    def data(self,n,a,s):
        self.name=n
        self.age=a
        self.salary=s

    def talk(self):
        print("name is =",self.name)
        print("age is =",self.age)
        print("age is =",self.salary)

p=person()
p.data('rachana',21,50000)
p.talk()'''

'''class person:
    """ simple demo"""
    def data(self,n='rachana',a=21,s=50000):
        self.name=n
        self.age=a
        self.salary=s

    def talk(self):
        print("name is =",self.name)
        print("age is =",self.age)
        print("age is =",self.salary)

p=person()
p.data()
p.talk()'''


class fruit:
    def decay(self,s,c,sh):
        self.size=s
        self.color=c
        self.shape=sh;
    def ripe(self):
        print("size=",self.size)
        print("color=",self.color)
        print("shape=",self.shape)
apple=fruit()
apple.decay(20,"red","circle")
apple.ripe()



        











# create more than one -object
'''class person:
    """ simple demo"""
    def data(self,n='rachana',a=21,s=50000):
        self.name=n
        self.age=a
        self.salary=s

    def talk(self):
        print("name is =",self.name)
        print("age is =",self.age)
        print("age is =",self.salary)
        print("dept is=",self.dept)

p=person()
p.dept="training"
p.data()
p.talk()

print("===================")
p2=person()
p2.dept="CE"
p2.data("hitha",22,30000)
p2.talk()'''
































