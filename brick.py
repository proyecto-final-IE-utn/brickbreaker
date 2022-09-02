import pygame
import random


class Bricks():
    def __init__(self, brick_color, scr_heigth, scr_width, screen, bkgrd_color):
        self.rows = 4
        self.rows_bricks = 5
        self.screen = screen
        self.scr_width = scr_width
        self.scr_heigth = scr_heigth
        self.bkgrd_color = bkgrd_color
        self.brick_color = brick_color
        self.length = int(self.scr_width*0.8)//self.rows_bricks
        self.width = 40
        self.spacing = 4
        self.coordinates = []
        self.random_color = []
        for i in range(10, self.rows*(self.width), self.width):
            for j in range(int(self.scr_width*0.1), int(self.scr_width*0.9 - self.length)+1, self.length):
                self.coordinates.append([j, i])
                self.random_color.append(random.choice(self.brick_color))

    def show(self):
        num = 1
        color_index = 1
        for item in self.coordinates:
            pygame.draw.rect(self.screen, self.brick_color[color_index-1], ((
                item[0], item[1]), (self.length-self.spacing, self.width-self.spacing)))
            num += 1
            if num > color_index * self.rows_bricks:
                color_index += 1

    def clone(self):
        brick_list = []
        for item in self.coordinates:
            brick_list.append(item)
        return brick_list

    def update(self, cordinate):
        pygame.draw.rect(self.screen, self.bkgrd_color, (cordinate,
                                               (self.length-self.spacing, self.width-self.spacing)))
