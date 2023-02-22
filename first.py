import pygame
pygame.init()#initalize modules

#Creating window
gameWindow=pygame.display.set_mode((1200,500))#Defines game window size
pygame.display.set_caption("My first game")#Setting up title

#definig game specific variables
exit_game=False
game_over=False


#Creating a game loop
while not exit_game:
    for event in pygame.event.get(): #pygame.event.get() contains all the possible events
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type==pygame.KEYDOWN:#enables program to use key 
            if event.key == pygame.K_Right:
                print("right")

pygame.quit()
quit() 