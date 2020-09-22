# Inheritance
 
class Parent:
    def __init__(self):
        self.a = 123
        self.b = 123
        self.__comand = 123
        # self.__d = d
    

# class Child(Parent):
#     def __init__(self,a,b,c,d):
#         self.c = c
#         Parent.__init__(self,a,b,d)
#     def display(self):
#         print(self.a,self.b,self.__d)

# manu = Child("manu",21,"bca","rad")
# manu.display()

parentobj = Parent()
print(parentobj.a)
print(parentobj.b)
print(parentobj.__comand)
# SINGLE LEVEL INHERITANCE Ends

# class GrandParent:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b


# class Parent(GrandParent):
#     def __init__(self,a,b,c):
#         self.c = c
#         GrandParent.__init__(self,a,b)
#     def display(self):
#         print(self.a,self.b,self.c)

# class Child(Parent):
#     def __init__(self,a,b,c,d):
#         self.d = d
#         Parent.__init__(self,a,b,c)
#     def display(self):
#         print(self.a,self.b,self.c)

# childObj = Child("manu","real",21,"Ignou")
# childObj.display()

# MULTIPLE INHERITANCE Ends


# class GrandParent:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.__c = c

# class Parent:
#     def __init__(self,c):
#         self.c = c

# class Child(GrandParent,Parent):
#     def __init__(self,a,b,c,d):
#         self.d = d
#         GrandParent.__init__(self,a,b)
#         Parent.__init__(self,c)

#     def display(self):
#         print(self.a,self.b,self.c,self.d)

# childObj = Child("manu","real","html","Ignou")
# childObj.display()

# Take Different properties and put inside the child 