import pygame, sys
import rock_paper_scissor, data


pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Rock Paper Scissor")


# Creat button with effect when you click on it
#############################################################################################################################################################
class Button:
    def __init__(self, image, width, height, pos, elevation, name): #elevation mean how hight of the button
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

        self.id = name

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
                    # print(self.id)
                    self.dynamic_elevation = self.elevation #This set dynamic_elevation back to elevation so the button shift up back when you realease the mouse button
                    self.pressed = False

    def click(self, event):
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if self.top_rect.collidepoint(x, y):    
                        return self.id #Return the ID of the button ("Rock", "Paper" or "Scissor")
##############################################################################################################################################################################

#Exposion animation
################################################################################################################
class Expolsion(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.is_animating = False
        self.is_showing = False
        self.sprites = []
        for i in range(1,31):
            self.sprites.append(pygame.image.load("./images/explosion/explosion" + str(i) + ".png")) #Append 30 explosion image to the self.sprites
        self.current_sprite = 0     #Set self.current_sprite to index 0 so it will start at the first image
        self.image = self.sprites[self.current_sprite]  #Set self.image to the current sprite
        self.rect = self.image.get_rect()   #Create a rectangel then assign the image to that rectangle
        self.rect.topleft = [pos_x, pos_y]  #Set the position of that rectangle (Or the position of the image) to the position that I set when I call this function

    def animate(self):
        self.is_animating = True    #When this function is called the sprite will amimate

    def show(self):
        return self.is_showing  #Return is_showing so later we can decide when the animation if show up 

    def update(self):
        if self.is_animating == True:   #Run the animation only when it called
            self.current_sprite += 0.2 #Add 0.2 to the index so it will go to next index. If add 1 the animation will go supper fast
            if self.current_sprite >= len(self.sprites):    #If the current_sprite reach the end of the sprites list(Or the the end of animation)
                self.current_sprite = 0                     #Then set the current_sprite to 0 (or index of the first image of the animation) of I can reuse it
                self.is_animating = False                   #End the animation so it will not loop
                self.is_showing = False                     #Then hide the animation
            self.image = self.sprites[int(self.current_sprite)] #After do all of the thing above then just set the image to sprites[current_sprite]; I used int() so it won't make the index ERORR.

    def who_lose(self):
        self.is_showing = True  #Set is_showing to True so it play the animation on who lose
##################################################################################################################


def get_image(img_location, scale):
    result = pygame.image.load(img_location) #Get image
    result = pygame.transform.scale(result, scale)  #Then scale the image
    return result

def health_bar(cur_hp, max_hp, px_hp = 380):
    result = cur_hp * 100 / max_hp
    result = result * px_hp / 100
    return result


def minus_hp(cur_hp, atk):  #Current Hp of who lose and ATK of who won
    cur_hp = cur_hp - atk
    return cur_hp

def who_win(winner, boss_cur_hp, boss, mc_cur_hp, mc):
    boss_max_hp = boss[0]
    boss_atk = boss[1]
    mc_max_hp = mc[0]
    mc_atk = mc[1]
    
    if winner == "Player":
        boss_cur_hp = minus_hp(boss_cur_hp, mc_atk)
        boss_health = health_bar( boss_cur_hp, boss_max_hp)
        print("Boss: " + str(boss_cur_hp))
        print(boss_health)
        print()
        return boss_cur_hp, boss_health
    else:
        mc_cur_hp = minus_hp(mc_cur_hp, boss_atk)
        mc_health = health_bar( mc_cur_hp, mc_max_hp)
        print("MC: " + str(mc_cur_hp))
        print(mc_health)
        print()
        return mc_cur_hp, mc_health

def endGame(boss_cur_hp, mc_cur_hp):
    if boss_cur_hp <= 0:
        return "Boss"
    if mc_cur_hp <= 0:
        return "Player"

#Create the screen
SCREEN_WITDH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WITDH,SCREEN_HEIGHT))
#All color use to draw
WHITE = (255,255,255)
BLACK = (0, 0, 0)
GRAY = (150,150,150)
RED = (255,0,0)
LIGHTGRAY = (161, 160, 151)
LIGHTYELLOW = (237, 233, 83)



