#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    子弹的实现
"""

import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Bullet, self).__init__()
        self.image = pygame.image.load('material/image/bullet1.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.rect.left -= 10
        self.rect.top -= 3
        self.speed = 30
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        """
        子弹移动, 超出屏幕范围, 则设置死亡
        :return:
        """
        if self.rect.top < 0:
            self.active = False
        else:
            self.rect.top -= self.speed

    def reset(self, position):
        """
        复位函数
        :param position:
        :return:
        """
        self.rect.left, self.rect.top = position
        self.rect.left -= 10
        self.rect.top -= 3
        self.active = True

class enemy_bullet(Bullet):

    def __init__(self, position):
        super().__init__(position)
        self.image = pygame.image.load('material/image/bullet2.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.rect.top += 20
        self.rect.left -= 24
        self.speed = 10
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        """
        子弹移动, 超出屏幕范围, 则设置死亡
        :return:
        """
        if self.rect.top < 0 or self.rect.top > 600:
            self.active = False
        else:
            self.rect.top += self.speed

    def reset(self, position):
        """
        复位函数
        :param position:
        :return:
        """
        self.rect.left, self.rect.top = position
        self.rect.top += 20
        self.rect.left -= 24
        self.active = True

class enhance_bullet(Bullet):

    def __init__(self, position):
        super().__init__(position)
        self.image = pygame.image.load('material/image/bullet3.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.rect.top -= 15
        self.rect.left -= 28
        self.speed = 35

    def reset(self, position):
        """
        复位函数
        :param position:
        :return:
        """
        self.rect.left, self.rect.top = position
        self.rect.top -= 15
        self.rect.left -= 28
        self.active = True
