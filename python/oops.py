# oops is a object oriented programmming approach
# oops concept match with real life

# oops:
# class - design/car 
# object 

class Car:
    # 1st word should be capital
    # we can access properties of class only thru object
    color = "Red"
    door = 4
    tyre = 4
    mirror = 2
    def structure(self):
        # self used to point
        print("hi there is 4 tyre, 2 mirrors, 4 door")

# create an object
honda = Car()
# know the type 
print(type(honda))
# Acess Variable
print(honda.door)
print(honda.tyre)
# Acess function inside class / method 
honda.structure()


class Bike:
    # costructor is a spl function which activate automatically on creating object of that class  
    # contructor use: At the time of object creation we can pass the value to the variable we used

    def __init__(self,brand,model):
        # point the variables
        self.brand = brand
        self.model = model
        print("object initiation")
    def display(self):
        print("Brand is :",self.brand,"and Model No. is ",self.model)

vehicle = Bike("tvs","2020")

vehicle.display()
print(vehicle.brand)
print(vehicle.model)
