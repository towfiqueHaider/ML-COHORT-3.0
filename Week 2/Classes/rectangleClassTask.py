class Rectangle:    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def getArea(self):
        area = self.length * self.breadth
        return area
    
l = int(input("Length of triangle: "))
b = int(input("Breadth of triangle: "))

rect1 = Rectangle(l,b)
print(rect1.getArea())



    
        