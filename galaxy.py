from math import pi, pow
from random import random
from star import Star

import coordinate

class Circular(object):
    def __init__(self, stars, radius, seed):
        self.radius = radius
        self._seed = seed
        self.stars = []
        for star in range(stars):
            angle = rand.random() * 2 * pi
            rad = rand.random() * radius
            self.stars.append(Star(coordinate.Polar(angle, rad)))

class Spiral(object):
    def __init__(self, stars, radius, arms, rotation_factor, rand):
        self._radius = radius
        self._arms = arms
        self._rand = rand
        self._arm_separation_distance = 2 * pi / arms
        self._arm_offset_max = 250
        self.random_offset_xy = 0.02
        self.stars = []
        for star in range(stars):
            distance = self._rand.random() * radius
            angle = self._rand.random() * 2 * pi
            distance = distance * distance
            arm_offset = self._rand.random() * self._arm_offset_max
            arm_offset = arm_offset - self._arm_offset_max / 2
            arm_offset = arm_offset * (1 / distance)
            squaredArmOffset = pow(arm_offset, 2)
            if (arm_offset < 0):
                squaredArmOffset = squaredArmOffset * -1
            arm_offset = squaredArmOffset
            rotation = float(distance * rotation_factor)
            angle = int(angle / self._arm_separation_distance) * self._arm_separation_distance + arm_offset + rotation
            self.stars.append(Star(coordinate.Polar(angle, distance)))
            #print(angle, distance)
