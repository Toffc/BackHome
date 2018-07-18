#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pygame



class Settings():
    def __init__(self):

        pygame.init()  # 游戏初始化
              
        self.bg_size = 1080, 600  # 初始化游戏背景大小(宽, 高)
        self.screen = pygame.display.set_mode(self.bg_size)  # 设置背景对话框
        pygame.display.set_caption("飞机大战")  # 设置标题
        self.background = pygame.image.load(os.path.join(
            BASE_DIR, "material/image/background.png"))  # 加载背景图片,并设置为不透明
        
        # 血槽颜色绘制
        self.color_black = (0, 0, 0)
        self.color_green = (0, 255, 0)
        self.color_red = (255, 0, 0)
        self.color_white = (255, 255, 255)
        self.bg_color = (200, 200, 200)

class MyMap(pygame.sprite.Sprite):
    
    def __init__(self,x,y, background, length):
        self.x = x
        self.y = y
        self.bg = background.convert_alpha()
        self.length = length

    def map_rolling(self):
        if self.y > self.length:
            self.y = -self.length
        else:
            self.y +=5
    def map_update(self, screen):
        screen.blit(self.bg, (self.x,self.y))
    def set_pos(x,y):
        self.x =x
        self.y =y

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pygame.mixer.init()  # 混音器初始化
# 游戏背景音乐
pygame.mixer.music.load(os.path.join(BASE_DIR, "material/sound/game_music.wav"))
pygame.mixer.music.set_volume(0.2)

# 子弹发射音乐
bullet_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "material/sound/bullet.wav"))
bullet_sound.set_volume(0.2)

# 我方飞机挂了的音乐
me_down_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "material/sound/game_over.wav"))
me_down_sound.set_volume(0.2)

# 敌方飞机挂了的音乐
enemy1_down_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "material/sound/enemy1_down.wav"))
enemy1_down_sound.set_volume(0.2)

enemy2_down_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "material/sound/enemy2_down.wav"))
enemy2_down_sound.set_volume(0.2)

enemy3_down_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "material/sound/enemy3_down.wav"))
enemy3_down_sound.set_volume(0.2)

button_down_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "material/sound/button.wav"))
button_down_sound.set_volume(0.2)

level_up_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "material/sound/achievement.wav"))
level_up_sound.set_volume(0.2)

bomb_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "material/sound/use_bomb.wav"))
bomb_sound.set_volume(0.2)

get_bomb_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "material/sound/get_bomb.wav"))
get_bomb_sound.set_volume(0.2)

get_bullet_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "material/sound/get_double_laser.wav"))
get_bullet_sound.set_volume(0.2)

big_enemy_flying_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "material/sound/big_spaceship_flying.wav"))
big_enemy_flying_sound.set_volume(0.2)

