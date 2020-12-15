class Shape:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self._a = a
        self.b = par_b

    def get_a(self):
        return self._a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


class Rectangle(Shape):
    def calc_surface(self):
        return self._a*self.b

    def calc_area(self):
        return 2*self._a + 2*self.b

    def swap_sides(self):
        a = self._a
        b = self.b
        self._a = b
        self.b = a

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

import math

class EquilateralTriangle(Shape):
    def __init__(self, a):
        super().__init__(a,0)

    def calc_surface(self):
            return (pow(self._a , 2) * math.sqrt(3)) / 2

    def calc_area(self):
        return 3 * self._a

class Triangle(Shape):
    def __init__(self, a, b):
        super().__init__(a, b)

    def calc_surface(self):
            return 0.5 * self._a * self.b

class Circle(Shape):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, 0)
        #self._a = a

    def calc_surface(self):
        return math.pi * self._a**2

    def calc_area(self):
        return 2 * math.pi * self._a

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))

r = Rectangle(5, 6)
print(r)
print(r.calc_surface())
print(r.calc_area())
r.swap_sides()
print(r)

c = Circle(7)
print(c)
print(c.calc_surface())
print(c.calc_area())

d = Triangle(1,4)
print(d)
print(d.calc_surface())

e = EquilateralTriangle(4)
print(e)
print(e.calc_surface())
print(e.calc_area())

f = Square(4)
print(f)
print(f.calc_surface())