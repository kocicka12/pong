import sys, pygame

pygame.init()

size = width, height = 820, 840

speed = [1, 1]

black = 255, 165, 0
green = (0, 255, 0)
blue = (0, 0, 128)


screen = pygame.display.set_mode(size)


ball = pygame.image.load("intro_ball.gif")
bar = pygame.image.load("bar.gif")

ballrect = ball.get_rect()

barrect = bar.get_rect()
barrect = ballrect.move([10,0])
bar2rect = bar.get_rect()
bar2rect = bar2rect.move([width-40,0])

p1points = 0
p2points = 0

font = pygame.font.Font('freesansbold.ttf', 32)
# create a text surface object,
# on which text is drawn on it.

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_w:
                 if barrect.top > 0:
                     barrect = barrect.move([0,-50])
             if event.key == pygame.K_s:
                 if barrect.bottom<height:
                    barrect = barrect.move([0,50])
             if event.key == pygame.K_UP:
                 if bar2rect.top > 0:
                     bar2rect = bar2rect.move([0,-50])
             if event.key == pygame.K_DOWN:
                 if bar2rect.bottom<height:
                    bar2rect = bar2rect.move([0,50])


 
    if ballrect.left < 0:
         p2points  += 1
         ballrect.center = [width/2,height/2]
    if ballrect.right > width:
        p1points += 1
        ballrect.center = [width/2,height/2]
        #speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > height:

        speed[1] = -speed[1]

    ballrect = ballrect.move(speed)

    screen.fill(black)
    text = font.render("p1 %s p2 %s"%(p1points, p2points), True, green, blue)

    textRect = text.get_rect()
    textRect.center = (width // 2, 50)
    screen.blit(text, textRect)
    screen.blit(ball, ballrect)

    screen.blit(bar,barrect)
    screen.blit(bar,bar2rect)


    pygame.display.flip()




    pygame.key.key_code("return") == pygame.K_RETURN
    True
    
    pygame.key.key_code("0") == pygame.K_0
    True

    #ballrect = ballrect.move(speed)
