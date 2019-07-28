import pygame, os
import time
import random

# Position game window in center of screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

window = pygame.display.set_mode((1150, 700))

plane_image = pygame.image.load("plane.png").convert_alpha()
background_image = pygame.image.load("background.png").convert_alpha()

pygame.display.set_caption("Evasive Maneuvers")
pygame.display.set_icon(plane_image)


class Player:
    def __init__(self):
        self.vertical_displacement = 100
        self.vertical_velocity = 0

    def update_vertical_displacement(self):
        self.vertical_displacement += self.vertical_velocity

    def update_height(self):
        if self.vertical_velocity > 13:
            self.vertical_velocity = 13
        elif self.vertical_velocity < -13:
            self.vertical_velocity = -13
        self.update_vertical_displacement()
        for obstacle in obstacles:
            if obstacle.x_position < -50:
                obstacles.remove(obstacle)
            else:
                obstacle.scroll()
        window.blit(plane_image, (0, play.vertical_displacement))


class Obstacle:
    def __init__(self):
        self.opening_top = random.randint(50, 500)
        self.opening_bottom = self.opening_top + 200
        self.x_position = 1100

    def scroll(self):
        self.x_position -= 6
        self.draw()

    def draw(self):
        pygame.draw.rect(window, green, (self.x_position, 0, 85, self.opening_top))
        pygame.draw.rect(window, green, (self.x_position, self.opening_bottom, 85, 700 - self.opening_bottom))


def draw_background():
    window.blit(background_image, (0, 0))


running = True
green = (0, 255, 0)
white = (255, 255, 255)
play = Player()
obstacles = []
horizontal_distance_moved = 0

draw_background()
window.blit(plane_image, (0, play.vertical_displacement))
pygame.display.update()

time.sleep(1.5)

while running:
    pygame.time.Clock().tick(120)
    draw_background()
    if horizontal_distance_moved % 600 == 0:
        ob = Obstacle()
        obstacles.append(ob)

    events = pygame.event.get()
    keys = pygame.key.get_pressed()  # checking pressed keys

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if keys[pygame.K_SPACE]:
        play.vertical_velocity -= 0.70
    else:
        play.vertical_velocity += 0.70

    play.update_height()

    if play.vertical_displacement > 615:
        running = False

    pygame.display.update()

    horizontal_distance_moved += 6

pygame.quit()
