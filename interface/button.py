# -*- coding: utf-8 -*-
import pygame
from sys import exit

class Button(object):
    def __init__(self, upimage, downimage, screen, position):
        '''
        调用本按钮需要提供两幅图片
        position为图像出现的位置
        '''
        self.imageUp = pygame.image.load(upimage).convert_alpha()
        self.imageDown = pygame.image.load(downimage).convert_alpha()
        self.screen = screen
        self.position = position

    def isCover(self):
        point_x,point_y = pygame.mouse.get_pos()
        x, y = self. position
        w, h = self.imageUp.get_size()

        in_x = x - w/2 < point_x < x + w/2
        in_y = y - h/2 < point_y < y + h/2
        return in_x and in_y

    def show(self):
        w, h = self.imageUp.get_size()
        x, y = self.position
        
        if self.isCover():
            self.screen.blit(self.imageDown, (x-w/2,y-h/2))
        else:
            self.screen.blit(self.imageUp, (x-w/2, y-h/2))

