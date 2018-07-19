from random import randint
import pygame
from src.bullet import *


class random_bullet(pygame.sprite.Sprite):
    """
    定义弹幕
    """

    def __init__(self, bg_size):
        super(random_bullet, self).__init__()
        self.image = pygame.image.load('material/image/bullet2.png')
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.mask = pygame.mask.from_surface(
            self.image)  # 获取图像的掩膜用以更加精确的碰撞检测
        self.speed = 1
        # 定义子弹出现的位置, 保证子弹不会在程序已开始就立即出现
        self.rect.left, self.rect.top = (
            randint(0, self.width - self.rect.width),  randint(-5 *
                                                               self.rect.height, -5),
        )
        self.active = True

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        """
        当子弹向下移动出屏幕或子弹失效
        :return:
        """
        self.rect.left, self.rect.top = (
            randint(5, self.width - self.rect.width), randint(-5 * self.rect.height, 0))
        self.active = True


def add_random_bullet(group1, group2, num, bg_size):
    """
    添加弹幕
    :return:
    """
    for i in range(num):
        random_bullets = random_bullet(bg_size)
        group1.add(random_bullets)
        group2.add(random_bullets)
