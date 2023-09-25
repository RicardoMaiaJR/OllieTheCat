import pygame
import os
import sys
import random
import math

pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.font.init()
pygame.mixer.init()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First game")

WHITE = (255,255,190)
FPS = 60

#GAME
IN_MENU = True
IN_GAME = False
IN_ENDGAME =False

#MUSIC AND SOUNDS
IN_MENU_MUSIC = pygame.mixer.Sound("assets/menulegal.mp3")
IN_GAME_MUSIC = pygame.mixer.Sound("assets/running.mp3")
PLAYER_HIT = pygame.mixer.Sound("assets/Porrada_1.mp3")
OBSTACLE_HIT = pygame.mixer.Sound("assets/Porrada_2.mp3")
GAME_OVER_HIT = pygame.mixer.Sound("assets/Perdeu.mp3")
GAME_OVER_MUSIC = pygame.mixer.Sound("assets/Morreu.mp3")

IN_MENU_MUSIC.play(-1)

#Background
BACKGROUND_SPEED = 5
BACKGROUND_IMAGES = ['rua1.png','rua2.png','rua3.png','rua4.png','rua5.png','rua6.png','rua7.png']  
BACKGROUND_INDEX = [4,6,1]
BACKGROUND_WIDTH, BACKGROUND_HEIGHT = 900, 250
#Background tile 0
BACKGROUND_POSITION0 = [0,-250]
BACKGROUND0 = pygame.image.load(os.path.join('assets/'+BACKGROUND_IMAGES[BACKGROUND_INDEX[0]]))
BACKGROUND0 = pygame.transform.scale(BACKGROUND0, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
#Background tile 2
BACKGROUND_POSITION1 = [0,0]
BACKGROUND1 = pygame.image.load(os.path.join('assets/'+BACKGROUND_IMAGES[BACKGROUND_INDEX[1]]))
BACKGROUND1 = pygame.transform.scale(BACKGROUND1, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
#Background tile 3
BACKGROUND_POSITION2 = [0,250]
BACKGROUND2 = pygame.image.load(os.path.join('assets/'+BACKGROUND_IMAGES[BACKGROUND_INDEX[2]]))
BACKGROUND2 = pygame.transform.scale(BACKGROUND2, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
#Menu Background
MENU_IMAGE = pygame.image.load(os.path.join('assets/menu.png'))
MENU_BACKGROUND = pygame.transform.scale(MENU_IMAGE, (WIDTH, HEIGHT))
#play button
PLAY_BUTTON_IMAGE = pygame.image.load(os.path.join('assets/jogar.png'))
PLAY_BUTTON_POSITION = [386,165]
PLAY_BUTTON_SIZE = [416,109]
#options button
OPTIONS_BUTTON_IMAGE = pygame.image.load(os.path.join('assets/opcoes.png'))
OPTIONS_BUTTON_POSITION = [722, 377]
OPTIONS_BUTTON_SIZE = [172,82]
SOM_BUTTON_IMAGES = ["check.png", "nocheck.png"]
SOM_BUTTON_INDEX = 1
SOM_BUTTON_SIZE = [48*2,48*2]
SOM_BUTTON_IMAGE = pygame.image.load(os.path.join('assets/'+SOM_BUTTON_IMAGES[SOM_BUTTON_INDEX]))
SOM_BUTTON = pygame.transform.scale(SOM_BUTTON_IMAGE, SOM_BUTTON_SIZE)
SOM_BUTTON_POSITION = [290, 40]
FX_BUTTON_IMAGES = ["check.png", "nocheck.png"]
FX_BUTTON_INDEX = 1
FX_BUTTON_SIZE = [48*2,48*2]
FX_BUTTON_IMAGE = pygame.image.load(os.path.join('assets/'+FX_BUTTON_IMAGES[FX_BUTTON_INDEX]))
FX_BUTTON = pygame.transform.scale(FX_BUTTON_IMAGE, FX_BUTTON_SIZE)
FX_BUTTON_POSITION = [290, 214]
#Options Screen
OPTIONS_SCREEN_IMAGE = pygame.image.load(os.path.join('assets/opts.png'))
OPTIONS_SCREEN = pygame.transform.scale(OPTIONS_SCREEN_IMAGE, (WIDTH, HEIGHT))
#Game Over Screen
GAME_OVER_BACKGROUND_IMAGE = pygame.image.load(os.path.join('assets/morreu.png'))
GAME_OVER = pygame.transform.scale(GAME_OVER_BACKGROUND_IMAGE, (WIDTH, HEIGHT))

#PLAYER
GATO_SPEED = 8
GATO_WIDTH, GATO_HEIGHT = 24, 44
GATO_POSITION = [400,350]
GATO_SKIN = ["gato.png", "banin.png", "catdir.png", "catdirs.png"]
GATO_SKIN_INDEX = 2
GATO_IMAGE = pygame.image.load(os.path.join("assets/", GATO_SKIN[GATO_SKIN_INDEX]))
GATO = pygame.transform.scale(GATO_IMAGE, (GATO_WIDTH+30, GATO_HEIGHT+30))
GATO = pygame.transform.flip(GATO_IMAGE, True, False)
points = 0
bg_points = 0
#Player Life
PLAYER_LIFE_IMAGE_SIZE = [59*3, 12*3]
PLAYER_LIFE_IMAGES = ["vidas.png","vidas2.png","vidas3.png"]
life = 0
PLAYER_LIFE_GUI = pygame.image.load(os.path.join("assets/",PLAYER_LIFE_IMAGES[life]))
PLAYER_LIFE = pygame.transform.scale(PLAYER_LIFE_GUI, (PLAYER_LIFE_IMAGE_SIZE[0], PLAYER_LIFE_IMAGE_SIZE[1]))


#ENEMY
DificultValue = 10
ENEMY_SPEED = 5
ENEMY_WIDTH, ENEMY_HEIGHT = [20, 29, 24, 18, 20],[19, 42, 24, 19, 20]
ENEMY_IMAGE_WIDTH, ENEMY_IMAGE_HEIGHT = [20*3, 29*3, 24*3, 18*3, 20*3, 20*3, 20*3, 20*3, 60*3],[19*3, 42*2, 24*3, 19*3, 20*3, 20*3, 20*3, 20*3, 80*3]
ENEMY_POSITION = [[0, 600], [0,600], [0,600], [0,600], [0,600]]
ENEMY_IMAGES = ["bosta.png", "belinha.png", "caixa.png", "cone.png", "lata1.png", "lata2.png", "lata3.png", "lata4.png", "policia.png"]
ENEMY_IMAGE_INDEX = [0,1,2,3,4]
ENEMY_IMAGE = [pygame.image.load(os.path.join("assets/"+ENEMY_IMAGES[ENEMY_IMAGE_INDEX[0]])),
               pygame.image.load(os.path.join("assets/"+ENEMY_IMAGES[ENEMY_IMAGE_INDEX[1]])),
               pygame.image.load(os.path.join("assets/"+ENEMY_IMAGES[ENEMY_IMAGE_INDEX[2]])),
               pygame.image.load(os.path.join("assets/"+ENEMY_IMAGES[ENEMY_IMAGE_INDEX[3]])),
               pygame.image.load(os.path.join("assets/"+ENEMY_IMAGES[ENEMY_IMAGE_INDEX[4]]))]
ENEMY = [pygame.transform.scale(ENEMY_IMAGE[0], (ENEMY_WIDTH[0], ENEMY_HEIGHT[0])),
         pygame.transform.scale(ENEMY_IMAGE[1], (ENEMY_WIDTH[1], ENEMY_HEIGHT[1])),
         pygame.transform.scale(ENEMY_IMAGE[2], (ENEMY_WIDTH[2], ENEMY_HEIGHT[2])),
         pygame.transform.scale(ENEMY_IMAGE[3], (ENEMY_WIDTH[3], ENEMY_HEIGHT[3])),
         pygame.transform.scale(ENEMY_IMAGE[4], (ENEMY_WIDTH[4], ENEMY_HEIGHT[4]))]
ENEMY_DEAD = [False, False, False, False, False]

#SHOOT
MOUSE_X, MOUSE_Y = 0 , 0
SHOOT_SPEED = 20
SHOOT_WIDTH, SHOOT_HEIGHT = 25,25
SHOOT_POSITION = [-500,-500]
SHOOT_IMAGE = pygame.image.load(os.path.join("assets", "proj.png"))
SHOOT = pygame.transform.scale(SHOOT_IMAGE, (SHOOT_WIDTH, SHOOT_HEIGHT))
SHOOT_ACTIVE = False
CAN_SHOOT = True
shoot_timer = 5
shoot_time = 5
shoot_flag = False
#SHOOT GUI
SHOOT_GUI_WIDTH, SHOOT_GUI_HEIGHT = 50,70
SHOOT_GUI_IMAGES = ["proj.png", "noproj.png"]
Shoot_Index = 0
SHOOT_GUI_IMAGE = pygame.image.load(os.path.join("Assets/"+SHOOT_GUI_IMAGES[Shoot_Index]))
SHOOT_GUI = pygame.transform.scale(SHOOT_IMAGE, (SHOOT_WIDTH, SHOOT_HEIGHT))

font_path = "assets/VCR_OSD_MONO_1.001.ttf"
text_font = pygame.font.Font(font_path, 60)
minor_text_font = pygame.font.Font(font_path, 30)


####################### IN GAME FUNCTIONS ##########################

baninPoints = 0
def EASTER_EGG():
    global baninPoints, BACKGROUND_IMAGES, GATO_SKIN_INDEX, GATO_IMAGE, GATO
    keys = pygame.key.get_pressed()
    if keys[pygame.K_b]:
        baninPoints = 1
    if keys[pygame.K_a] and baninPoints == 1:
        baninPoints = 2
    if keys[pygame.K_n] and (baninPoints == 2 or baninPoints == 4):
        baninPoints += 1
    if keys[pygame.K_i] and baninPoints == 3:
        baninPoints = 4
    if baninPoints == 5:
        BACKGROUND_IMAGES = ['chupetao.jpg','damn.jpg','deep.jpg','rock.jpg','gato2.jpg','tosilly.jpg','dora.jpg']  
        GATO_SKIN_INDEX = 1
        GATO_IMAGE = pygame.image.load(os.path.join("assets/", GATO_SKIN[GATO_SKIN_INDEX]))
        GATO = pygame.transform.scale(GATO_IMAGE, (GATO_WIDTH+30, GATO_HEIGHT+30))
        if keys[pygame.K_BACKSPACE]:
            baninPoints = 0
    if baninPoints == 0:
        BACKGROUND_IMAGES = ['rua1.png','rua2.png','rua3.png','rua4.png','rua5.png','rua6.png','rua7.png']    
        GATO_SKIN_INDEX = 2
        GATO_IMAGE = pygame.image.load(os.path.join("assets/", GATO_SKIN[GATO_SKIN_INDEX]))
        GATO = pygame.transform.scale(GATO_IMAGE, (GATO_WIDTH+30, GATO_HEIGHT+30))

def Timer():
    global CAN_SHOOT, shoot_timer, shoot_flag, Shoot_Index
    CAN_SHOOT = False
    shoot_timer -= 1 / 60
    Shoot_Index = 1
    if shoot_timer < 1:
        CAN_SHOOT = True
        shoot_timer = shoot_time
        shoot_flag = False
        Shoot_Index = 0

def shoot():
    global MOUSE_X, MOUSE_Y, SHOOT_POSITION, SHOOT_ACTIVE
    global GATO_POSITION
    angle = math.atan2((int(GATO_POSITION[1]+(GATO_HEIGHT/2)))-MOUSE_Y, (int(GATO_POSITION[0]+(GATO_WIDTH/2)))-MOUSE_X)
    dx = math.cos(angle)*SHOOT_SPEED
    dy = math.sin(angle)*SHOOT_SPEED
    SHOOT_POSITION[0] = SHOOT_POSITION[0] - int(dx)
    SHOOT_POSITION[1] = SHOOT_POSITION[1] - int(dy)
    

def DificultGenerator():
    global ENEMY_POSITION
    global DificultValue
    for i in range(len(ENEMY)-1):
        if points < 12 * (i+1):
            ENEMY_POSITION[i+1][1] = 600

def Obstacle():
    global ENEMY_POSITION, ENEMY_DEAD
    ##respawn
    for i in range(len(ENEMY)):
        if ENEMY_POSITION[i][1] == 600:
            ENEMY_POSITION[i][0] = Spawn()[0]
            ENEMY_POSITION[i][1] = Spawn()[1]
            ENEMY_IMAGE_INDEX[i] = Spawn()[2]
            ENEMY_IMAGE[i] = pygame.image.load('assets/'+ENEMY_IMAGES[ENEMY_IMAGE_INDEX[i]])
            ENEMY_WIDTH[i] = ENEMY_IMAGE_WIDTH[ENEMY_IMAGE_INDEX[i]]
            ENEMY_HEIGHT[i] = ENEMY_IMAGE_HEIGHT[ENEMY_IMAGE_INDEX[i]]
            ENEMY[i] = pygame.transform.scale(ENEMY_IMAGE[i], (ENEMY_WIDTH[i], ENEMY_HEIGHT[i]))
            ENEMY_DEAD[i] = False
        else:
            ENEMY_POSITION[i][1] += ENEMY_SPEED

def Spawn():
    X = random.randint(150, 650)
    Y = -100
    index = random.randint(0, len(ENEMY_IMAGES)-1)
    return[X , Y, index]

RandBG = random.sample(range(len(BACKGROUND_IMAGES)), len(BACKGROUND_IMAGES))
def background():
    global BACKGROUND_INDEX, BACKGROUND0,BACKGROUND1,BACKGROUND2,BACKGROUND_SPEED, points, bg_points, RandBG
    BACKGROUND_POSITION0[1] += BACKGROUND_SPEED
    BACKGROUND_POSITION1[1] += BACKGROUND_SPEED
    BACKGROUND_POSITION2[1] += BACKGROUND_SPEED
    if BACKGROUND_POSITION0[1] >= HEIGHT:
        BACKGROUND_POSITION0[1] = -250
        BACKGROUND_INDEX[0] = RandBG[bg_points]
        BACKGROUND0 = pygame.image.load('assets/'+BACKGROUND_IMAGES[BACKGROUND_INDEX[0]])
        BACKGROUND0 = pygame.transform.scale(BACKGROUND0, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
        points += 1
        bg_points += 1
    if BACKGROUND_POSITION1[1] >= HEIGHT:
        BACKGROUND_POSITION1[1] = -250
        BACKGROUND_INDEX[1] = RandBG[bg_points]
        BACKGROUND1 = pygame.image.load('assets/'+BACKGROUND_IMAGES[BACKGROUND_INDEX[1]])
        BACKGROUND1 = pygame.transform.scale(BACKGROUND1, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
        points += 1
        bg_points += 1
    if BACKGROUND_POSITION2[1] >= HEIGHT:
        BACKGROUND_POSITION2[1] = -250
        BACKGROUND_INDEX[2] = RandBG[bg_points]
        BACKGROUND2 = pygame.image.load('assets/'+BACKGROUND_IMAGES[BACKGROUND_INDEX[2]])
        BACKGROUND2 = pygame.transform.scale(BACKGROUND2, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
        points += 1
        bg_points += 1
    if bg_points == 7:
        bg_points = 0
        RandBG = random.sample(range(len(BACKGROUND_IMAGES)), len(BACKGROUND_IMAGES))

def collision_detection():
    global IN_ENDGAME, IN_GAME
    global GATO_rect
    global ENEMY_rect
    global ENEMY_DEAD, SHOOT_ACTIVE, life
    ENEMY_rect = [pygame.Rect(ENEMY_POSITION[0][0], ENEMY_POSITION[0][1], ENEMY_WIDTH[0], ENEMY_HEIGHT[0]),
                  pygame.Rect(ENEMY_POSITION[1][0], ENEMY_POSITION[1][1], ENEMY_WIDTH[1], ENEMY_HEIGHT[1]),
                  pygame.Rect(ENEMY_POSITION[2][0], ENEMY_POSITION[2][1], ENEMY_WIDTH[2], ENEMY_HEIGHT[2]),
                  pygame.Rect(ENEMY_POSITION[3][0], ENEMY_POSITION[3][1], ENEMY_WIDTH[3], ENEMY_HEIGHT[3]),
                  pygame.Rect(ENEMY_POSITION[4][0], ENEMY_POSITION[4][1], ENEMY_WIDTH[4], ENEMY_HEIGHT[4])]
    GATO_rect = pygame.Rect(GATO_POSITION[0]+15, GATO_POSITION[1]+15, GATO_WIDTH, GATO_HEIGHT)
    SHOOT_RECT = pygame.Rect(SHOOT_POSITION[0], SHOOT_POSITION[1], SHOOT_WIDTH, SHOOT_HEIGHT)
    
    for i in range(len(ENEMY)):
        if GATO_rect.colliderect(ENEMY_rect[i]) and ENEMY_DEAD[i] == False:
            ENEMY_DEAD[i] = True
            life += 1
            if life == 3:
                IN_GAME = False
                IN_GAME_MUSIC.stop()
                GAME_OVER_MUSIC.play(-1)
                IN_ENDGAME = True
            PLAYER_HIT.play()
            
        if ENEMY_rect[i].colliderect(SHOOT_RECT) and SHOOT_ACTIVE == True and ENEMY_DEAD[i] == False:
            ENEMY_DEAD[i] = True
            SHOOT_ACTIVE = False
            OBSTACLE_HIT.play()
fliped = False
def input_keys():
    global ENEMY_DEAD, GATO_SPEED, fliped
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and GATO_rect.top >= 0: 
        GATO_POSITION[1] -= 1 * GATO_SPEED
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and GATO_rect.left >= 130: 
        GATO_POSITION[0] -= 1 * GATO_SPEED
        fliped = True
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and GATO_rect.bottom <= HEIGHT: 
        GATO_POSITION[1] += 1 * GATO_SPEED
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and GATO_rect.right <= WIDTH-131: 
        GATO_POSITION[0] += 1 * GATO_SPEED
        fliped = False
    if keys[pygame.K_1]: 
        ENEMY_DEAD[0] = True
        ENEMY_DEAD[1] = True
        ENEMY_DEAD[2] = True
        ENEMY_DEAD[3] = True
        ENEMY_DEAD[4] = True

    
def draw_game_window():
    global GATO
    WIN.blit(BACKGROUND0, BACKGROUND_POSITION0)
    WIN.blit(BACKGROUND1, BACKGROUND_POSITION1)
    WIN.blit(BACKGROUND2, BACKGROUND_POSITION2)
    if SHOOT_ACTIVE == True:
        WIN.blit(SHOOT, SHOOT_POSITION)
    
    GATO = pygame.transform.flip(GATO, fliped, False)
    WIN.blit(GATO, GATO_POSITION)
    if ENEMY_DEAD[0] == False:
        WIN.blit(ENEMY[0], ENEMY_POSITION[0])
    if ENEMY_DEAD[1] == False:
        WIN.blit(ENEMY[1], ENEMY_POSITION[1])
    if ENEMY_DEAD[2] == False:
        WIN.blit(ENEMY[2], ENEMY_POSITION[2])
    if ENEMY_DEAD[3] == False:
        WIN.blit(ENEMY[3], ENEMY_POSITION[3])
    if ENEMY_DEAD[4] == False:
        WIN.blit(ENEMY[4], ENEMY_POSITION[4])

def TextDisplay(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x, y))

def LifeDisplay():
    if life < 3:
        PLAYER_LIFE_GUI = pygame.image.load(os.path.join("assets/",PLAYER_LIFE_IMAGES[life]))
        PLAYER_LIFE = pygame.transform.scale(PLAYER_LIFE_GUI, (PLAYER_LIFE_IMAGE_SIZE[0], PLAYER_LIFE_IMAGE_SIZE[1]))
        WIN.blit(PLAYER_LIFE, (20, 20))

def ShootDisplay():
    global SHOOT_GUI, SHOOT_GUI_IMAGE
    SHOOT_GUI_IMAGE = pygame.image.load(os.path.join("assets/",SHOOT_GUI_IMAGES[Shoot_Index]))
    SHOOT_GUI = pygame.transform.scale(SHOOT_GUI_IMAGE, (SHOOT_GUI_WIDTH, SHOOT_GUI_HEIGHT))
    WIN.blit(SHOOT_GUI, (20, 140))

###############      IN MENU      ###############

mouse_pos = pygame.mouse.get_pos()
playbuttonFlag, optionsmenuflag, optionsmenuflag2 = False, False, False
def DrawMenuWindow():
    global mouse_pos
    WIN.blit(MENU_BACKGROUND, (0,0))
    if playbuttonFlag == True:
        WIN.blit(PLAY_BUTTON_IMAGE, PLAY_BUTTON_POSITION)
    if optionsmenuflag == True:
        WIN.blit(OPTIONS_BUTTON_IMAGE, OPTIONS_BUTTON_POSITION)
    mouse_pos = pygame.mouse.get_pos()
    pygame.display.update()

def Buttons():
    global playbuttonFlag, optionsmenuflag, run
    playbuttonFlag, optionsmenuflag = False, False

    if mouse_pos[0] >= PLAY_BUTTON_POSITION[0] and mouse_pos[1] >= PLAY_BUTTON_POSITION[1]:
        if mouse_pos[0] <= PLAY_BUTTON_POSITION[0] + PLAY_BUTTON_SIZE[0] and mouse_pos[1] <= PLAY_BUTTON_POSITION[1] + PLAY_BUTTON_SIZE[1]:
            playbuttonFlag = True
    if mouse_pos[0] >= OPTIONS_BUTTON_POSITION[0] and mouse_pos[1] >= OPTIONS_BUTTON_POSITION[1]:
        if mouse_pos[0] <= OPTIONS_BUTTON_POSITION[0] + OPTIONS_BUTTON_SIZE[0] and mouse_pos[1] <= OPTIONS_BUTTON_POSITION[1] + OPTIONS_BUTTON_SIZE[1]:
            optionsmenuflag = True

###############    IN ENDGAME     ###############

def GameOverScreen():
    WIN.fill((0,0,0))
    WIN.blit(GAME_OVER, (0,0))
    pygame.display.update()

###############    IN OPTIONS     ###############

sombuttonflag = False
fxbuttonflag = False
def OptionsMenu():
    global IN_MENU, optionsmenuflag, mouse_pos, sombuttonflag, fxbuttonflag
    if optionsmenuflag == True:
        if IN_MENU:
            IN_MENU = not IN_MENU
        WIN.blit(OPTIONS_SCREEN, (0,0))
        pygame.display.update()
        optionsmenuflag = False
    if optionsmenuflag == False:
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] >= SOM_BUTTON_POSITION[0] and mouse_pos[1] >= SOM_BUTTON_POSITION[1]:
            if mouse_pos[0] <= SOM_BUTTON_POSITION[0] + SOM_BUTTON_SIZE[0] and mouse_pos[1] <= SOM_BUTTON_POSITION[1] + SOM_BUTTON_SIZE[1]:
                sombuttonflag = True
        if mouse_pos[0] >= FX_BUTTON_POSITION[0] and mouse_pos[1] >= FX_BUTTON_POSITION[1]:
            if mouse_pos[0] <= FX_BUTTON_POSITION[0] + FX_BUTTON_SIZE[0] and mouse_pos[1] <= FX_BUTTON_POSITION[1] + FX_BUTTON_SIZE[1]:
                fxbuttonflag = True
        WIN.blit(SOM_BUTTON, (SOM_BUTTON_POSITION[0], SOM_BUTTON_POSITION[1]))
        WIN.blit(FX_BUTTON, (FX_BUTTON_POSITION[0], FX_BUTTON_POSITION[1]))
        pygame.display.update()
    if optionsmenuflag2 == False:
        if not IN_MENU:
            IN_MENU = not IN_MENU
            
        


###############       MAIN        ###############
no_music = False
no_sound = False
def main():
    clock = pygame.time.Clock()
    global run, shoot_flag, IN_GAME, IN_MENU, IN_ENDGAME, WIDTH, HEIGHT, optionsmenuflag2, SOM_BUTTON_INDEX, SOM_BUTTON_IMAGE, FX_BUTTON_INDEX, FX_BUTTON_IMAGE, no_music, no_sound, SOM_BUTTON, FX_BUTTON
    run = True
    while run:
        print("no sound = "+ str(no_sound))
        #print("no music = "+ str(no_music))
        clock.tick(FPS)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.MOUSEBUTTONUP:
                if IN_GAME and CAN_SHOOT:
                    global SHOOT_POSITION, MOUSE_X, MOUSE_Y, SHOOT_ACTIVE
                    SHOOT_POSITION[0] = GATO_POSITION[0]+(GATO_WIDTH/2)
                    SHOOT_POSITION[1] = GATO_POSITION[1]+(GATO_HEIGHT/2)
                    MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
                    SHOOT_ACTIVE = True
                    shoot_flag = True
                if IN_MENU and playbuttonFlag and IN_GAME == False:
                    IN_MENU = False
                    IN_MENU_MUSIC.stop()
                    IN_GAME_MUSIC.play(-1)
                    IN_GAME = True
                if IN_MENU and optionsmenuflag and IN_GAME == False:
                    optionsmenuflag2 = True
                if optionsmenuflag2 and sombuttonflag and no_music == False:
                    SOM_BUTTON_INDEX = 0
                    SOM_BUTTON_IMAGE = pygame.image.load(os.path.join('assets/'+SOM_BUTTON_IMAGES[SOM_BUTTON_INDEX]))
                    SOM_BUTTON = pygame.transform.scale(SOM_BUTTON_IMAGE, SOM_BUTTON_SIZE)
                    no_music = True
                elif optionsmenuflag2 and sombuttonflag and no_music == True:
                    no_music = False
                    SOM_BUTTON_INDEX = 1
                    SOM_BUTTON_IMAGE = pygame.image.load(os.path.join('assets/'+SOM_BUTTON_IMAGES[SOM_BUTTON_INDEX]))
                    SOM_BUTTON = pygame.transform.scale(SOM_BUTTON_IMAGE, SOM_BUTTON_SIZE)
                if optionsmenuflag2 and fxbuttonflag and no_sound == False:
                    FX_BUTTON_INDEX = 0
                    FX_BUTTON_IMAGE = pygame.image.load(os.path.join('assets/'+FX_BUTTON_IMAGES[FX_BUTTON_INDEX]))
                    FX_BUTTON = pygame.transform.scale(FX_BUTTON_IMAGE, FX_BUTTON_SIZE)
                    no_sound = True
                if optionsmenuflag2 and fxbuttonflag and no_sound == True:
                    no_sound = False
                    FX_BUTTON_INDEX = 1
                    FX_BUTTON_IMAGE = pygame.image.load(os.path.join('assets/'+FX_BUTTON_IMAGES[FX_BUTTON_INDEX]))
                    FX_BUTTON = pygame.transform.scale(FX_BUTTON_IMAGE, FX_BUTTON_SIZE)
            if event.type == pygame.QUIT:
                run = False
            if keys[pygame.K_ESCAPE]:
                if IN_MENU == False and IN_ENDGAME == False:
                    IN_GAME = not IN_GAME
                elif IN_MENU:
                    run = False
                if IN_ENDGAME:
                    IN_ENDGAME = False
                    GAME_OVER_MUSIC.stop()
                    IN_MENU_MUSIC.play(-1)
                    IN_MENU = True
                if optionsmenuflag == True:
                    optionsmenuflag2 = False
                    OptionsMenu()
        if IN_MENU:
            DrawMenuWindow()
            Buttons()
        elif IN_GAME:
            if shoot_flag == True:
                Timer()   
            TextDisplay(str(round(points, 2)), text_font, (0,0,0), 20, 70)
            pygame.display.update()
            draw_game_window()
            input_keys()
            collision_detection()
            background()
            Spawn()
            Obstacle()
            DificultGenerator()
            shoot()
            EASTER_EGG()
            LifeDisplay()
            ShootDisplay()
        elif IN_ENDGAME:
            GameOverScreen()
        if optionsmenuflag2 == True:
            OptionsMenu()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()