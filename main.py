import pygame
import random
import time



pygame.init()
width = 480
height = 480
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption("Snake")
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
score = 0

snake_pos = [width/2,height/2]
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]
fruit_position = [random.randrange(1, (height//10)) * 10,
                  random.randrange(1, (width//10)) * 10]

def score_func(colour, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score: "+score, True, colour)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)

def game_over(colour, font, size):
    game_over_font = pygame.font.SysFont(font, size)
    game_over_surface = game_over_font.render("Score: "+score, True, colour)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width/2, height/2)
    screen.blit(game_over_surface, game_over_rect)
    time.sleep(4)
    pygame.quit()
    quit()

while running:
    for event in pygame.event.get():
        pass
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake_pos[1] -= 1
    if keys[pygame.K_s]:
        snake_pos[1] += 1
    if keys[pygame.K_a]:
        snake_pos[0] -= 1
    if keys[pygame.K_d]:
        snake_pos[0] += 1
    screen.fill("green")

    snake_body.insert(0,list(snake_pos))
    if snake_pos[0] == fruit_position[0] and snake_pos[1] == fruit_position[1]:
        score += 1
    
    for pos in snake_body:
        pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], 10, 10))

    if snake_pos[0] <= -3 or snake_pos[0] > width:
        game_over("white", "Times New Roman", 50)
    if snake_pos[1] <= -3 or snake_pos[1] > height:
        game_over("white", "Times New Roman", 50)

    pygame.display.update()