
# imaginary number object
class Imaginary:

    def __init__ (self, re, im):
        self.re = re
        self.im = im

    def add (self, other):
        r = self.re + other.re
        i = self.im + other.im
        return Imaginary(r, i)

    def subtract (self, other):
        r = self.re - other.re
        i = self.im - other.im
        return Imaginary(r, i)

    def multiply (self, other):
        r = (self.re * other.re) - (self.im * other.im)
        i = (self.re * other.im) + (self.im * other.re)
        return Imaginary(r, i)

    def get_distance_sq (self):
        return (self.re * self.re) + (self.im * self.im)

    def pow (self, p):
        c = Imaginary(self.re, self.im)
        for i in range(0, p - 1):
            c = c.multiply(c)
        return c
