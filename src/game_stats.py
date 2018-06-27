class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.score = 0
        self.life = 3
        self.time = 60

    def reset_stats(self):
        self.score = 0
        self.time = 60

    def add_score(self, score):
        self.score += score

    def reset_life(self):
        self.life = 3
    
    def add_life(self):
        self.life += 1
    
    def sub_life(self):
        self.life -= 1
    
    def sub_time(self):
        self.time -= 1
        if(self.time == 0):
            self.time = 0