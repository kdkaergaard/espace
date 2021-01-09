from enum import Enum

#class Classification(Object):

class SpectralType(Enum):
    O = 1
    B = 2
    A = 3
    F = 4
    G = 5
    K = 6
    M = 7

class Star(object):
    def __init__(self,  coordinate):
        self.coordinate = coordinate
