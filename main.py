#!/usr/bin/env python3

import sys, pygame, random, math
from pprint import pprint

from galaxy import Spiral
from coordinate import Cartesian

pygame.init()

clock = pygame.time.Clock()

#random.seed(8314569173651)

size = width, height = 1000, 1000
center = center_x, center_y = width / 2, height / 2
speed = -0.0001
#angle = 0
#background = 51
#star_count = 450
star_count = 4000

black = 0, 0, 0
background = 51, 51, 51
white = 255, 255, 255

def create_fonts(font_sizes_list):
    "Creates different fonts with one list"
    fonts = []
    for size in font_sizes_list:
        fonts.append(
            pygame.font.SysFont("Arial", size))
    return fonts

fonts = create_fonts([32, 16, 14, 8])

class PolarCoordinate(object):
    def __init__(self, x: int, y: int, angle: int, distance: float):
        self.x = x
        self.y = y
        self.angle = angle
        self.distance = distance
    def cartesian_x(self):
        return math.cos(self.angle) * self.distance
    def cartesian_y(self):
        return math.sin(self.angle) * self.distance
    def cartesian_coordinate(self):
        return (
            self.cartesian_x(),
            self.cartesian_y()
        )

class Star(object):
    def __init__(self, coordinate: PolarCoordinate):
        self.coordinate = coordinate
    def get_x(self):
        return self.coordinate.cartesian_x()
    def get_y(self):
        return self.coordinate.cartesian_y()
    def get_cartesian(self):
        return self.coordinate.cartesian_coordinate()
    def relative_cartesian(self): # need a name nerd!
        return (
            center_x + self.get_x(),
            center_y + self.get_y()
        )

def getGalaxy(star_count, radius):
    stars = []
    for star in range(star_count):
        distance = random.random() * radius
        angle = random.random() * 2 * math.pi
        coordinate = PolarCoordinate(
            0,
            0,
            angle,
            distance
        )
        stars.append(Star(coordinate))
    return stars

def rotate_around(coordinate, center, angleInDegrees):
    angleInRadians = angleInDegrees * (math.pi / 180)
    cosTheta = math.cos(angleInRadians)
    sinTheta = math.sin(angleInRadians)
    return (
        (cosTheta * (coordinate[0] - center[0]) -
         sinTheta * (coordinate[1] - center[1]) + center[0]),
        (sinTheta * (coordinate[0] - center[0]) +
         cosTheta * (coordinate[1] - center[1]) + center[1])
    )

def main():
    rand = random.Random()
    rand.seed(8314569173651)
    #galaxy = getGalaxy(star_count, 300)
    galaxy = Spiral(star_count, 20, 5, 0.01, rand).stars
    #for star in galaxy:
    #    print(star.coordinate.angle)
    screen = pygame.display.set_mode(size)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        screen.fill(background)
        
        txt = fonts[1].render(str(int(clock.get_fps())), 0, pygame.Color(white))
        screen.blit(txt, (0, 0))

        dist = 0.0
        
        for star in galaxy:
            # location = rotate_around(
            #     star.relative_cartesian(),
            #     center,
            #     0.2
            # )
            star.coordinate.angle += speed
            pygame.draw.circle(
                screen,
                white,
                star.coordinate.get_relative_cartesian(Cartesian(size[0]/2, size[1]/2)),
                1.0
            )
        clock.tick(60)
        pygame.display.flip()



if __name__ == "__main__":
    main()
