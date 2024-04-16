import pygame
import math
import random
from pygame import mixer
#Intialize the pygame
pygame.init()
# create the screen
screen= pygame.display.set_mode((1000, 800))
# Adjusting the FPS of the game
clock = pygame.time.Clock()
FPS =120
#Background
background = pygame.image.load("IBlogo_DP_adobespark.png")
pygame.display.set_caption("International Baccalaureate")
#caption and icon
icon = pygame.image.load("IB2.png")
pygame.display.set_icon(icon)
#IB logo
PlayerImg = pygame.image.load("IB2.png")

#background sound
mixer.music.load("game continue.wav")
mixer.music.play(-1)
playerX = 400
playerY = 700
playerX_change = 0
# objects
enemyImg = pygame.image.load("TOK2.png")
enemyX = 500
enemyY = -800
enemyX_change = 0
enemyY_change = 2.5

BMIMG = pygame.image.load("BM_adobespark.png")
BMX = 200
BMY = -400
BMX_change = 0
BMY_change = 2.5

EEImg = pygame.image.load("EE.png")
EEX = 100
EEY = -300
EEX_change = 0
EEY_change = 2.5

CASImg = pygame.image.load("CAS.png")
CASX = 600
CASY = 200
CASX_change = 0
CASY_change = 2.5

CSImg = pygame.image.load("CS1_adobespark.png")
CSX = 200
CSY = -100
CSX_change = 0
CSY_change = 2.5

IAImg = pygame.image.load("IA.png")
IAX = 300
IAY = 0
IAX_change = 0
IAY_change = 2.5

mathsImg = pygame.image.load("maths.png")
mathsX = 800
mathsY = -600
mathsX_change = 0
mathsY_change = 2.5
#score
score_number =42
font = pygame.font.Font("Hello Avocado.ttf",28)
textX=10
textY=10

#diploma not awarded text
def game_over_text():
    over_font = pygame.font.Font("orange juice 2.0.ttf", 64)
    over_text = over_font.render("score "+str(score_number) +" DIPLOMA NOT AWARDED",True,(0,0,0))
    screen.blit(over_text, (100,400))

#diploma awarded text
def END():
    end_font = pygame.font.Font("sportsfonts - Winner Cond Regular.otf", 64)
    end_text = end_font.render("Diploma awarded  you scored "+ str(score_number), True,(0,0,0))
    screen.blit(end_text,(100,400))
#score
def show_score(x,y):

    score = font.render("IB SCORE :"+ str(score_number), True,(169,169,169))
    screen.blit(score,(x,y))
#full iB grades achieved
def win_ner_text  ():
    winnter_font =pygame.font.Font("orange juice 2.0.ttf", 60)
    winner_text=winnter_font.render("You scored full points Diploma awarded", True, (0,0,0))
    screen.blit(winner_text,(10,400))
