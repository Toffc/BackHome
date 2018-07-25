#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    创建飞机
    在pygame中, 所有可移动的对象均叫可看作一个精灵(sprite)
    该类并实现了碰撞方法 spritecollide
z
    我方飞机和敌方飞机指定掩膜属性以及生存状态标志位 添加 self.mask 属性(可以实现更精准的碰撞效果)
"""
from config.settings import BASE_DIR
from random import randint
import sys 
sys.path.append('..')
from config.settings import *
import os
# 倒入精灵模块, 使飞机可以动起来
import pygame
import time
from src.bullet import Bullet

me_destroy_index = 0

class OurPlane(pygame.sprite.Sprite):

    def __init__(self, bg_size, screen):
        super(OurPlane, self).__init__()
        # 确定我方飞机背景图(有俩张，可以让它们不停的切换，形成动态效果)
        self.image_one = pygame.image.load(os.path.join(BASE_DIR, "material/image/hero1.png"))
        self.image_two = pygame.image.load(os.path.join(BASE_DIR, "material/image/hero2.png"))
        # 获取我方飞机的位置
        self.rect = self.image_one.get_rect()
        # 本地化背景图片的尺寸
        self.width, self.height = bg_size[0], bg_size[1]
        # 获取飞机图像的掩膜用以更加精确的碰撞检测
        self.mask = pygame.mask.from_surface(self.image_one)
        # 定义飞机初始化位置，底部预留60像素
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, (self.height - self.rect.height - 10)
        # 设置飞机移动速度
        self.speed = 10
        # 设置飞机存活状态(True为存活, False为死亡)
        self.active = True
        #设置飞机生命值
        self.life = 3
        # 加载飞机损毁图片
        self.destroy_images = []
        self.destroy_images.extend(
            [
                pygame.image.load(os.path.join(BASE_DIR, "material/image/hero_blowup_n1.png"))
            ]
        )
        self.bullets = []
        self.time = randint(0, 30)
        self.screen = screen
        self.bullet1 = []
        self.bullet_index = 0
        self.bullet_num = 5
        for i in range(self.bullet_num):
            self.bullets.append(Bullet(self.rect.midtop))
    
    def get_Time(self):
        return self.time

    def add_Time(self):
        self.time += 1
        self.time = self.time % 31

    def move_up(self):
        """
        飞机向上移动的操作函数，其余移动函数方法类似
        """
        if self.rect.top > 0:  # 如果飞机尚未移动出背景区域
            self.rect.top -= self.speed
        else:  # 若即将移动出背景区域，则及时纠正为背景边缘位置
            self.rect.top = 0

    def move_down(self):
        """
        飞机向下移动
        """
        if self.rect.bottom < self.height - 10:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 10

    def move_left(self):
        """
        飞机向左移动
        """
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def move_right(self):
        """
        飞机向右移动
        """
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        # 初始化飞机(飞机挂了, 初始化到初始位置)
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, (self.height - self.rect.height - 10)
        # 重置飞机的存活状态
        self.active = True
        #各项数值初始化
        self.speed = 10
        self.bullets = []
        for i in range(self.bullet_num):
            self.bullets.append(Bullet(self.rect.midtop))

    def display(self, delay):
        switch_image = True
        if not delay % 3:
            switch_image = not switch_image
        if switch_image:
            self.screen.blit(self.image_one, self.rect)
        else:
            self.screen.blit(self.image_two, self.rect)

    def fire(self, enemies):
        if self.time == 30:  #限定飞机发射子弹的间隔
            bullet_sound.play()
            self.bullet1 = self.bullets
            self.bullet1[self.bullet_index].reset(self.rect.midtop)
            self.bullet_index = (self.bullet_index + 1) % self.bullet_num
        self.add_Time()
        return self.bullet1

    def destroy(self, delay):
        global me_destroy_index
        me_down_sound.play()
        for i in range(1):
            time.sleep(0.02)
            self.screen.blit(self.destroy_images[i], self.rect)
        self.reset()
       
