import pygame
from os import path
from sys import exit
from time import sleep
from random import choice
from itertools import product
from pygame.locals import QUIT, KEYDOWN
 
 
def direction_check(moving_direction, change_direction):
  directions = [['up', 'down'], ['left', 'right']]
  if moving_direction in directions[0] and change_direction in directions[1]:
    return change_direction
  elif moving_direction in directions[1] and change_direction in directions[0]:
    return change_direction
  return moving_direction
 
 
class Snake:
 
  colors = list(product([0, 64, 128, 192, 255], repeat=3))[1:-1]
 
  def __init__(self):
    self.map = {(x, y): 0 for x in range(32) for y in range(24)}
    self.body = [[100, 100], [120, 100], [140, 100]]
    self.head = [140, 100]
    self.food = []
    self.food_color = []
    self.moving_direction = 'right'
    self.speed = 4
    self.generate_food()
    self.game_started = False
 
  def check_game_status(self):
    if self.body.count(self.head) > 1:
      return True
    if self.head[0] < 0 or self.head[0] > 620 or self.head[1] < 0 or self.head[1] > 460:
      return True
    return False
 
  def move_head(self):
    moves = {
      'right': (20, 0),
      'up': (0, -20),
      'down': (0, 20),
      'left': (-20, 0)
    }
    step = moves[self.moving_direction]
    self.head[0] += step[0]
    self.head[1] += step[1]
 
  def generate_food(self):
    self.speed = len(self.body) // 16 if len(self.body) // 16 > 4 else self.speed
    for seg in self.body:
      x, y = seg
      self.map[x//20, y//20] = 1
    empty_pos = [pos for pos in self.map.keys() if not self.map[pos]]
    result = choice(empty_pos)
    self.food_color = list(choice(self.colors))
    self.food = [result[0]*20, result[1]*20]
 
 
def main():
  key_direction_dict = {
    119: 'up', # W
    115: 'down', # S
    97: 'left', # A
    100: 'right', # D
    273: 'up', # UP
    274: 'down', # DOWN
    276: 'left', # LEFT
    275: 'right', # RIGHT
  }
 
  fps_clock = pygame.time.Clock()
  pygame.init()
  pygame.mixer.init()
  snake = Snake()
  sound = False
  if path.exists('eat.wav'):
    sound_wav = pygame.mixer.Sound("eat.wav")
    sound = True
  title_font = pygame.font.SysFont('arial', 32)
  welcome_words = title_font.render('Welcome to My Snake', True, (0, 0, 0), (255, 255, 255))
  tips_font = pygame.font.SysFont('arial', 24)
  start_game_words = tips_font.render('Click to Start Game', True, (0, 0, 0), (255, 255, 255))
  close_game_words = tips_font.render('Press ESC to Close', True, (0, 0, 0), (255, 255, 255))
  gameover_words = title_font.render('GAME OVER', True, (205, 92, 92), (255, 255, 255))
  win_words = title_font.render('THE SNAKE IS LONG ENOUGH AND YOU WIN!', True, (0, 0, 205), (255, 255, 255))
  screen = pygame.display.set_mode((640, 480), 0, 32)
  pygame.display.set_caption('My Snake')
  new_direction = snake.moving_direction
  while 1:
    for event in pygame.event.get():
      if event.type == QUIT:
        exit()
      elif event.type == KEYDOWN:
        if event.key == 27:
          exit()
        if snake.game_started and event.key in key_direction_dict:
          direction = key_direction_dict[event.key]
          new_direction = direction_check(snake.moving_direction, direction)
      elif (not snake.game_started) and event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if 213 <= x <= 422 and 304 <= y <= 342:
          snake.game_started = True
    screen.fill((255, 255, 255))
    if snake.game_started:
      snake.moving_direction = new_direction # 在这里赋值，而不是在event事件的循环中赋值，避免按键太快
      snake.move_head()
      snake.body.append(snake.head[:])
      if snake.head == snake.food:
        if sound:
          sound_wav.play()
        snake.generate_food()
      else:
        snake.body.pop(0)
      for seg in snake.body:
        pygame.draw.rect(screen, [0, 0, 0], [seg[0], seg[1], 20, 20], 0)
      pygame.draw.rect(screen, snake.food_color, [snake.food[0], snake.food[1], 20, 20], 0)
      if snake.check_game_status():
        screen.blit(gameover_words, (241, 310))
        pygame.display.update()
        snake = Snake()
        new_direction = snake.moving_direction
        sleep(3)
      elif len(snake.body) == 512:
        screen.blit(win_words, (33, 210))
        pygame.display.update()
        snake = Snake()
        new_direction = snake.moving_direction
        sleep(3)
    else:
      screen.blit(welcome_words, (188, 100))
      screen.blit(start_game_words, (236, 310))
      screen.blit(close_game_words, (233, 350))
    pygame.display.update()
    fps_clock.tick(snake.speed)
 
 
if __name__ == '__main__':
  main()