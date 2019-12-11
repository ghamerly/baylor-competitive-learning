import math
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return (self.x, self. y) < (other.x, other.y)

    def __eq__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, a):
        return Point(self.x*a , self.y*a)

    def __truediv__(self, other):
        return Point(self.x/other, self.y/other)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.x + self.y * other.y

    def dist2(self):
        return self.x * self.x + self.y *self.y

    def dist(self):
        return math.sqrt(float(self.dist2()))

    def angle(self):
        return math.atan2(self.y, self.x)

    def unit(self):
        return self/self.dist()

    def perp(self):
        return Point(-self.y, self.x)

    def normal(self):
        return self.perp().unit()

    def rotate(self, a):
        return Point(self.x*math.cos(a) - self.y*math.sin(a),
                     self.x*math.sin(a) + self.y*math.cos(a))
    def __str__(self):
        return  "(" + str(self.x) +  "," + str(self.y) + ")"