def gameEXE(boss, mc):
    #GENARAL SET UP
    #########################################################################
    #Background
    background = get_image("./images/background.jpg", (1000,600))
    battle_bacground = get_image("./images/DemonCastle.png", (1000,760))
    #Win and lose image
    win_background = get_image("./images/win.jpg", (1000,600))
    lose_background = get_image("./images/lose.jpg", (1000,600))
    win_hide = True
    lose_hide = True
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
    #Character Hp
    boss_cur_hp = boss[0]   #Boss Current Hp; boss[0] is the boss hp
    boss_max_hp = boss[0]   #Boss Max Hp
    mc_cur_hp = mc[0]       #Main character current Hp
    mc_max_hp = mc[0]       #Main character max Hp
    boss_health = health_bar(boss_cur_hp,boss_max_hp)
    mc_health = health_bar(mc_cur_hp, mc_max_hp)
    #Define button
    rock_button = Button(rock_img, 80, 80, (340,480), 5, "ROCK")  #Right button
    paper_button = Button(paper_img, 80, 80, (460,480), 5, "PAPER")  #Middle button
    scissor_button = Button(scissor_img, 80, 80, (580,480), 5, "SCISSOR")  #Left button
    #Define explosion animation
    moving_sprites = pygame.sprite.Group()
    explosin1 = Expolsion(70, 100)  #Eplosion on boss
    moving_sprites.add(explosin1)

    explosin2 = Expolsion(700, 100) #Explosion on main charater
    moving_sprites.add(explosin2)
    running = True
    result = ""
    ########################################################################## 
    while running:
        # All this code below is get input on screen and do what ever you want
        for event in pygame.event.get(): 
            #click on the button on screen to triger the event
            #######################################################################################
            if (mc_cur_hp > 0) and (boss_cur_hp >0):
                #***********************************************************************************
                                        #ROCK BUTTON
                if rock_button.click(event) == "ROCK":
                    winner = (rock_paper_scissor.rk_pr_sr("ROCK"))
                    if winner == "Player":
                        boss_cur_hp, boss_health = who_win(winner, boss_cur_hp, boss, mc_cur_hp, mc)
                        explosin1.who_lose()
                        explosin1.animate()
                        loser = endGame(boss_cur_hp, mc_cur_hp)
                        if loser == "Boss":
                            print("You win")
                            win_hide = False
                    elif winner == "Computer":
                        mc_cur_hp, mc_health = who_win(winner, boss_cur_hp, boss, mc_cur_hp, mc)
                        explosin2.who_lose()
                        explosin2.animate()
                        loser = endGame(boss_cur_hp, mc_cur_hp)
                        if loser == "Player":
                            print("You lose")
                            lose_hide = False
                #***********************************************************************************
                                        #PAPER BUTTON
                if paper_button.click(event) == "PAPER":
                    winner = (rock_paper_scissor.rk_pr_sr("PAPER"))
                    if winner == "Player":
                        boss_cur_hp, boss_health = who_win(winner, boss_cur_hp, boss, mc_cur_hp, mc)
                        explosin1.who_lose()
                        explosin1.animate()
                        loser = endGame(boss_cur_hp, mc_cur_hp)
                        if loser == "Boss":
                            print("You win")
                            win_hide = False
                    elif winner == "Computer":
                        mc_cur_hp, mc_health = who_win(winner, boss_cur_hp, boss, mc_cur_hp, mc)
                        explosin2.who_lose()
                        explosin2.animate()
                        loser = endGame(boss_cur_hp, mc_cur_hp)
                        if loser == "Player":
                            print("You lose")
                            lose_hide = False
                #***********************************************************************************
                                        #SCISSOR BUTTON
                if scissor_button.click(event) == "SCISSOR":
                    winner = rock_paper_scissor.rk_pr_sr("SCISSOR")
                    if winner == "Player":
                        boss_cur_hp, boss_health = who_win(winner, boss_cur_hp, boss, mc_cur_hp, mc)
                        explosin1.who_lose()
                        explosin1.animate()
                        loser = endGame(boss_cur_hp, mc_cur_hp)
                        if loser == "Boss":
                            print("You win")
                            win_hide = False
                    elif winner == "Computer":
                        mc_cur_hp, mc_health = who_win(winner, boss_cur_hp, boss, mc_cur_hp, mc)
                        explosin2.who_lose()
                        explosin2.animate()
                        loser = endGame(boss_cur_hp, mc_cur_hp)
                        if loser == "Player":
                            print("You lose")
                            lose_hide = False
            ########################################################################################
           
            # This code alow you to close the window when click on top right X button
            if event.type == pygame.QUIT:
                running = False
                return result
                
                


        #fill screen with background
        screen.blit(background, (0, 0))
        screen.blit(battle_bacground, (0, 0))        
        #Draw character
        screen.blit(mc_image, (650,200))
        screen.blit(boss_img, (0, 200))
        #Draw vs icon and pick bar
        screen.blit(vs_icon, (460, 5))
        screen.blit(pick_bar, (150, 425))
        #Draw health bar
        pygame.draw.rect(screen, GRAY, (20,20, 380,30)) #Boss health bar(HP)
        pygame.draw.rect(screen, RED, (20,20, boss_health,30))
        pygame.draw.rect(screen, GRAY, (600,20, 380,30)) #Our character health bar(HP)
        pygame.draw.rect(screen, RED, (600,20, mc_health,30)) 
        #Draw the button
        rock_button.draw()
        paper_button.draw()
        scissor_button.draw()

        if explosin1.show() == True:
            moving_sprites.draw(screen)
            moving_sprites.update()

        if explosin2.show() == True:
            moving_sprites.draw(screen)
            moving_sprites.update()

        if win_hide == False:
            screen.blit(win_background, (0,0))
        elif lose_hide == False:
            screen.blit(lose_background, (0,0))
        
        if mc_cur_hp == 0:
            result = "lose"
        if boss_cur_hp == 0:
            result = "win"
        # This code use to draw everything to screen 
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()
    
  
def main():
    boss = data.get_status("Boss")
    mc = data.get_status("Player")
    result = gameEXE(boss, mc)
    data.update_history(result)

main()