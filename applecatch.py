import pgzrun
from random import randint

WIDTH=600
HEIGHT=600
game_over=False
score=0

apple=Actor("apple")
apple.pos=200,100

basket=Actor("basket")
basket.pos=500,500

def draw():
    screen.blit("forest",(0,0))
    apple.draw()
    basket.draw()
    screen.draw.text("Score : "+ str(score),color="Black",topleft=(10,10))
    if game_over:
        screen.fill("Grey")
        screen.draw.text("Game Over and Your final score : "+str(score),midtop=(WIDTH/2,10),fontsize=40,color="White")

def time_up():
    global game_over
    global score
    game_over=True

def update():
    global score
    if keyboard.left:
        basket.x=basket.x-5
    if keyboard.right:
        basket.x=basket.x+5
    if basket.colliderect(apple):
        apple.y=0
        apple.x=randint(70,(WIDTH-70))

        score=score+1
        
    apple.y=apple.y+5


clock.schedule(time_up,20.0)

pgzrun.go()