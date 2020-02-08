import pygame

imagepath = 'game/images/queen.png'    
def init(n_board, size, seq=[6, 3, 7, 2, 4, 8, 1, 5], boardLength = 8, fitness=[]):    
    pygame.init()
    # pygame.font.init()

    #set color with rgb
    white,black,red = (255,255,255),(0,0,0),(255,0,0)

    #set display
    gameDisplay = pygame.display.set_mode((1080, 1080), pygame.RESIZABLE)
    # font = pygame.font.Font('/System/Library/Fonts/Keyboard.ttf', 30)
    font = pygame.font.Font('game/Keyboard.ttf', 30)

    # myfont = pygame.font.SysFont('Caveat', 30)

    #caption
    pygame.display.set_caption("ChessBoard")

    #beginning of logic
    gameExit = False

    lead_x = 20
    lead_y = 20

    frame = len(seq) - 1
    step = max(1, int(len(seq) / 10.))
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    frame = (frame - step) % len(seq)
                if event.key == pygame.K_RIGHT:
                    frame = (frame + step) % len(seq)
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
                    pygame.quit()

            gameDisplay.fill(white)

            queenimage = pygame.image.load(imagepath)
            queenimage = pygame.transform.scale(queenimage, (size, size))
            xp = 0
            xy = -1
            for j in range(n_board):
                cnt = 0
                if xp % 6 == 0:
                    xy += 1
                    xp = 0
                for i in range(1,boardLength+1):
                    for z in range(1,boardLength+1):         
                        #check if current loop value is even
                        if cnt % 2 == 0:
                            pygame.draw.rect(gameDisplay, black,[size*z+(xp*(size*boardLength+50)),size*i+(xy*(size*boardLength+50)),size,size])
                        else:
                            pygame.draw.rect(gameDisplay, red, [size*z+(xp*(size*boardLength+50)),size*i+(xy*(size*boardLength+50)),size,size])
                        cnt +=1
                        if seq[frame][z-1] == i:
                            gameDisplay.blit(queenimage, [size*z+(xp*(size*boardLength+50)),size*i+(xy*(size*boardLength+50)), 10, 10])
                    #since theres an even number of squares go back one value
                    if boardLength % 2 == 0:
                        cnt-=1
                    #Add a nice boarder
                    pygame.draw.rect(gameDisplay,black,[size*z+(xp*(size*boardLength+50)),size*i+(xy*(size*boardLength+50)),size,size],3)
                xp += 1
            
            # pygame.display.set_caption("frame={}".format{frame})
            text = font.render('Iteration    {}'.format(frame), True, (0, 0, 0))
            gameDisplay.blit(text, (250, 800))
            text = font.render('Best Fitness     {}'.format(fitness[frame]), True, (0, 0, 0))
            gameDisplay.blit(text, (250, 900))
            # textsurface = myfont.render('Some Text', False, (0, 0, 0))
            # screen.blit(textsurface,(500,500))

            pygame.display.update()
            # white, black = black, white