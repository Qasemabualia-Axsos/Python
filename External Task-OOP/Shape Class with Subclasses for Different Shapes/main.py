class Shape:
    def __init__(self,name):
        self.name=name
    
    def area(self):
        return("Area")
    
    def perimeter(self):
        return ("Perimeter")


class Circle(Shape):
    def __init__(self, name,radius):
        super().__init__(name)
        self.radius=radius
    
    def area(self):
        return 3.141592653589793*self.radius **2
    
    def perimeter(self):
        return 2*3.141592653589793*self.radius
    

class Square(Shape):
    def __init__(self, name,side):
        super().__init__(name)
        self.side=side
    
    def area(self):
        return self.side*self.side

    def perimeter(self):
        return 4*self.side


class Triangle(Shape):
    def __init__(self, name,a,b,c):
        super().__init__(name)
        self.a=a
        self.b=b
        self.c=c

    def area(self):
        s=(self.a+self.b+self.c) / 2 
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) **0.5
    
    def perimeter(self):
       return self.a+self.b+self.c

C=Circle("circle",7)

print("circle area:", C.area())
print("circle perimeter:", C.perimeter())

S=Square("square",3)

print("square area:", S.area())
print("square perimeter:", S.perimeter())


T=Triangle("triangle",3,6,8)

print("triangle area:", T.area())
print("triangle perimeter:", T.perimeter())