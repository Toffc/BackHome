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
from src.bullet import *
from src.props import *
from interface.ui import *
from interface.running_ui import *
from src.random_bullet import *


def endless():
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, stats)

    bg1 = MyMap(0,0, ai_settings.background, 600)
    bg2 = MyMap(0,600, ai_settings.background, 600)

    #添加暂停类
    plane_ui = Running(ai_settings, stats)

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
    飞机大战
    '''

    while running:

        # 响应用户的操作
        for event in pygame.event.get():
            if event.type == 12:  # 如果用户按下屏幕上的关闭按钮，触发QUIT事件，程序退出
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and plane_ui.button_stop.isCover() and stats.pause == True:
                stats.pause = False
            elif event.type == pygame.MOUSEBUTTONDOWN and plane_ui.button_stop.isCover() and stats.pause == False:
                stats.pause = True
            elif event.type == pygame.MOUSEBUTTONDOWN and plane_ui.button_back_menu.isCover() and stats.back_menu == False:
                stats.back_menu = True

        if stats.back_menu == True:
            return
        if stats.pause == True:
            continue

        # 绘制背景图
        #ai_settings.screen.blit(ai_settings.background, (0, 0))
        bg1.map_update(ai_settings.screen)
        bg2.map_update(ai_settings.screen)
        bg1.map_rolling()
        bg2.map_rolling()

        #show pause button
        plane_ui.show(ai_settings, stats)

        #显示分数、时间
        sb.show_score()
        sb.prep_time()

        # 计时
        time_counter += 1
        if(time_counter == 50):
            time_counter = 0
            stats.add_time()
            sb.prep_time()

        # 微信的飞机貌似是喷气式的, 那么这个就涉及到一个帧数的问题
        clock = pygame.time.Clock()
        clock.tick(60)

        # 绘制我方飞机的两种不同的形式
        #if not delay % 3:
        #    switch_image = not switch_image

        ''' 绘制敌机 '''

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
                for i in range(2):
                    time.sleep(0.02)
                    ai_settings.screen.blit(
                        each.destroy_images[i], each.rect)
                each.reset()

        #在不同时间段增加敌机类型
        if stats.getTime() >= 310:
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
                    for i in range(2):
                        time.sleep(0.02)
                        ai_settings.screen.blit(
                            each.destroy_images[i], each.rect)
                    each.reset()

        #在不同时间段增加敌机类型
        if stats.getTime() >= 380: 
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
                    enemy3_down_sound.play()
                    #更新得分
                    stats.add_score(200)
                    sb.prep_score()
                    for i in range(2):
                        time.sleep(0.02)
                        ai_settings.screen.blit(
                            each.destroy_images[i], each.rect)
                    each.reset()

        for b in small_bullet:
            if b.active:  # 只有激活的子弹才可能击中飞机
                b.move()
                ai_settings.screen.blit(b.image, b.rect)

        for b in mid_bullet:
            if b.active:  # 只有激活的子弹才可能击中飞机
                b.move()
                ai_settings.screen.blit(b.image, b.rect)
        
        for b in big_bullet:
            if b.active:  # 只有激活的子弹才可能击中飞机
                b.move()
                ai_settings.screen.blit(b.image, b.rect)

        #敌机发射子弹
        for small in small_enemies:
            if small.get_Time() == 80:  # 敌机内置时间达到指定值，发射子弹
                bullets = small_bullet
                bullets[bullet_index_small].reset(small.rect.midtop)
                bullet_index_small = (
                    bullet_index_small + 1) % small_bullet_all
            small.add_Time()

        for mid in mid_enemies:
            if mid.get_Time() == 60:  #  敌机内置时间达到指定值，发射子弹
                bullets = mid_bullet
                bullets[bullet_index_mid].reset(mid.rect.midtop)
                bullet_index_mid = (bullet_index_mid + 1) % mid_bullet_all
            mid.add_Time()

        for big in big_enemies:
            if big.get_Time() == 50:  # 敌机内置时间达到指定值，发射子弹
                bullets = big_bullet
                bullets[bullet_index_big].reset(big.rect.midtop)
                bullet_index_big = (bullet_index_big + 1) % big_bullet_all
            big.add_Time()

        """
        随机添加道具
        """
        for each in props_bullet:
            if each.active:
                each.move()
                ai_settings.screen.blit(each.image, each.rect)
            else:
                each.reset()

        for each in props_plane_speed:
            if each.active:
                each.move()
                ai_settings.screen.blit(each.image, each.rect)
            else:
                each.reset()


        
        
        
        
        #判断飞机获得道具
        props_down = pygame.sprite.spritecollide(
            our_plane, props, False, pygame.sprite.collide_mask)
        if props_down:
            for row in props_down:
                row.active = False
                our_plane = row.gain(our_plane)
                if row.is_add_life and stats.life < 5:
                    stats.add_life()
                row.reset()

        # 当我方飞机存活状态, 正常展示
        if our_plane.active:
            our_plane.display(delay)

            bullets = our_plane.fire(enemies)
            for b in bullets:
                if b.active:  # 只有激活的子弹才可能击中敌机
                    b.move()
                    ai_settings.screen.blit(b.image, b.rect)
                    enemies_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemies_hit:  # 如果子弹击中飞机
                        b.active = False  # 子弹损毁
                        for e in enemies_hit:
                            e.active = e.reduce_energy()  # 小型敌机损毁
        else:
            our_plane.destroy(delay)
            stats.sub_life()
            sb.prep_life()
        
        # 调用 pygame 实现的碰撞方法 spritecollide (我方飞机如果和敌机碰撞, 更改飞机的存活属性)
        enemies_down = pygame.sprite.spritecollide(our_plane, enemies, False, pygame.sprite.collide_mask)
        if enemies_down:
            our_plane.active = False
            for row in enemies_down:
                row.active = False

        hit_plane = True        
        hit = pygame.sprite.spritecollide(our_plane, small_bullet, False, pygame.sprite.collide_mask)
        if hit:  # 如果子弹击中飞机
            for b in hit:
                if b.active == True:
                    b.active = False  # 子弹损毁
                else:
                    hit_plane = False
            if hit_plane:
                our_plane.active = False  # 飞机损毁

        hit_plane = True
        hit = pygame.sprite.spritecollide(our_plane, mid_bullet, False, pygame.sprite.collide_mask)
        if hit:  # 如果子弹击中飞机
            for b in hit:
                if b.active == True:
                    b.active = False  # 子弹损毁
                else:
                    hit_plane = False
            if hit_plane:
                our_plane.active = False  # 飞机损毁

        hit_plane = True
        hit = pygame.sprite.spritecollide(our_plane, big_bullet, False, pygame.sprite.collide_mask)
        if hit:  # 如果子弹击中飞机
            for b in hit:
                if b.active == True:
                    b.active = False  # 子弹损毁
                else:
                    hit_plane = False
            if hit_plane:
                our_plane.active = False  # 飞机损毁

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

        if stats.getTime() % 10 == 0 and stats.getTime() <= 350 and time_counter == 49:
            num_small = 1
            add_small_enemies(small_enemies, enemies, num_small, ai_settings.bg_size)  # 生成若干敌方小型飞机
            

        if stats.getTime() % 15 == 0 and stats.getTime() > 350 and stats.getTime() <= 380 and time_counter == 49:
            num_small -= 1
            num_mid += 1
            add_small_enemies(small_enemies, enemies, num_small, ai_settings.bg_size)  # 生成若干敌方小型飞机
            add_mid_enemies(mid_enemies, enemies, num_mid, ai_settings.bg_size)  # 生成若干敌方小型飞机

        if stats.getTime() % 2 == 0 and stats.getTime() > 380 and stats.getTime() <= 400 and time_counter == 49:
            for s_bullet in small_bullet:
                sbullet.speed += 2

        if stats.pause == True:
            sb.show_end()
            key = pygame.key.get_pressed()
            if key[K_q]:
                return
