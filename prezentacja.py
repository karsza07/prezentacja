import pygame 
pygame.init()
import prezentacja_klasy

presentation = True
slide  = 0
screen = pygame.display.set_mode((1366,768))
klasy  = prezentacja_klasy.slide_change()

while presentation:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            presentation = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                slide += 1
            elif event.key == pygame.K_LEFT and slide != 0:
                slide -= 1
            elif event.key == pygame.K_ESCAPE:
                presentation = False


    screen.fill((232, 226,226))
    klasy.slide(screen, slide)
    pygame.display.flip()

pygame.quit()               