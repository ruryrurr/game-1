import pygame
import random
import sys
from pygame.locals import*
pygame.init()

screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w),
                          int(screen_info.current_h))

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
def main():
  pass


fish_image=pygame.image.load('fish.png')
fish_image=pygame.transform.smoothscale(fish_image, 80,80)
fish_rect=fish_image .get_rect()

fish_rect.center=(width//2, height//2)

speed = pygame. math.Vecter2(0,10)
rotate=random.randint(0,360)
speed.rotate_ip(rotate)
fish_image=pygame.transform.rotate(fish_ image,180, rotate)
def main():
  while True:
    clock.tick(60)
  for event in pygame.event.get():
    if event.type == QUIT:
      sys.exit()
    move_fish()
    screen.fill(0,127,245)
    screen.blit(fish_image,fish_rect)
    pygame.display.flip()



if __name__ == "__main__":
  main()
