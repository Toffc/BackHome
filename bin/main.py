#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
import time
import random 
from bin.endless import *
from pygame.locals import *
from config.settings import *
from src.plane import OurPlane  # 导入我们的飞机
from src.enemy import *
from src.game_stats import *
from src.scoreboard import *
from src.bullet import *
from src.props import *
from interface.ui import *
from interface.function import *
from src.random_bullet import *


def main():
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, stats)

    bg1 = MyMap(0,0, ai_settings.background, 600)
    bg2 = MyMap(0,600, ai_settings.background, 600)

    #添加主界面类以及界面背景加载
    ui_back = pygame.image.load(os.path.join(
            BASE_DIR, "material/image/background.png"))
    ui = Ui(ai_settings, stats)

    # 获取我方飞机
    our_plane = OurPlane(ai_settings.bg_size, ai_settings.screen)
    # 响应音乐
    pygame.mixer.music.play(-1)  # loops 接收该参数, -1 表示无限循环(默认循环播放一次)
    running = True
    switch_image = False  # 切换飞机的标识位(使飞机具有喷气式效果)
    delay = 60  # 对一些效果进行延迟, 效果更好一些
    num_small = 6
    num_mid = 3
    num_big = 2

    enemies = pygame.sprite.Group()  # 生成敌方飞机组(一种精灵组用以存储所有敌机精灵)
    small_enemies = pygame.sprite.Group()  # 敌方小型飞机组(不同型号敌机创建不同的精灵组来存储)
    mid_enemies = pygame.sprite.Group()  # 敌方中型飞机组(不同型号敌机创建不同的精灵组来存储)
    big_enemies = pygame.sprite.Group()  # 敌方大型飞机组(不同型号敌机创建不同的精灵组来存储)

    #生成道具组
    props = pygame.sprite.Group()
    props_bullet = pygame.sprite.Group()
    props_plane_speed = pygame.sprite.Group()
    props_plane_add_life = pygame.sprite.Group()

    

    #生成道具
    add_props_bullet(props_bullet, props, 1, ai_settings.bg_size)
    add_props_plane_speed(props_plane_speed, props, 1, ai_settings.bg_size)
    add_props_plane_add_life(props_plane_add_life, props, 1, ai_settings.bg_size)

    
    #生成敌机
    add_small_enemies(small_enemies, enemies, num_small, ai_settings.bg_size)  # 生成若干敌方小型飞机
    add_mid_enemies(mid_enemies, enemies, num_mid, ai_settings.bg_size)  # 生成若干敌方小型飞机
    add_big_enemies(big_enemies, enemies, num_big, ai_settings.bg_size)  # 生成若干敌方小型飞机

    # 定义各种子弹索引
    bullet_index = 0
    bullet_index_small = 0
    bullet_index_mid = 0
    bullet_index_big = 0

    # 定义飞机子弹实例化个数
    bullet_num = 1

    #敌机的子弹
    small_bullet = []
    mid_bullet = []
    big_bullet = []

    #定义敌机子弹实例化个数
    small_bullet_num = 1
    mid_bullet_num = 1
    big_bullet_num = 1


    for small in small_enemies:
        for i in range(small_bullet_num):
            small_bullet.append(small.bullet)
    for mid in mid_enemies:
        for i in range(mid_bullet_num):
            mid_bullet.append(mid.bullet)
    for big in big_enemies:
        for i in range(big_bullet_num):
            big_bullet.append(big.bullet)

    small_bullet_all = len(small_bullet)
    mid_bullet_all = len(mid_bullet)
    big_bullet_all = len(big_bullet)
    
    #计时变量    
    time_counter = 0

    
    '''
    开始界面
    '''
    while 1:
        ai_settings.screen.blit(ui_back, (0, 0))
        ui.show(ai_settings, stats)
        if stats.function == 1:
            f1(ai_settings, ui_back, stats)
            if stats.mode != 0:
                break
        elif stats.function == 2:
            f2(ai_settings, ui_back, stats)
        elif stats.function == 3:
            f3(ai_settings, ui_back, stats, v)
        elif stats.function == 4:
            f4(ai_settings, ui_back, stats)
        pygame.display.update()
    


    '''
    游戏界面
    '''
    if stats.mode == 2:
        endless()
    elif stats.mode == 1:
        endless()