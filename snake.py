import pygame
import Color
import random
#assign variables
dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()




#assign colors
blue = Color.normal_blue
red = Color.red
green = Color.normal_green
black = Color.rich_black
white = Color.white
yellow = Color.yellow

# start pygame code
pygame.init()
pygame.font.init()

reg_font = pygame.font.SysFont("bahnschrift", 25)


#basics
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 30)

#foodcoords
foodx , foody = 0 , 0

def message(msg, color,x,y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [x, y])

def startsnake():
    dis.fill(black)

def genfood():
    foodx , foody = random.randrange(1,dis_width, 2), random.randrange(1, dis_height, 2)
    


def showscore():
    print("placeholder")


def updatesnake():
    print("placeholder")


def yousuck():
    dis.fill(white)
    message("You Died!" , red , 350 , 200)
    message("Press Q to play again, or press C to quit", black, 200, 250)




def loop():
    game_over = False
    game_end = False
    x1, y1 = dis_width / 5 , dis_height / 2
    Xchange, Ychange = 0 ,0
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Xchange = Xchange + 10
                    Ychange = 0
                elif event.key == pygame.K_LEFT:
                    Xchange = Xchange - 10
                    Ychange = 0
                elif event.key == pygame.K_DOWN:
                    Ychange = Ychange +10
                    Xchange = 0
                elif event.key == pygame.K_UP:
                    Ychange = Ychange - 10
                    Xchange = 0
        if Xchange >= 10:
            Xchange = 10
        elif Xchange <= -10:
            Xchange = -10
        if Ychange >= 10:
            Ychange = 10
        elif Ychange <= -10:
            Ychange = -10

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_end = True
            print("print")


        while game_end == True:
            yousuck()
            pygame.display.update()




        x1 += Xchange
        y1 += Ychange
        dis.fill(black)
        pygame.draw.rect(dis, green, [x1, y1, 20, 20])
        pygame.display.update()
        clock.tick(10)



    pygame.quit()
    quit()

loop()