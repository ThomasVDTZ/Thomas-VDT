class Point:
    """ Point class for representing and manipulating x,y coordinates. """   
    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0 
    def deplace(self, dx, dy):
        """ Deplace le point de dx et dy """
        self.x = self.x + dx
        self.y = self.y + dy 
    def double(self):
        self.x = self.x * 2
        self.y = self.y * 2
    def mult(self, n):
        self.x = self.x * n
        self.y = self.y * n

a = Point() 
b= Point()
print(a.x, a.y) 
"""a.x = 7 
a.y = 6   
b.x = 5 
b.y = 4 


print(a.x, a.y, b.x, b.y) 
print(a.x, b.y)"""
a.deplace(3, 4)
print(a.x, a.y)
b.deplace(5, 6)
print(b.x, b.y) 
a.double()
print(a.x, a.y)
b.double()
print(b.x, b.y)
a.mult(3)
print(a.x, a.y)
a.mult
print(a.x, a.y)

