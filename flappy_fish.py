import pygame
from sea_floor import SeaFloor
import sys
from fish import Fish
from random import randint
from pygame import mixer
import settings
from obsticale import Obsticale
from health import Health

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Fish")
screen_rect = screen.get_rect()
water_top = pygame.image.load("images/water_tile.png")
water_top_rect = water_top.get_rect()
water_full = pygame.image.load("images/water_full.png")
water_full_rect = water_full.get_rect()
sand_full = pygame.image.load("images/kenney_fishpack/PNG/Default size/fishTile_001.png")
sand_full_rect = sand_full.get_rect()


random_position_x = randint(0, 200)
random_position_y = randint(0, 896)

fish = Fish(screen)
obsticales = pygame.sprite.Group(Obsticale((settings.SCREEN_WIDTH, 50)),
                                 Obsticale((settings.SCREEN_WIDTH + 200, 800)),
                                 Obsticale((settings.SCREEN_WIDTH + 300, 200)),
                                 Obsticale((settings.SCREEN_WIDTH + 400, 500)),
                                 Obsticale((settings.SCREEN_WIDTH + 800, 600)),
                                 Obsticale((settings.SCREEN_WIDTH + 1300, 700)),
                                 Obsticale((settings.SCREEN_WIDTH + 1200, 200)),
                                 Obsticale((settings.SCREEN_WIDTH + 1400, 400)))

power_ups = pygame.sprite.Group(Health((settings.SCREEN_WIDTH + 500, 200)),
                                Health((settings.SCREEN_WIDTH, 700)))



background = pygame.surface.Surface((screen_rect.width, screen_rect.height))
background.fill((120, 181, 250))
for y in range(settings.NUMTILES):
    for x in range(settings.NUMTILES):
        background.blit(water_full, (x * water_full_rect.width, y * water_full_rect.height))
        background.blit(sand_full, (x * sand_full_rect.width, 896))

mixer.init()
mixer.music.load("sounds/summer.mp3")
mixer.music.set_volume(0.3)
mixer.music.play()

font = pygame.font.Font(None, 80)
frame_count = 0
frame_rate = 60
start_time = 0

game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                fish.moving_up = True
            if event.key == pygame.K_DOWN:
                fish.moving_down = True
            if event.key == pygame.K_RIGHT:
                fish.moving_right = True
            if event.key == pygame.K_LEFT:
                fish.moving_left = True
        if event.type == pygame.KEYUP:
            fish.moving_up = False
            fish.moving_down = False
            fish.moving_right = False
            fish.moving_left = False
        if event.type == pygame.QUIT:
            sys.exit()

    fish.update(obsticales, power_ups)
    obsticales.update()
    power_ups.update(fish)
    screen.blit(background, (0, 0))
    total_seconds = frame_count // frame_rate
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    time_display = "{0:02}:{1:02}".format(minutes, seconds)
    fish.blitme()
    obsticales.draw(screen)
    power_ups.draw(screen)
    text = font.render(time_display, True, (227, 124, 7))
    screen.blit(text, (20, 20))
    total_seconds = start_time + (frame_count // frame_rate)
    frame_count += 1
    if total_seconds > 5:
        settings.OBSTICALE_SPEED = 8
    if total_seconds > 10:
        settings.OBSTICALE_SPEED = 11
    if total_seconds > 15:
        settings.OBSTICALE_SPEED = 14
    if total_seconds > 15:
        settings.OBSTICALE_SPEED = 14
    clock.tick(frame_rate)
    pygame.display.flip()