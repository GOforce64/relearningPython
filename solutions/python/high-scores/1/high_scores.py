class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]
        
    def personal_best(self):
        sorted_list = sorted(self.scores, reverse=True)
        return sorted_list[0]
    
    def personal_top_three(self):
        sorted_list = sorted(self.scores, reverse=True)
        return sorted_list[:3]