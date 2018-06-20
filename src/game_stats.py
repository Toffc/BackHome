class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.score = 0
        self.life = 3

    def reset_stats(self):
        self.score = 0

    def add_score(self, score):
        self.score += score

    def reset_life(self):
        self.life = 3
    
    def add_life(self):
        self.life += 1
    
    def sub_life(self):
        self.life -= 1