import pygame
from .paddle import Paddle
from .ball import Ball
from .brick import Bricks
from .button import Button
from .breaker import brick_collision, show_gameover


def brick_start():
    pygame.init()
    scr_width = 800
    scr_height = 600
    screen = pygame.display.set_mode((scr_width, scr_height))
    pygame.display.set_caption("Brick Breaker")

    # COLORS IN GAME
    bkgrd_color = (255, 255, 255)
    ball_color = (148, 0, 211)
    paddle_color = (80, 50, 30)
    brick_color = [(200, 50, 80), (230, 170, 80), (60, 230, 220), (180, 210, 80)]


    # have to initial here because there is a reference of paddle in Ball object
    paddle = Paddle(int(scr_width*0.45), screen, scr_height, scr_width, paddle_color)
    clock = pygame.time.Clock()
    while True:
        ball = Ball(int(scr_width/2), int(scr_height*0.8), paddle, ball_color, screen, scr_width)
        brick = Bricks(brick_color, scr_height, scr_width, screen, bkgrd_color)
        brick_list = brick.clone()
        brick_breaked = []
        over = False
        clicked_replay = False

        # paddle movement switches
        key_left = False
        key_right = False

        while True:

            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        key_left = True
                    if event.key == pygame.K_RIGHT:
                        key_right = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        paddle.stop()
                        key_left = False
                    if event.key == pygame.K_RIGHT:
                        paddle.stop()
                        key_right = False

            # GAME LOGIC

            # paddle movement switches
            if key_left == True:
                paddle.move_left()
            if key_right == True:
                paddle.move_right()

            # ball machanics
            ball.move()
            ball.boundries()
            ball.limit_vel()
            #  must review code in the first inquality statement 
            if paddle.paddleY + 10 > (ball.ballY + ball.ball_radius) > paddle.paddleY and ball.ballX > paddle.paddleX and ball.ballX < (paddle.paddleX + paddle.length):
                ball.collision_change()
            # brick collision
            brick_collision(brick, brick_list, brick_breaked, ball)

            # paddle boundries
            paddle.boundaries()
            if ball.ballY > scr_height:
                show_gameover(screen)
                over = True
                # REPLAY BUTTON
                b = Button(screen, (80, 45, 200), (200, 250, 255),
                        (260, 350), (150, 60), "REPLAY", 30)
                state = 'original'
                while True:
                    b.show()
                    for event in pygame.event.get():
                        if b.isOverMouse() == True:
                            if event.type == pygame.MOUSEBUTTONUP:
                                clicked_replay = True
                            state = 'changed'
                        elif b.isOverMouse() == False:
                            state = 'original'
                        if event.type == pygame.QUIT:
                            pygame.quit()
                    if state == 'changed':
                        b.changeColor((80, 240, 80), (14, 37, 100))
                    if clicked_replay == True:
                        break
                    pygame.display.update()

            # DISPLAY THINGS

            screen.fill(bkgrd_color)
            paddle.show()
            brick.show()
            for brk in brick_breaked:
                brick.update(brk)
            # brick_collision(brick, brick_list, ball)
            ball.show()
            if over == True:
                break
            pygame.display.update()


if __name__ == "__main__":
    brick_start()
