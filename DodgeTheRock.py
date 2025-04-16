import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 350

game_over = False
score = 0


#Characters
rock = Actor("rock")
rock.pos = 100,100

nathan = Actor("nathan drake")
nathan.pos = 300,250

def draw():
    screen.blit("land",(0,0))
    rock.draw()
    nathan.draw()
    screen.draw.text("Rocks Dodged : "+ str(score),color="Red",topleft=(10,10))
    if game_over:
        screen.fill("Grey")
        screen.draw.text("Game Over and Your final score : "+str(score),midtop=(WIDTH/2,10),fontsize=40,color="White")


def update():
    global score
    global game_over

    if keyboard.left:
        nathan.x -= 5
    if keyboard.right:
        nathan.x += 5

   
    rock.y += 5

    
    if nathan.colliderect(rock):
        game_over = True

     
    if rock.y > HEIGHT:
        
        if not nathan.colliderect(rock):
            score += 1
        
        
        rock.y = 0
        rock.x = randint(70, WIDTH - 70)
    



pgzrun.go()
