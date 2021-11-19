import pygame, sys

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Rock Paper Scissor")

#Background
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (1280,720)) #Scale the picture to my screen size
#Create the screen
SCREEN_WITDH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WITDH,SCREEN_HEIGHT))
#Font of text
font = pygame.font.Font(None, 30)
#All color use to draw
WHITE = (255,255,255)
BLACK = (0, 0, 0)
GRAY = (150,150,150)
LIGHTGRAY = (161, 160, 151)
LIGHTYELLOW = (237, 233, 83)

running = True

# Creat button with effect when you click on it
class Button:
    def __init__(self, text, width, height, pos, elevation): #elevation mean how hight of the button
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
        self.text_suft = font.render(text, True, BLACK)
        self.text_rect = self.text_suft.get_rect(center = self.top_rect.center)

    def draw(self):
        #elevation logic
        self.top_rect.y = self.origin_y_pos - self.dynamic_elevation #This will set the button up so it make the click down effect when you click on it 
        self.text_rect.center = self.top_rect.center #Make the text center the of the button

        self.bot_rect.midtop = self.top_rect.midtop
        self.bot_rect.height = self.top_rect.height + self.dynamic_elevation
        #Draw bottom rectangle Or the shadow of the button
        pygame.draw.rect(screen, self.bot_color, self.bot_rect, border_radius = 10) #We have to draw shadow first because what draw after will overlay the one before
        #Draw top button
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = 10)
        screen.blit(self.text_suft, self.text_rect)
        self.check_click()
        

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos): #This code check if your mouse (Or mouse position) inside the button (Or my top rectangle)
            if pygame.mouse.get_pressed()[0]:   #This code check if you click by right mouse button
                self.dynamic_elevation = 0      #dynamic_elevation = 0 mean shift the button down [elevation] pixel
                self.pressed = True             #Without these codes pygame will take that you have click a lot of time. Because pygame draw to your screen 60 frame in 1 second
            else:                               
                if self.pressed == True:        #So we need to check only count when we realease the button
                    print("Click")
                    self.dynamic_elevation = self.elevation #This set dynamic_elevation back to elevation so the button shift up back when you realease the mouse button
                    self.pressed = False


button1 = Button("Click me", 200, 40, (50,100), 5)

while running:
    screen.fill(WHITE)
    #fill screen with background
    screen.blit(background, (0, 0))
    #This code use to get position of your mouse
    mouse_x , mouse_y = pygame.mouse.get_pos()

    button1.draw()
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