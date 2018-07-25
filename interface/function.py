from interface.button import Button
from config.settings import *
import pygame

def f1(ai_settings, ui_back, stats):
    button_nml = Button('material/image/normal.png', 'material/image/normal_down.png', ai_settings.screen, (125,80))
    button_inf = Button('material/image/infinite.png', 'material/image/infinite_down.png', ai_settings.screen, (270,80))
    
    route = 'material/image/mode_choose.png'
    
    while 1:
        pygame.display.update()
        ai_settings.screen.blit(ui_back, (0, 0))
        ai_settings.screen.blit(pygame.image.load(route), (50,50))

        button_nml.show()
        button_inf.show()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and button_nml.isCover():
                stats.mode = 1
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and button_inf.isCover():
                stats.mode = 2
                break
            elif button_nml.isCover():
                route = 'material/image/normal_mode.png'
                continue
            elif button_inf.isCover():
                route = 'material/image/infinite_mode.png'
                continue
            elif event.type == pygame.MOUSEBUTTONDOWN:
                stats.function = 0

        if stats.function == 0 or stats.mode != 0:
            break


def f2(ai_settings, ui_back, stats):
    while 1:
        pygame.display.update()
        ai_settings.screen.blit(ui_back, (0, 0))
        ai_settings.screen.blit(pygame.image.load('material/image/rankboard.png'), (50,50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                stats.function = 0
                #break

        if stats.function == 0:
            break

def f3(ai_settings, ui_back, stats, v):
    # button
    button_add = Button('material/image/plus.png', 'material/image/plus_down.png', ai_settings.screen, (200,290))
    button_min = Button('material/image/minus.png', 'material/image/minus_down.png', ai_settings.screen, (260,290))
    button_mute = Button('material/image/off.png', 'material/image/off_down.png', ai_settings.screen, (220,350))
    button_nml = Button('material/image/on.png', 'material/image/on_down.png', ai_settings.screen, (220,350))
    
    while 1:
        pygame.display.update()
        ai_settings.screen.blit(ui_back, (0, 0))
        ai_settings.screen.blit(pygame.image.load('material/image/setboard.png'), (100,200))
        
        button_add.show()
        button_min.show()
        if stats.mute == False:
            button_nml.show()
        else:
            button_mute.show()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                continue
            elif event.type == pygame.MOUSEBUTTONDOWN and button_add.isCover():
                add_volume(v)
                continue
            elif event.type == pygame.MOUSEBUTTONDOWN and button_min.isCover():
                min_volume(v)
                continue
            elif event.type == pygame.MOUSEBUTTONDOWN and button_nml.isCover() and stats.mute == False:
                mute()
                stats.mute = True
                continue
            elif event.type == pygame.MOUSEBUTTONDOWN and button_mute.isCover() and stats.mute == False:
                mute()
                stats.mute = True
                continue
            elif event.type == pygame.MOUSEBUTTONDOWN and button_mute.isCover() and stats.mute == True:
                normal()
                stats.mute = False
                continue
            elif event.type == pygame.MOUSEBUTTONDOWN and button_nml.isCover() and stats.mute == True:
                normal()
                stats.mute = False
                continue
            elif event.type == pygame.MOUSEBUTTONDOWN:
                stats.function = 0
            
        if stats.function == 0:
            break   

def f4(ai_settings, ui_back, stats):
    while 1:
        pygame.display.update()
        ai_settings.screen.blit(ui_back, (0, 0))
        ai_settings.screen.blit(pygame.image.load('material/image/information.png'), (100,200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                stats.function = 0
                #break

        if stats.function == 0:
            break
