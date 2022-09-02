import pygame

class Ball():

    global screen
    global ball_color
    global paddle

    def __init__(self, ballX, ballY, paddle, ball_color, screen, scr_width):
        self.ballX = ballX
        self.ballY = ballY
        self.paddle = paddle
        self.ball_color = ball_color
        self.screen = screen
        self.scr_width = scr_width
        self.x_vel = 8
        self.y_vel = -8
        self.ball_radius = 10
        self.max_x_vel = 10

    def show(self):

        pygame.draw.circle(self.screen, self.ball_color,
                           (self.ballX, self.ballY), self.ball_radius)

    def move(self):

        self.ballX += self.x_vel
        self.ballY += self.y_vel

    def collision_change(self):

        center = self.paddle.paddleX + self.paddle.length//2
        left_end = self.paddle.paddleX
        right_end = self.paddle.paddleX + self.paddle.length
        self.y_vel = -self.y_vel
        if left_end < self.ballX < center:
            ratio = (center - self.ballX)//(self.paddle.length//2)
            self.x_vel += -self.max_x_vel * ratio
        elif center < self.ballX < right_end:
            ratio = (self.ballX - center)//(self.paddle.length//2)
            self.x_vel += self.max_x_vel * ratio

    def boundries(self):

        if self.ballY <= (0 + self.ball_radius):
            self.y_vel = -self.y_vel
        if self.ballX <= (0 + self.ball_radius):
            self.x_vel = -self.x_vel
        if self.ballX >= (self.scr_width - self.ball_radius):
            self.x_vel = -self.x_vel

    def limit_vel(self):

        if -self.max_x_vel > self.x_vel:
            self.x_vel = -self.max_x_vel
        elif self.x_vel > self.max_x_vel:
            self.x_vel = self.max_x_vel

