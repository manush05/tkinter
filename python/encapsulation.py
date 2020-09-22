class Rectangle:
    def __init__(self, height ,width):
        self.__height = height
        self.__width = width

    def set_hieght(self,height):
        self.__height = height
    
    def get_height(self):
        return self.__height

    def set_width(self,width):
            self.__width = width    
    def get_width(self):
        return self.__width

    def area(self):
        return self.__height*self.__width

rect = Rectangle(20,60)

# rect.height = 200
# print(rect.__hieght)
rect.set_hieght(300)
print(rect.get_height())
# rect.width = 300
rect.set_width(100)
print(rect.get_width())
