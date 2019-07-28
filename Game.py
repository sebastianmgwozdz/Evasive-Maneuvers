import pygame, os
import time

# Position game window in center of screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

plane_image = pygame.image.load("plane.png")

window = pygame.display.set_mode((1150, 700))
pygame.display.set_caption("Evasive Maneuvers")
pygame.display.set_icon(plane_image)


class Player:
    def __init__(self):
        self.vertical_displacement = 289
        self.vertical_velocity = 5

    def update_vertical_displacement(self):
        self.vertical_displacement += self.vertical_velocity

    def jump(self):
        initial_displacement = self.vertical_displacement
        final_displacement = self.vertical_displacement
        self.vertical_velocity = -1.8
        while final_displacement - initial_displacement > -25:
            self.update_vertical_displacement()
            window.fill(white)
            window.blit(plane_image, (0, play.vertical_displacement))
            pygame.display.update()
            final_displacement = self.vertical_displacement
        self.vertical_velocity = 5

    def fall(self):
        self.update_vertical_displacement()
        window.fill(white)
        window.blit(plane_image, (0, play.vertical_displacement))
        pygame.display.update()


running = True
white = (255, 255, 255)
play = Player()

window.fill(white)
window.blit(plane_image, (0, play.vertical_displacement))
pygame.display.update()
time.sleep(1.5)

while running:
    pygame.time.Clock().tick(120)
    play.fall()

    events = pygame.event.get()
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_SPACE]:
        play.jump()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play.jump()

    if play.vertical_displacement > 585:
        running = False

pygame.quit()
