class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.score = 0

    def reset_stats(self):
        self.score = 0
