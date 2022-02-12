import sys, pygame

pygame.init()


size = width, height = 820, 840

speed = [5, 5]

black = 255, 165, 0


screen = pygame.display.set_mode(size)


ball = pygame.image.load("intro_ball.gif")
bar = pygame.image.load("bar.gif")

ballrect = ball.get_rect()

barrect = bar.get_rect()

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_w:
                barrect = barrect.move([0,50])
             if event.key == pygame.K_s:
                barrect = barrect.move([0,-50])
    if ballrect.left < 0 or ballrect.right > width:

        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > height:

        speed[1] = -speed[1]

    ballrect = ballrect.move(speed)

    screen.fill(black)

    screen.blit(ball, ballrect)

    screen.blit(bar,barrect)


    pygame.display.flip()

    pygame.key.key_code("return") == pygame.K_RETURN
    True
    
    pygame.key.key_code("0") == pygame.K_0
    True

    #ballrect = ballrect.move(speed)
