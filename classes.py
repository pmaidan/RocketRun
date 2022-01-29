import pygame as pg
from settings import *
from random import randrange


class Stars:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.img = STAR_IMGS[randrange(4)]
        self.w = self.img.get_width()
        self.h = self.img.get_height()

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))

    def update(self):
        self.y += 2


class Rocket:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.w = pg.image.load("rocketFireMiddle.png").get_width()
        self.h = pg.image.load("rocketFireMiddle.png").get_height()
        self.state = "Idle"
        self.AnimIdx = 0
        self.rocketCounter = 0

        self.AnimMiddle = []
        self.AnimMiddle.append(pg.image.load("rocketFireMiddle.png"))
        self.AnimMiddle.append(pg.image.load("rocketFireRight.png"))
        self.AnimMiddle.append(pg.image.load("rocketFireMiddle.png"))
        self.AnimMiddle.append(pg.image.load("rocketFireLeft.png"))

        self.AnimToRight = []
        self.AnimToRight.append(pg.image.load("rocketFireLeft.png"))
        self.AnimToRight.append(pg.image.load("rocketFireFlyRight.png"))

        self.AnimToLeft = []
        self.AnimToLeft.append(pg.image.load("rocketFireRight.png"))
        self.AnimToLeft.append(pg.image.load("rocketFireFlyLeft.png"))

    def update(self):
        if self.rocketCounter == 10:
            self.AnimIdx += 1
        if self.rocketCounter > 10:
            self.rocketCounter = 0
        self.rocketCounter += 1

    def animation(self):
        if self.state == "Idle":
            if self.AnimIdx > 3:
                self.AnimIdx = 0
            self.screen.blit(self.AnimMiddle[self.AnimIdx], (self.x, self.y))
        if self.state == "ToRight":
            if self.AnimIdx > 1:
                self.AnimIdx = 0
            self.screen.blit(self.AnimToRight[self.AnimIdx], (self.x, self.y))
        if self.state == "ToLeft":
            if self.AnimIdx > 1:
                self.AnimIdx = 0
            self.screen.blit(self.AnimToLeft[self.AnimIdx], (self.x, self.y))

   # def collision(self, star):
      #  if star.x > self.x and star.x < self.x + self.w and star.y > self.y and star.y < self.y + self.h or
        #    star.x + star.w > self.x and star.x + star.w < self.x + self.w
