from math import sqrt, cos, sin

class Polar(object):
    def __init__(self, angle, distance):
        self.angle = angle
        self.distance = distance
    def distance_from(self, other):
        theta1 = self.angle
        theta2 = other.angle
        r1 = self.distance
        r2 = other.distance
        return sqrt(r1*r1 + r2*r2 - 2*r1*r2*cos(theta2 - theta1))
    def to_cartesian(self):
        return Cartesian(
            cos(self.angle) * self.distance,
            sin(self.angle) * self.distance
        )
    def get_relative_cartesian(self, coordinate):
        origin_cartesian = self.to_cartesian()
        return (
            coordinate.x + origin_cartesian.x,
            coordinate.y + origin_cartesian.y
        )

class Cartesian(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_from(self, other):
        return sqrt(((self.x-other.x)**2)+((self.y-other.y)**2))