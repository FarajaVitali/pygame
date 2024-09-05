import pygame
import random

pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width,screen_height))
icon = pygame.image.load('./pictures/doge.png')
text = pygame.display.set_caption("Doge Game")

pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('./pictures/jet-plane.png')
playerX = 200
playerY= 400
playerX_change = 0

#enemy
enemyImg = pygame.image.load('./pictures/enemy.png')

enemyX = random.randint(0,0)
enemyY= random.randint(20,40)
enemy_changeX = 0
enemy_changeY = 0

rotatedImg = pygame.transform.rotate(enemyImg,180)

def player(x,y):
    screen.blit(playerImg,(x,y))
    
def enemy(x,y):
    screen.blit(rotatedImg,(x,y))    

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False        
        if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                  playerX_change = -0.5
              if event.key == pygame.K_RIGHT:
                  playerX_change = 0.5         
        if event.type == pygame.KEYUP:
              if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                  playerX_change = 0         
    playerX += playerX_change  
    if playerX <= 0:
        playerX = 0
    if playerX >= 436:
        playerX = 436
    enemyX += enemy_changeX  
    if enemyX <= 0:
       enemy_changeX = 0.3
    if enemyX >= 436:
       enemy_changeX = -0.3                  
    screen.fill((0,0,0))        
    player(playerX,playerY)
    enemy(enemyX,enemyY)        
    pygame.display.update()       