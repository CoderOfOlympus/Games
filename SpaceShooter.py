import pygame
import random
import sys

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Shooter")

WHITE = (255,255,255)
RED = (255,0,0)
clock = pygame.time.Clock()
FPS = 60

player_img = pygame.Surface((50,40))
player_img.fill(WHITE)
player_x = WIDTH//2-25
player_y  = HEIGHT - 60
player_speed = 5


bullet_img = pygame.Surface((5,10))
bullet_img.fill(RED)
bullets = []
bullet_speed = 7


enemy_img = pygame.Surface((40,30))
enemy_img.fill((0,255,0))
enemies = []
enemy_speed = 3
enemy_spawn_delay = 30
enemy_timer = 0


score = 0
font = pygame.font.SysFont(None,30)

def draw_text(text,x,y):
    img = font.render(text,True,WHITE)
    screen.blit(img,(x,y))

running = True
while running:
    clock.tick(FPS)
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:
            bullets.append([player_x + 22,player_y])
    for bullet in bullets[:]:
            bullet[1]-=bullet_speed
            if bullet[1] < 0:
                bullets.remove(bullet)

    enemy_timer +=1
    if enemy_timer>enemy_spawn_delay:
            enemy_x = random.randint(0,WIDTH-40)
            enemies.append([enemy_x,0])
            enemy_timer = 0

    for enemy in enemies[:]:
        enemy[1]+=enemy_speed
        if enemy[1]>HEIGHT:
            enemies.remove(enemy)

    for bullet in bullets[:]:
            for enemy in enemies[:]:
                if (bullet[0] in range(enemy[0],enemy[0]+40) and bullet[1] in range(enemy[1],enemy[1]+30)):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score+=1
                    break
        
    screen.blit(player_img,(player_x,player_y))

    for bullet in bullets:
            screen.blit(bullet_img,(bullet[0],bullet[1]))
    for enemy in enemies:
            screen.blit(enemy_img,(enemy[0],enemy[1]))

    draw_text(f"Score: {score}",10,10)
    pygame.display.update()

pygame.quit()
sys.exit()        
