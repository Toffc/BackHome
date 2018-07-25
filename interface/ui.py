from interface.button import Button
import pygame

class Ui():
    def __init__(self, ai_settings, stats):
        # main button
        self.button_feiji = Button('material/image/feiji.png', 'material/image/feiji_down.png', ai_settings.screen, (200,300))
        # self.button_rank = Button('material/image/rank.png', 'material/image/rank_down.png', ai_settings.screen, (200,340))
        self.button_setting = Button('material/image/setting.png', 'material/image/setting_down.png', ai_settings.screen, (200,340))
        self.button_about = Button('material/image/about.png', 'material/image/about_down.png', ai_settings.screen, (200,380))
        

    def show(self, ai_settings, stats):
        self.button_feiji.show()
        # self.button_rank.show()
        self.button_setting.show()
        self.button_about.show()
        ai_settings.screen.blit(pygame.image.load('material/image/openning.png'), (130,100))

        # event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.button_feiji.isCover():
                stats.function = 1
            # elif event.type == pygame.MOUSEBUTTONDOWN and self.button_rank.isCover():
            #     stats.function = 2
            elif event.type == pygame.MOUSEBUTTONDOWN and self.button_setting.isCover():
                stats.function = 3
            elif event.type == pygame.MOUSEBUTTONDOWN and self.button_about.isCover():
                stats.function = 4
            


