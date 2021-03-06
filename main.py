import sys, pygame
from pygame.locals import *

# 224 x 256 pixels x 4
size = width, height = 896, 1024
backgroundColor = 34, 58, 96

pygame.init()
pygame.display.set_caption("Time Pirate")
screen = pygame.display.set_mode(size)

topDisplayRect = pygame.Rect(0, 0, width, 32 * 4)
bottomDisplayRect = pygame.Rect(0, height - (8 * 4), width, 8 * 4)

score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        # Keyboard events
        if event.type == KEYDOWN:
            if event.key == K_w:
                print("up")
            elif event.key == K_a:
                print("left")
            elif event.key == K_s:
                print("right")
            elif event.key == K_d:
                print("down")
            elif event.key == K_SPACE:
                print("shoot")

    # Draw background color
    screen.fill(backgroundColor)
    # Draw display rects
    screen.fill((0, 0, 0), topDisplayRect)
    screen.fill((0, 0, 0), bottomDisplayRect)

    # Draw score
    if pygame.font:
        arcadeFont = pygame.font.Font("ARCADECLASSIC.ttf", 56)
        text = arcadeFont.render("SCORE", False, (230, 230, 230))
        scoreText = arcadeFont.render(str(score), False, (230, 230, 230))
        textpos = text.get_rect(centerx=screen.get_width()/2)
        scoreTextPos = scoreText.get_rect(centerx=screen.get_width()/2, centery=64)
        screen.blit(text, textpos)
        screen.blit(scoreText, scoreTextPos)

    # Update display
    pygame.display.flip()

