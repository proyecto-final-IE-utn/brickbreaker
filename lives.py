import pygame


class Lives():

    def __init__(self, scr_heigth, scr_width, screen, lives):
        self.lives = lives
        self.screen = screen
        self.pos_x = 0.05*scr_width
        self.pos_y = 0.1*scr_heigth

    def show(self):
        text = pygame.font.Font("freesansbold.ttf", int(self.pos_y*0.5))
        gameover = text.render(str(self.lives), True, (255, 23, 20))
        self.screen.blit(gameover, (int(self.pos_x), int(self.pos_y)))

    def less1(self):
        self.lives = self.lives - 1