class computer:
    def config(self):
        print("16gb,1TB")
    def boot(self):
        print("Boot menu")
comp1 = computer()
comp2 = computer()

computer.boot(comp2)
computer.config(comp1)


class car:
    # costructor is a spl function which activate automatically on creating object of that class  
    # contructor use: At the time of object creation we can pass the value to the variable we used

    def __init__(self,name,age):
        # point the variables
        self.name = name
        self.age = age
    def display(self):
        print("my name is" ,self.name,"and i am ",self.age," years old")
    

  
honda = car("manorma","21")
honda.display()        