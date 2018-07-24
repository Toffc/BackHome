#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    定义敌机
"""

from random import randint
import pygame
from src.bullet import enemy_bullet

class SmallEnemy(pygame.sprite.Sprite):
    """
    定义小飞机敌人
    """
    energy = 2

    def __init__(self, bg_size):
        super(SmallEnemy, self).__init__()
        self.image = pygame.image.load("material\image\enemy1.png")
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.mask = pygame.mask.from_surface(self.image)  # 获取飞机图像的掩膜用以更加精确的碰撞检测
        self.speed = 2
        self.energy = SmallEnemy.energy
        # 定义敌机出现的位置, 保证敌机不会在程序已开始就立即出现
        self.rect.left, self.rect.top = (
            randint(0, self.width - self.rect.width),  randint(-5 * self.rect.height, -5),
        )
        self.active = True
        # 加载飞机损毁图片
        self.destroy_images = []
        self.destroy_images.extend(
            [
                pygame.image.load("material/image/enemy1_down1.png"),
                pygame.image.load("material/image/enemy1_down2.png")
            ]
        )
        self.bullet = enemy_bullet(self.rect.midtop)
        #加入发射子弹的时间
        self.time = randint(0, 80)
        
    def get_Time(self):
        return self.time

    def add_Time(self):
        self.time += 1
        self.time = self.time % 81

    def move(self):
        """
        定义敌机的移动函数
        :return:
        """
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        """
        当敌机向下移动出屏幕且飞机是需要进行随机出现的, 以及敌机死亡
        :return:
        """
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width), randint(-5 * self.rect.height, 0))
        self.active = True
        self.energy = 2

    def reduce_energy(self):
        self.energy = self.energy - 1
        if self.energy <= 0:
            return False
        else:
            return True


class MidEnemy(pygame.sprite.Sprite):

    energy = 5

    def __init__(self, bg_size):
        super(MidEnemy, self).__init__()
        self.image = pygame.image.load("material/image/enemy2.png")
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.mask = pygame.mask.from_surface(self.image)  # 获取飞机图像的掩膜用以更加精确的碰撞检测
        self.speed = 1
        self.energy = MidEnemy.energy
        # 定义敌机出现的位置, 保证敌机不会在程序已开始就立即出现
        self.rect.left, self.rect.top = (
            randint(10, self.width - self.rect.width),  randint(-5 *
                                                               self.rect.height, -5),
        )
        self.active = True
        # 加载飞机损毁图片
        self.destroy_images = []
        self.destroy_images.extend(
            [
                pygame.image.load("material/image/enemy2_down1.png"),
                pygame.image.load("material/image/enemy2_down2.png")
            ]
        )
        self.bullet = enemy_bullet(self.rect.midtop)
        #加入发射子弹的时间
        self.time = randint(0, 60)
    
    def get_Time(self):
        return self.time

    def add_Time(self):
        self.time += 1
        self.time = self.time % 61

    def move(self):
        """
        定义敌机的移动函数
        :return:
        """
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        """
        当敌机向下移动出屏幕且飞机是需要进行随机出现的, 以及敌机死亡
        :return:
        """
        self.rect.left, self.rect.top = (
            randint(10, self.width - self.rect.width), randint(-5 * self.rect.height, 0))
        self.active = True
        self.energy = 5

    def reduce_energy(self):
        self.energy = self.energy - 1
        if self.energy <= 0:
            return False
        else:
            return True

class BigEnemy(pygame.sprite.Sprite):

    energy = 10

    def __init__(self, bg_size):
        super(BigEnemy, self).__init__()
        self.image = pygame.image.load("material\image\enemy3.png")
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.mask = pygame.mask.from_surface(self.image)  # 获取飞机图像的掩膜用以更加精确的碰撞检测
        self.speed = 1
        self.energy = BigEnemy.energy
        # 定义敌机出现的位置, 保证敌机不会在程序已开始就立即出现
        self.rect.left, self.rect.top = (
            randint(10, self.width - self.rect.width),  randint(-5 *
                                                               self.rect.height, -5),
        )
        self.active = True
        # 加载飞机损毁图片
        self.destroy_images = []
        self.destroy_images.extend(
            [
                pygame.image.load("material/image/enemy3_down1.png"),
                pygame.image.load("material/image/enemy3_down2.png")
            ]
        )
        self.bullet = enemy_bullet(self.rect.midtop)
        #加入发射子弹的时间
        self.time = randint(0, 50)

    def get_Time(self):
        return self.time

    def add_Time(self):
        self.time += 1
        self.time = self.time % 51

    def move(self):
        """
        定义敌机的移动函数
        :return:
        """
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        """
        当敌机向下移动出屏幕且飞机是需要进行随机出现的, 以及敌机死亡
        :return:
        """
        self.rect.left, self.rect.top = (
            randint(10, self.width - self.rect.width), randint(-5 * self.rect.height, 0))
        self.active = True
        self.energy = 10

    def reduce_energy(self):
        self.energy = self.energy - 1
        if self.energy <= 0:
            return False
        else:
            return True


def add_small_enemies(group1, group2, num, bg_size):
    """
    添加小型敌机
    指定个敌机对象添加到精灵组（sprite.group）
    参数group1、group2是两个精灵组类型的形参，用以存储多个精灵对象（敌机）。
    需要注意的一点是group既然是特定的精灵组结构体，在向其内部添加精灵对象时需要调用其对应的成员函数add()
    :return:
    """
    for i in range(num):
        small_enemy = SmallEnemy(bg_size)
        group1.add(small_enemy)
        group2.add(small_enemy)


def add_mid_enemies(group1, group2, num, bg_size):
    """
    添加中型敌机
    指定个敌机对象添加到精灵组（sprite.group）
    参数group1、group2是两个精灵组类型的形参，用以存储多个精灵对象（敌机）。
    需要注意的一点是group既然是特定的精灵组结构体，在向其内部添加精灵对象时需要调用其对应的成员函数add()
    :return:
    """
    for i in range(num):
        mid_enemy = MidEnemy(bg_size)
        group1.add(mid_enemy)
        group2.add(mid_enemy)


def add_big_enemies(group1, group2, num, bg_size):
    """
    添加大型敌机
    指定个敌机对象添加到精灵组（sprite.group）
    参数group1、group2是两个精灵组类型的形参，用以存储多个精灵对象（敌机）。
    需要注意的一点是group既然是特定的精灵组结构体，在向其内部添加精灵对象时需要调用其对应的成员函数add()
    :return:
    """
    for i in range(num):
        big_enemy = BigEnemy(bg_size)
        group1.add(big_enemy)
        group2.add(big_enemy)
