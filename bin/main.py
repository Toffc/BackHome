#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *
from config.settings import *
from src.plane import OurPlane  # 导入我们的飞机
from src.enemy import *
from src.game_stats import *
from src.scoreboard import *
from src.bullet import Bullet


def main():
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, stats)
    # 获取我方飞机
    our_plane = OurPlane(ai_settings.bg_size)
    # 响应音乐
    pygame.mixer.music.play(-1)  # loops 接收该参数, -1 表示无限循环(默认循环播放一次)
    running = True
    switch_image = False  # 切换飞机的标识位(使飞机具有喷气式效果)
    delay = 60  # 对一些效果进行延迟, 效果更好一些

    enemies = pygame.sprite.Group()  # 生成敌方飞机组(一种精灵组用以存储所有敌机精灵)
    small_enemies = pygame.sprite.Group()  # 敌方小型飞机组(不同型号敌机创建不同的精灵组来存储)
    mid_enemies = pygame.sprite.Group()  # 敌方中型飞机组(不同型号敌机创建不同的精灵组来存储)
    big_enemies = pygame.sprite.Group()  # 敌方大型飞机组(不同型号敌机创建不同的精灵组来存储)

    add_small_enemies(small_enemies, enemies, 6,
                      ai_settings.bg_size)  # 生成若干敌方小型飞机
    add_mid_enemies(mid_enemies, enemies, 3, ai_settings.bg_size)  # 生成若干敌方小型飞机
    add_big_enemies(big_enemies, enemies, 2, ai_settings.bg_size)  # 生成若干敌方小型飞机

    # 定义子弹, 各种敌机和我方敌机的毁坏图像索引
    bullet_index = 0
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0

    # 定义子弹实例化个数
    bullet1 = []
    bullet_num = 6
    for i in range(bullet_num):
        bullet1.append(Bullet(our_plane.rect.midtop))

    while running:

        # 绘制背景图
        ai_settings.screen.blit(ai_settings.background, (0, 0))
        sb.show_score()

        # 微信的飞机貌似是喷气式的, 那么这个就涉及到一个帧数的问题
        clock = pygame.time.Clock()
        clock.tick(60)

        # 绘制我方飞机的两种不同的形式
        if not delay % 3:
            switch_image = not switch_image

        for each in small_enemies:
            if each.active:
                # 随机循环输出小飞机敌机
                each.move()
                ai_settings.screen.blit(each.image, each.rect)

                pygame.draw.line(ai_settings.screen, ai_settings.color_black,
                                 (each.rect.left, each.rect.top - 5),
                                 (each.rect.right, each.rect.top - 5),
                                 2)
                energy_remain = each.energy / SmallEnemy.energy
                if energy_remain > 0.2:  # 如果血量大约百分之二十则为绿色，否则为红色
                    energy_color = ai_settings.color_green
                else:
                    energy_color = ai_settings.color_red
                pygame.draw.line(ai_settings.screen, energy_color,
                                 (each.rect.left, each.rect.top - 5),
                                 (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5),
                                 2)
            else:
                if e1_destroy_index == 0:
                    enemy1_down_sound.play()
                ai_settings.screen.blit(
                    each.destroy_images[e1_destroy_index], each.rect)
                e1_destroy_index = (e1_destroy_index + 1) % 4
                if e1_destroy_index == 0:
                    each.reset()

        for each in mid_enemies:
            if each.active:
                # 随机循环输出小飞机敌机
                each.move()
                ai_settings.screen.blit(each.image, each.rect)

                pygame.draw.line(ai_settings.screen, ai_settings.color_black,
                                 (each.rect.left, each.rect.top - 5),
                                 (each.rect.right, each.rect.top - 5),
                                 2)
                energy_remain = each.energy / MidEnemy.energy
                if energy_remain > 0.2:  # 如果血量大约百分之二十则为绿色，否则为红色
                    energy_color = ai_settings.color_green
                else:
                    energy_color = ai_settings.color_red
                pygame.draw.line(ai_settings.screen, energy_color,
                                 (each.rect.left, each.rect.top - 5),
                                 (each.rect.left + each.rect.width *
                                  energy_remain, each.rect.top - 5),
                                 2)
            else:
                if e2_destroy_index == 0:
                    enemy2_down_sound.play()
                ai_settings.screen.blit(
                    each.destroy_images[e2_destroy_index], each.rect)
                e2_destroy_index = (e2_destroy_index + 1) % 2
                if e2_destroy_index == 0:
                    each.reset()

        for each in big_enemies:
            if each.active:
                # 随机循环输出小飞机敌机
                each.move()
                ai_settings.screen.blit(each.image, each.rect)

                pygame.draw.line(ai_settings.screen, ai_settings.color_black,
                                 (each.rect.left, each.rect.top - 5),
                                 (each.rect.right, each.rect.top - 5),
                                 2)
                energy_remain = each.energy / BigEnemy.energy
                if energy_remain > 0.2:  # 如果血量大约百分之二十则为绿色，否则为红色
                    energy_color = ai_settings.color_green
                else:
                    energy_color = ai_settings.color_red
                pygame.draw.line(ai_settings.screen, energy_color,
                                 (each.rect.left, each.rect.top - 5),
                                 (each.rect.left + each.rect.width *
                                  energy_remain, each.rect.top - 5),
                                 2)
            else:
                if e3_destroy_index == 0:
                    enemy3_down_sound.play()
                ai_settings.screen.blit(
                    each.destroy_images[e3_destroy_index], each.rect)
                e3_destroy_index = (e3_destroy_index + 1) % 1
                if e3_destroy_index == 0:
                    each.reset()

        # 当我方飞机存活状态, 正常展示
        if our_plane.active:
            if switch_image:
                ai_settings.screen.blit(our_plane.image_one, our_plane.rect)
            else:
                ai_settings.screen.blit(our_plane.image_two, our_plane.rect)

            # 飞机存活的状态下才可以发射子弹
            if not (delay % 10):  # 每十帧发射一颗移动的子弹
                bullet_sound.play()
                bullets = bullet1
                bullets[bullet_index].reset(our_plane.rect.midtop)
                bullet_index = (bullet_index + 1) % bullet_num

            for b in bullets:
                if b.active:  # 只有激活的子弹才可能击中敌机
                    b.move()
                    ai_settings.screen.blit(b.image, b.rect)
                    enemies_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemies_hit:  # 如果子弹击中飞机
                        b.active = False  # 子弹损毁
                        for e in enemies_hit:
                            e.active = e.reduce_energy()  # 小型敌机损毁

        # 毁坏状态绘制爆炸的场面
        else:
            if not (delay % 3):
                ai_settings.screen.blit(
                    our_plane.destroy_images[me_destroy_index], our_plane.rect)
                me_destroy_index = (me_destroy_index + 1) % 4
                if me_destroy_index == 0:
                    me_down_sound.play()
                    our_plane.reset()

        # 调用 pygame 实现的碰撞方法 spritecollide (我方飞机如果和敌机碰撞, 更改飞机的存活属性)
        enemies_down = pygame.sprite.spritecollide(our_plane, enemies, False, pygame.sprite.collide_mask)
        if enemies_down:
            our_plane.active = False
            for row in enemies:
                row.active = False

        # 响应用户的操作
        for event in pygame.event.get():
            if event.type == 12:  # 如果用户按下屏幕上的关闭按钮，触发QUIT事件，程序退出
                pygame.quit()
                sys.exit()

        if delay == 0:
            delay = 60
        delay -= 1

        # 获得用户所有的键盘输入序列(如果用户通过键盘发出“向上”的指令,其他类似)
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            our_plane.move_up()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            our_plane.move_down()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            our_plane.move_left()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            our_plane.move_right()

        # 绘制图像并输出到屏幕上面
        pygame.display.flip()



