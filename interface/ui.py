from interface.button import Button
import pygame

class Ui():
    def __init__(self, ai_settings, stats):
        # show button
        self.button_feiji = Button('material/image/feiji.png', 'material/image/feiji_down.png', ai_settings.screen, (540,300))
        self.button_rank = Button('material/image/rank.png', 'material/image/rank_down.png', ai_settings.screen, (540,340))
        self.button_setting = Button('material/image/setting.png', 'material/image/setting_down.png', ai_settings.screen, (540,380))

    def show(self, ai_settings, stats):
        self.button_feiji.show()
        self.button_rank.show()
        self.button_setting.show()

        # event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.button_feiji.isCover():
                stats.feiji = True


