import pygame
import random
import threading
from random import randint
from src.bullet import enhance_bullet
from src.plane import OurPlane
from src.scoreboard import *
from src.game_stats import *
class Props(pygame.sprite.Sprite):

    def __init__(self, bg_size):
        super(Props, self).__init__()
        self.image = pygame.image.load("material\image\props0.png")
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 5
        self.rect.left, self.rect.top = (
            randint(0, self.width - self.rect.width),  randint(-5 * self.rect.height, -5),
        )
        self.active = True
        self.is_add_life = 0

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width), randint(-5 * self.rect.height, 0))
        self.active = True



class Props_bullet(Props):

    def __init__(self, bg_size):
        super(Props_bullet, self).__init__(bg_size)
        self.image = pygame.image.load('material/image/props1.png')

    def gain(self, our_plane):
        our_plane.bullet = enhance_bullet(our_plane.rect.midtop)
        return our_plane

class Props_plane_speed(Props):

    def __init__(self, bg_size):
        super(Props_plane_speed, self).__init__(bg_size)
        self.image = pygame.image.load('material/image/props2.png')

    def gain(self, our_plane):
        our_plane.speed = 20
        return our_plane

class Props_plane_add_life(Props):

    def __init__(self, bg_size):
        super(Props_plane_add_life, self).__init__(bg_size)
        self.image = pygame.image.load('material/image/props3.png')
        self.is_add_life = 1

    def gain(self, our_plane):
        if our_plane.life < 5:
            our_plane.life += 1
        return our_plane


'''
能量暂时保留
#
class Props_plane_energy(Props):

    def __init__(self, position, our_plane):
        super(Props_plan_energy, self).__init__(self, position, our_plane)
        self.image = pygame.image.load('material/image/props4.png')

    def gain(self):
        our_plane.energy += 1
#
'''
def add_props_bullet(group1, group2, num, bg_size):
    """
    添加子弹增强道具
    """
    for i in range(num):
        props_bullet = Props_bullet(bg_size)
        group1.add(props_bullet)
        group2.add(props_bullet)

def add_props_plane_speed(group1, group2, num, bg_size):
    """
    添加飞机加速道具
    """
    for i in range(num):
        props_plane_speed = Props_plane_speed(bg_size)
        group1.add(props_plane_speed)
        group2.add(props_plane_speed)

def add_props_plane_add_life(group1, group2, num, bg_size):
    """
    添加飞机增加生命道具
    """
    for i in range(num):
        props_plane_add_life = Props_plane_add_life(bg_size)
        group1.add(props_plane_add_life)
        group2.add(props_plane_add_life)

