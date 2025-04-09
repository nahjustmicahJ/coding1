import pygame 
import button
import shooter_1
import shooter_2
import shooter_3

pygame.init()

screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Preposterous Propoganza")

clock = pygame.time.Clock()
FPS = 60


shooterA = shooter_1()

while running:
    clock.tick(FPS)
    screen.fill((255,255,255))  

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            pygame.draw.rect(shooter_1)


pygame.quit() 