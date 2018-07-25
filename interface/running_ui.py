from interface.button import Button
import pygame

class Running():
    def __init__(self, ai_settings, stats):
        # show button
        self.button_stop = Button('material/image/game_pause_nor.png', 'material/image/game_pause_pressed.png', ai_settings.screen, (30,20))
        self.button_continue = Button('material/image/game_resume_nor.png', 'material/image/game_resume_pressed.png', ai_settings.screen, (30,20))

    def show(self, ai_settings, stats):
        if stats.pause == False:
            self.button_stop.show()
        else:
            self.button_continue.show()

        # event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.button_stop.isCover():
                stats.pause = True
            elif event.type == pygame.MOUSEBUTTONDOWN and self.button_continue.isCover():
                stats.pause = False




