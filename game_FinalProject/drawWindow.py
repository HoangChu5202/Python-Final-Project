import pygame

from pygame import draw

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Rock Paper Scissor")


# Creat button with effect when you click on it
class Button:
    def __init__(self, image, width, height, pos, elevation): #elevation mean how hight of the button
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.origin_y_pos = pos[1]
        #Top rectangle
        self.top_rect = pygame.Rect((pos), (width, height))
        self.top_color = LIGHTYELLOW
        #Bottom rectangle
        self.bot_rect = pygame.Rect(pos, (width, elevation))
        self.bot_color = LIGHTGRAY
        #Write Text on button
        self.image_suft = image
        self.image_rect = self.image_suft.get_rect(center = self.top_rect.center)

    def draw(self):
        #elevation logic
        self.top_rect.y = self.origin_y_pos - self.dynamic_elevation #This will set the button up so it make the click down effect when you click on it 
        self.image_rect.center = self.top_rect.center #Make the text center the of the button

        self.bot_rect.midtop = self.top_rect.midtop
        self.bot_rect.height = self.top_rect.height + self.dynamic_elevation
        #Draw bottom rectangle Or the shadow of the button
        pygame.draw.rect(screen, self.bot_color, self.bot_rect, border_radius = 12) #We have to draw shadow first because what draw after will overlay the one before
        #Draw top button
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = 12)
        screen.blit(self.image_suft, self.image_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos): #This code check if your mouse (Or mouse position) inside the button 
            if pygame.mouse.get_pressed()[0]:   #This code check if you click by right mouse button
                self.dynamic_elevation = 0      #dynamic_elevation = 0 mean shift the button down [elevation] pixel
                self.pressed = True             #Without these codes pygame will take that you have click a lot of time. Because pygame draw to your screen 60 frame in 1 second
            else:                               
                if self.pressed == True:        #So we need to check only count when we realease the button
                    print("Click")
                    self.dynamic_elevation = self.elevation #This set dynamic_elevation back to elevation so the button shift up back when you realease the mouse button
                    self.pressed = False

def get_image(img_location, scale):
    result = pygame.image.load(img_location) #Get image
    result = pygame.transform.scale(result, scale)  #Then scale the image
    return result

def health_bar(cur_hp, max_hp, px_hp = 380):
    result = cur_hp * 100 / max_hp
    result = int(result * px_hp / 100)
    return result

#Create the screen
SCREEN_WITDH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WITDH,SCREEN_HEIGHT))
#Font of text
font = pygame.font.Font(None, 30)
#All color use to draw
WHITE = (255,255,255)
BLACK = (0, 0, 0)
GRAY = (150,150,150)
RED = (255,0,0)
LIGHTGRAY = (161, 160, 151)
LIGHTYELLOW = (237, 233, 83)



#### REMEMBER TO DELETE
boss_health = health_bar(1,20)
mc_health = health_bar(10, 15)
####

def gameEXE():
    #Background
    background = get_image("./images/background.jpg", (1000,600))
    battle_bacground = get_image("./images/DemonCastle.png", (1000,760))
    #main character image
    mc_image = get_image("./images/player.png", (210,200))
    #Boss image
    boss_img = get_image("./images/boss.png", (350,200))
    #Vs icon
    vs_icon = get_image("./images/vs_icon2.png", (100, 100))
    #Picl bar
    pick_bar = get_image("./images/pick_bar.png", (700, 160))
    #Rock-Paper-Scissor image
    rock_img = get_image("./images/rock.png", (70,70))
    paper_img = get_image("./images/paper.png", (70,70))
    scissor_img = get_image("./images/scissors.png", (70,70))
    
    rock_button = Button(rock_img, 80, 80, (340,480), 5)  #Right button
    paper_button = Button(paper_img, 80, 80, (460,480), 5)  #Middle button
    scissor_button = Button(scissor_img, 80, 80, (580,480), 5)  #Left button


    running = True
    while running:
        screen.fill(WHITE)
        #fill screen with background
        screen.blit(background, (0, 0))
        screen.blit(battle_bacground, (0, 0))
        #This code use to get position of your mouse
        # mouse_x , mouse_y = pygame.mouse.get_pos()

        #Draw health bar
        pygame.draw.rect(screen, GRAY, (20,20, 380,30)) #Boss health bar(HP)
        pygame.draw.rect(screen, RED, (20,20, boss_health,30))
        pygame.draw.rect(screen, GRAY, (600,20, 380,30)) #Our character health bar(HP)
        pygame.draw.rect(screen, RED, (600,20, mc_health,30))
        #Draw character
        screen.blit(mc_image, (650,200))
        screen.blit(boss_img, (0, 200))
        
        screen.blit(vs_icon, (460, 5))
        screen.blit(pick_bar, (150, 425))
        #Draw the button
        rock_button.draw()
        paper_button.draw()
        scissor_button.draw()
        # All this code below is get input and do what ever you want
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass
            # This code alow you to close the window when click on top right X button
            if event.type == pygame.QUIT:
                running = False
        
        # This code use to draw everything to screen 
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


gameEXE()