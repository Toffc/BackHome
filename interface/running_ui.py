from interface.button import Button
import pygame

class Running():
    def __init__(self, ai_settings, stats):
        # show button
        self.button_stop = Button('material/image/game_pause_nor.png', 'material/image/game_pause_pressed.png', ai_settings.screen, (30,20))

    def show(self, ai_settings, stats):
        self.button_stop.show()

                
            




