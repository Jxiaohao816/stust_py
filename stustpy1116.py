class Myshape:
    def __init__(self,side,lenght,width,radius):
        self.side = side
        self.lenght = lenght
        self.width = width
        self.radius = radius
    def __squ__(self):
        return f" 正方形面積:{self.side * self.side}"
    def __rec__(self):
        return f" 長方形面積:{self.lenght * self.width}"
    def __cir__(self):
        return f" 圓形面積:{self.radius * self.radius*  3.14}"
        
        
p1 = Myshape(7,8,5,10)

print(p1.__squ__())
print(p1.__rec__())
print(p1.__cir__())
