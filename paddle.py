import pygame


class Paddle():
    def __init__(self, paddleX, screen, scr_height, scr_width, paddle_color):
        self.screen = screen
        self.scr_height = scr_height
        self.scr_width = scr_width
        self.paddle_color = paddle_color
        self.paddleX = paddleX
        self.paddleY = int(scr_height*0.95)
        self.length = 200

    def show(self):
        thickness = 10
        pygame.draw.rect(self.screen, self.paddle_color, ((
            self.paddleX, self.paddleY), (self.length, thickness)))

    def move_left(self):
        self.velocity = 15
        self.paddleX += -self.velocity

    def move_right(self):
        self.velocity = 15
        self.paddleX += self.velocity

    def stop(self):
        self.velocity = 0

    def boundaries(self):
        if self.paddleX >= (self.scr_width - self.length):
            self.paddleX = self.scr_width - self.length
        elif self.paddleX <= 0:
            self.paddleX = 0
