class Player:
    def __init__(self):
        self.vertical_displacement = 100
        self.vertical_velocity = 9

    def update_vertical_displacement(self):
        self.vertical_displacement += self.vertical_velocity

    def jump(self, button_status):
        if button_status == "hold":
            self.vertical_velocity = -13
        elif button_status == "press":
            self.vertical_velocity = -30
        self.update_vertical_displacement()
        for obstacle in obstacles:
            if obstacle.x_position < -50:
                obstacles.remove(obstacle)
            else:
                obstacle.scroll()
        self.vertical_velocity = 9

    def fall(self):
        self.update_vertical_displacement()
        window.blit(plane_image, (0, play.vertical_displacement))


class Obstacle:
    def __init__(self):
        self.opening_top = random.randint(1, 650)
        self.opening_bottom = self.opening_top + 50
        self.x_position = 1100

    def scroll(self):
        self.x_position -= 5
        self.draw()

    def draw(self):
        pygame.draw.rect(window, green, (self.x_position, 0, 50, self.opening_top))


running = True
green = (0, 255, 0)
white = (255, 255, 255)
play = Player()
obstacles = []
horizontal_distance_moved = 0
num = 0;

window.fill(white)
window.blit(plane_image, (0, play.vertical_displacement))
pygame.display.update()

time.sleep(1.5)

while running:
    pygame.time.Clock().tick(200)
    window.fill(white)
    play.fall()
    if horizontal_distance_moved % 100 == 0:
        ob = Obstacle()
        obstacles.append(ob)

    events = pygame.event.get()
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_SPACE]:
        play.jump("hold")
    else:
        for obstacle in obstacles:
            if obstacle.x_position < -50:
                obstacles.remove(obstacle)
            else:
                obstacle.scroll()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play.jump("press")
            else:
                for obstacle in obstacles:
                    if obstacle.x_position < -50:
                        obstacles.remove(obstacle)
                    else:
                        obstacle.scroll()

    if play.vertical_displacement > 585:
        running = False

    pygame.display.update()
    horizontal_distance_moved += 5

pygame.quit()
