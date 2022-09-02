import pygame


def brick_collision(brick, brick_list, brick_breaked, ball):
    for item in brick_list:
        x = item[0]
        y = item[1]
        index = brick_list.index(item)
        if x < ball.ballX and ball.ballX < (x + brick.length) and (ball.ballY + ball.ball_radius) > y and ball.ballY < y:
            ball.y_vel = -ball.y_vel
            brick_breaked.append(item)
            brick_list.pop(index)
        elif y < ball.ballY and ball.ballY < (y + brick.width) and (ball.ballX + ball.ball_radius) > x and ball.ballX < x:
            ball.x_vel = -ball.x_vel
            brick_breaked.append(item)
            brick_list.pop(index)
        elif y < ball.ballY and ball.ballY < (y + brick.width) and (ball.ballX - ball.ball_radius) < (x + brick.length) and ball.ballX > (x + brick.length):
            ball.x_vel = -ball.x_vel
            brick_breaked.append(item)
            brick_list.pop(index)
        elif x < ball.ballX and ball.ballX < (x + brick.length) and (ball.ballY - ball.ball_radius) < (y + brick.width) and ball.ballY > (y + brick.width):
            ball.y_vel = -ball.y_vel
            brick_breaked.append(item)
            brick_list.pop(index)


def show_gameover(screen):
    global scr_height
    global scr_width
    text = pygame.font.Font("freesansbold.ttf", int(scr_height*0.1))
    gameover = text.render("GAME OVER", True, (255, 23, 20))
    screen.blit(gameover, (int(scr_width*0.25), int(scr_height*0.4)))
