import pygame, os, sys
import time
import random

# Position game window in center of screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

window = pygame.display.set_mode((1150, 700))

plane_image = pygame.image.load("plane.png").convert_alpha()
background_image = pygame.image.load("background.png").convert_alpha()

font = pygame.font.Font('freesansbold.ttf', 32)

pygame.display.set_caption("Evasive Maneuvers")
pygame.display.set_icon(plane_image)


class Player:
    def __init__(self):
        self.vertical_displacement = 100
        self.vertical_velocity = 0
        self.horizontal_distance_moved = 0
        self.points = 0

    def update_vertical_displacement(self):
        self.vertical_displacement += self.vertical_velocity

    def update_position(self):
        if self.vertical_velocity > 13:
            self.vertical_velocity = 13
        elif self.vertical_velocity < -13:
            self.vertical_velocity = -13

        self.update_vertical_displacement()

        left_obstacle = obstacles[0]
        if left_obstacle.x_position < -85:
            obstacles.remove(left_obstacle)
            self.points += 1

        for obstacle in obstacles:
            obstacle.scroll()

        window.blit(plane_image, (0, play.vertical_displacement))

        self.horizontal_distance_moved += 6

    def collide(self, obstacle):
        return obstacle.x_position < 85 and (self.vertical_displacement <= obstacle.opening_top or
                                             self.vertical_displacement + 92 > obstacle.opening_bottom)


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


def display_text(font, string, x, y):
    text = font.render(string, True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    window.blit(text, text_rect)


def display_game_over_screen(points):
    draw_background()
    display_text(font, "Final Score: " + str(points), 575, 150)
    pygame.display.update()
    time.sleep(5)


def display_main_menu():
    draw_background()
    f = pygame.font.Font('freesansbold.ttf', 72)
    display_text(f, "Evasive Maneuvers", 575, 50)
    f = pygame.font.Font('freesansbold.ttf', 36)
    display_text(f, "Press space to start game", 575, 175)
    pygame.display.update()

def exit_game():
    pygame.display.quit()
    pygame.quit()
    sys.exit()


while True:
    display_main_menu()

    begin_game = False
    while not begin_game:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    begin_game = True

    green = (0, 255, 0)
    play = Player()
    obstacles = []

    draw_background()
    display_text(font, "Points: 0", 100, 32)
    window.blit(plane_image, (0, play.vertical_displacement))
    pygame.display.update()

    time.sleep(1)

    while True:
        pygame.time.Clock().tick(120)

        draw_background()
        display_text(font, "Points: " + str(play.points), 100, 32)

        if play.horizontal_distance_moved % 600 == 0:
            ob = Obstacle()
            obstacles.append(ob)

        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.QUIT:
                exit_game()

        if keys[pygame.K_SPACE]:
            play.vertical_velocity -= 0.70
        else:
            play.vertical_velocity += 0.70

        play.update_position()

        pygame.display.update()

        if play.collide(obstacles[0]):
            display_game_over_screen(play.points)
            exit_game()

        if play.vertical_displacement > 615 or play.vertical_displacement <= 0:
            display_game_over_screen(play.points)
            exit_game()