def player(x, y):
    screen.blit(PlayerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def BM(x, y):
    screen.blit(BMIMG, (x,y))


def maths(x, y):
    screen.blit(mathsImg, (x, y))


def CAS(x, y):
    screen.blit(CASImg, (x, y))


def EE(x, y):
    screen.blit(EEImg, (x, y))


def IA(x, y):
    screen.blit(IAImg, (x, y))


def CS(x, y):
    screen.blit(CSImg, (x, y))


def Collision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt(math.pow(enemyX - playerX, 2) + math.pow(enemyY - playerY, 2))
    if distance < 27:
        return True
    else:
        return False
def Fight (EEX , EEy , playerX ,playerY):
    length = math.sqrt(math.pow(EEX - playerX,2)+math.pow(EEY -playerY,2))
    if length <27:
        return True
    else:
        return False

def Activity (CASX ,CASY ,playerX ,playerY):
    Service = math.sqrt(math.pow(CASX-playerX,2)+math.pow(CASY -playerY,2))
    if Service <27:
        return True
    else:
        return False

def Equation (mathsX ,mathsY , playerX , playerY):
    indices = math.sqrt(math.pow(mathsX - playerX, 2) + math.pow(mathsY - playerY, 2))
    if indices <27:
        return True
    else:
        return False
def Internal (IAX , IAY ,playerX , playerY):
    Assesment= math.sqrt(math.pow(IAX - playerX, 2) + math.pow(IAY - playerY, 2))
    if Assesment <27:
        return True
    else:
        return False
def Computer (CSX ,CSY , playerX , playerY):
    Science = math.sqrt(math.pow(CSX - playerX, 2) + math.pow(CSY - playerY, 2))
    if Science <27:
        return True
    else:
        return False

def Profit (BMX , BMY , playerX ,playerY):
    Loss = math.sqrt(math.pow(BMX - playerX, 2) + math.pow(BMY - playerY, 2))
    if Loss <27:
        return True
    else:
        return False
# game Loop
running = True

while running:
    clock.tick(FPS)

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -20

            if event.key == pygame.K_RIGHT:
                playerX_change = 20

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0



    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 900:
        playerX = 900
#responing the object to different place
    if BMY >=800 and score_number <=23:

        IAY=-1000
        EEY =-1000
        CASY =-1000
        mathsY =-1000
        enemyY =-1000
        CSY =-1000

        game_over_text()


    if BMY >= 800 and score_number >=24:

        IAY = -1000
        EEY = -1000
        CASY = -1000
        mathsY = -1000
        enemyY = -1000
        CSY = -1000

        END()

    if CASY >=800 and score_number <=23:


        IAY=-1000
        EEY =-1000
        BMY =-1000
        mathsY =-1000
        enemyY =-1000
        CSY =-1000


        game_over_text()

    if CASY >=800 and score_number >=24:

        IAY=-1000
        EEY =-1000
        BMY =-1000

        mathsY =-1000
        enemyY =-1000
        CSY =-1000


        END()





    if EEY >=800 and score_number <=23:

        IAY=-1000

        BMY =-1000
        CASY =-1000
        mathsY =-1000
        enemyY =-1000
        CSY =-1000

        game_over_text()

    if EEY >=800 and score_number >=24:

        IAY=-1000

        BMY =-1000
        CASY =-1000
        mathsY =-1000
        enemyY =-1000
        CSY =-1000

        END()



    if CSY >=800 and score_number <=23:


        EEY =-1000
        BMY =-1000
        CASY =-1000
        mathsY =-1000
        enemyY =-1000
        IAY =-1000


        game_over_text()

    if CSY >=800 and score_number >=24:

        EEY =-1000
        BMY =-1000
        CASY =-1000
        mathsY =-1000
        enemyY =-1000

        IAY =-1000

        END()

    if mathsY >=800 and score_number <=23:

        IAY=-1000
        EEY =-1000
        BMY =-1000
        CASY =-1000

        enemyY =-1000
        CSY =-1000
        game_over_text()

    if mathsY >= 800 and score_number >= 24:
        IAY = -1000
        EEY = -1000
        BMY = -1000
        IASY = -1000

        enemyY = -1000
        CSY = -1000
        CASY =-1000

        END()

    if IAY >=800 and score_number <=23:


        EEY =-1000
        BMY =-1000
        CASY =-1000
        mathsY =-1000
        enemyY =-1000
        CSY =-1000
        game_over_text()

    if IAY >=800 and score_number >=24:

        EEY =-1000
        BMY =-1000
        CASY =-1000
        mathsY =-1000
        enemyY =-1000
        CSY =-1000
        END()

    if enemyY >=800 and score_number <=23:

        IAY=-1000
        EEY =-1000
        BMY =-1000
        CASY =-1000
        mathsY =-1000

        CSY =-1000
        game_over_text()

    if enemyY >=800 and score_number >=24:
        IAY=-1000
        EEY =-1000
        BMY =-1000
        CASY =-1000
        mathsY =-1000
        
        CSY =-1000
        END()



    enemyY += enemyY_change
    if enemyX <= 0:
        enemyX_change = 4

    elif enemyX >= 1000:
        enemyX_change = -4
        enemyX += enemyX_change


    CASY += CASY_change
    if CASX <= 0:
        CASX_change = 4
        CASX += CASX_change
    elif CASX >= 1000:
        CASX_change = -4
        CASX += CASX_change

    EEY += EEY_change
    if EEX <= 0:
        EEX_change = 4
        EEX += enemyX_change
    elif EEX >= 1000:
        EEX_change = -4
        EEX += EEX_change

    IAY += IAY_change
    if IAX <= 0:
        IAX_change = 4
        IAX += IAX_change
    elif IAX >= 1000:
        IAX_change = -4
        IAX += IAX_change

    CSY += CSY_change
    if CSX <= 0:
        CSX_change = 4
        CSX += CSX_change
    elif CSX >= 1000:
        CSX_change = -4
        CSX += CSX_change

    mathsY += mathsY_change
    if mathsX <= 0:
        mathsX_change = 4
        mathsX += mathsX_change
    elif mathsX >= 1000:
        mathsX_change = -4
        mathsX += mathsX_change

    BMY += BMY_change
    if BMX <= 0:
        BMX_change = 4
        BMX += BMX_change
    elif BMX >= 1000:
        BMX_change = -4
        BMX += BMX_change



    if score_number >=45:
        Score_wav = mixer.Sound("pass.wav")
        Score_wav.play()

        IAY=-1000
        EEY =-1000
        BMY =-1000
        CASY =-1000
        mathsY =-1000
        enemyY =-1000
        CSY =-1000



        win_ner_text()


    collision = Collision(enemyX,enemyY,playerX,playerY)
    if collision:
        Score_wav = mixer.Sound("score.wav")
        Score_wav.play()
        score_number +=1

        enemyX = random.randint(0,900)
        enemyY = (-800)

    fight = Fight(EEX,EEY,playerX,playerY)
    if fight:
        Score_wav = mixer.Sound("score.wav")
        Score_wav.play()
        score_number +=1
        score_number +=1

        EEX=  random.randint(0,900)
        EEY= (-400)
    activity =Activity(CASX ,CASY , playerX,playerY)
    if activity:
        Score_wav = mixer.Sound("score.wav")
        Score_wav.play()
        score_number +=1

        CASX =random.randint(0,900)
        CASY= -50

    equation = Equation(mathsX , mathsY , playerX , playerY)
    if equation:
        Score_wav = mixer.Sound("score.wav")
        Score_wav.play()
        score_number +=2

        mathsX=random.randint(0,900)
        mathsY= -200

    internal = Internal(IAX , IAY , playerX , playerY)
    if internal:
        Score_wav = mixer.Sound("score.wav")
        Score_wav.play()
        score_number +=1

        IAX=random.randint(0,900)
        IAY= -100

    computer = Computer(CSX , CSY , playerX , playerY)
    if computer:
        Score_wav = mixer.Sound("score.wav")
        Score_wav.play()
        score_number +=2

        CSX=random.randint(0,900)
        CSY= -500

    profit = Profit(BMX , BMY , playerX , playerY)
    if profit:
        Score_wav = mixer.Sound("score.wav")
        Score_wav.play()
        score_number +=2

        BMX=random.randint(0,800)
        BMY= -700

    BM(BMX, BMY)
    CS(CSX, CSY)
    maths(mathsX, mathsY)
    IA(IAX, IAY)
    CAS(CASX, CASY)
    EE(EEX, EEY)
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_score(textX, textY)
    pygame.display.update()



    clock.tick(120)
