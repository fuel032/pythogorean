import fractions
from math import sqrt,pi
from fractions import Fraction

name = "pythogorean"

class hypo():
    def __new__(self,leg1,leg2) -> float:

        leg1 = float(leg1)
        leg2 = float(leg2)

        leg1x = leg1 * leg1
        leg2x = leg2 * leg2

        hypotenuse2x = leg1x + leg2x

        hypotenuse = sqrt(hypotenuse2x)
        return hypotenuse

class leg():
    def __new__(self,leg1,hypotenuse) -> float:

        leg1 = float(leg1)
        hypotenuse = float(hypotenuse)

        leg1x = leg1 * leg1
        hypotenusex = hypotenuse * hypotenuse

        leg2x = hypotenusex - leg1x

        leg2 = sqrt(leg2x)
        return leg2

class trans():
    def __new__(self, angle) -> float:

        if angle > 180:
            return None
        else:
            angle = float(angle)

            anglex = 180 - angle
            return anglex

class alt():
    def __new__(self,a,b) -> float:
        a = float(a)
        b = float(b)

        c = a + b

        if c > 180:
            return None
        else:
            return c

class area():
    def __new__(self,length,width) -> float:
        
        length = float(length)
        width = float(width)

        area = length * width
        return area

class PI():
    def __new__(self) -> float:
        p = pi
        return p

class vol():
    def __new__(self,length,width,height) -> float:
        
        length = float(length)
        width = float(width)
        height = float(height)

        volume = length * width * height
        return volume

class circ():
    def __new__(self,radius) -> float:
        
        radius = float(radius)
        p = PI()

        C = 2 * p * radius
        return C

class rad():
    def __new__(self,circumference) -> float:
        
        circumference = float(circumference)

        d = circumference / PI()
        r = d / 2

        return r

class slope():
    def __new__(self,rise,run) -> int:
        rise = int(rise)
        run = int(run)

        s = Fraction(rise,run)
        return s

class yint():
    def __new__(self,m,x,b) -> float:
        m = float(m)
        x = float(x)
        b = float(b)

        y = m * x + b
        return y

class cbrt():
    def __new__(self,num) -> float:
        
        num = float(num)

        final = num ** (1./3)
        return round(final, 9)

class qdrt():
    def __new__(self,num) -> float:
        
        num = float(num)

        final = num ** (1./4)
        return round(final, 9)

class ffrt():
    def __new__(self,num) -> float:
        
        num = float(num)

        final = num ** (1./5)
        return round(final, 9)

class conv():
    def __new__(self,leg1,leg2,hypotenuse) -> bool:
        
        leg1 = float(leg1)
        leg2 = float(leg2)

        hypotenuse = float(hypotenuse)

        leg1x = leg1 * leg1
        leg2x = leg2 * leg2

        hypotenusex = hypotenuse * hypotenuse

        if leg1x + leg2x == hypotenusex:
            return True
        else:
            return False

class sq():
    def __new__(self,num) -> float:

        num = float(num)

        numx = num * num
        return numx

class cube():
    def __new__(self,num) -> float:

        num = float(num)

        numx = vol(num,num,num)
        return numx

class quad():
    def __new__(self,num) -> float:

        num = float(num)

        numx = num * num * num * num
        return numx