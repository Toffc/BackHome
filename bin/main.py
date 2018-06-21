#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
import time 
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
    num_small = 6
    num_mid = 3
    num_big = 2

    enemies = pygame.sprite.Group()  # 生成敌方飞机组(一种精灵组用以存储所有敌机精灵)
    small_enemies = pygame.sprite.Group()  # 敌方小型飞机组(不同型号敌机创建不同的精灵组来存储)
    mid_enemies = pygame.sprite.Group()  # 敌方中型飞机组(不同型号敌机创建不同的精灵组来存储)
    big_enemies = pygame.sprite.Group()  # 敌方大型飞机组(不同型号敌机创建不同的精灵组来存储)

    add_small_enemies(small_enemies, enemies, num_small,
                      ai_settings.bg_size)  # 生成若干敌方小型飞机
    add_mid_enemies(mid_enemies, enemies, num_mid, ai_settings.bg_size)  # 生成若干敌方小型飞机
    add_big_enemies(big_enemies, enemies, num_big, ai_settings.bg_size)  # 生成若干敌方小型飞机

    # 定义子弹, 各种敌机和我方敌机的毁坏图像索引
    bullet_index = 0
    bullet_index_enemy = 0
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0

    # 定义子弹实例化个数
    bullet1 = []
    bullet_num = 1
    for i in range(bullet_num):
        bullet1.append(Bullet(our_plane.rect.midtop))

    #敌机的子弹
    bullet2 = []
    small_bullet_num = 1
    mid_bullet_num = 1
    big_bullet_num = 1 
    for small in small_enemies:
        for i in range(small_bullet_num):
            bullet2.append(Bullet(small.rect.midtop))
    for mid in mid_enemies:
        for i in range(mid_bullet_num):
            bullet2.append(Bullet(mid.rect.midtop))
    for big in big_enemies:
        for i in range(big_bullet_num):
            bullet2.append(Bullet(big.rect.midtop))   
    bullet_num2 = len(bullet2)
    

    while running:

        # 绘制背景图
        ai_settings.screen.blit(ai_settings.background, (0, 0))
        sb.show_score()
        sb.show_life()

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
                enemy1_down_sound.play()
                stats.add_score(50)
                sb.prep_score()
                for i in range(4):
                    time.sleep(0.02)
                    ai_settings.screen.blit(
                        each.destroy_images[i], each.rect)
                each.reset()

        for each in mid_enemies:
            if each.active:
                # 随机循环输出中飞机敌机
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
                enemy2_down_sound.play()
                stats.add_score(100)
                sb.prep_score()
                for i in range(5):
                    time.sleep(0.02)
                    ai_settings.screen.blit(
                        each.destroy_images[i], each.rect)
                each.reset()

        for each in big_enemies:
            if each.active:
                # 随机循环输出大飞机敌机
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
                #更新得分
                stats.add_score(200)
                sb.prep_score()
                for i in range(7):
                    time.sleep(0.02)
                    ai_settings.screen.blit(
                        each.destroy_images[i], each.rect)
                each.reset()

        #敌机发射子弹
        for small in small_enemies:
            if not (delay % 30):  # 每十帧发射一颗移动的子弹
                #bullet_sound.play()
                bullets = bullet2
                bullets[bullet_index_enemy].reset(small.rect.midtop)
                bullet_index_enemy = (bullet_index_enemy + 1) % bullet_num2

        for mid in mid_enemies:
            if not (delay % 30):  # 每十帧发射一颗移动的子弹
                #bullet_sound.play()
                bullets = bullet2
                bullets[bullet_index_enemy].reset(mid.rect.midtop)
                bullet_index_enemy = (bullet_index_enemy + 1) % bullet_num2

        for big in big_enemies:
            if not (delay % 30):  # 每十帧发射一颗移动的子弹
                #bullet_sound.play()
                bullets = bullet2
                bullets[bullet_index_enemy].reset(big.rect.midtop)
                bullet_index_enemy = (bullet_index_enemy + 1) % bullet_num2
        
        for b in bullet2:
            if b.active:  # 只有激活的子弹才可能击中飞机
                b.move_enemy()
                ai_settings.screen.blit(b.image, b.rect)

        # 当我方飞机存活状态, 正常展示
        if our_plane.active:
            if switch_image:
                ai_settings.screen.blit(our_plane.image_one, our_plane.rect)
            else:
                ai_settings.screen.blit(our_plane.image_two, our_plane.rect)

            # 飞机存活的状态下才可以发射子弹
            if not (delay % 20):  # 每十帧发射一颗移动的子弹
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
            me_down_sound.play()
            for i in range(4):
                time.sleep(0.02)
                ai_settings.screen.blit(
                    our_plane.destroy_images[i], our_plane.rect)
            stats.sub_life()
            sb.prep_life()    
            our_plane.reset()

        # 调用 pygame 实现的碰撞方法 spritecollide (我方飞机如果和敌机碰撞, 更改飞机的存活属性)
        enemies_down = pygame.sprite.spritecollide(our_plane, enemies, False, pygame.sprite.collide_mask)
        if enemies_down:
            our_plane.active = False
            for row in enemies_down:
                row.active = False
                
        # 调用 pygame 实现的碰撞方法 spritecollide (我方飞机如果和子弹碰撞, 更改飞机的存活属性)
        hit = pygame.sprite.spritecollide(our_plane, bullet2, False, pygame.sprite.collide_mask)
        if hit:  # 如果子弹击中飞机
            our_plane.active = False  # 子弹损毁
            for b in hit:
                b.active = False  # 飞机损毁

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




