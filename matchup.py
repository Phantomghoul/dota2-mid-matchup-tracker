class Matchup:
    def __init__(self, my_hero, enemy_hero, difficulty):
        self.my_hero = my_hero
        self.enemy_hero = enemy_hero
        self.difficulty = difficulty
        self.wins = 0
        self.losses = 0

    def add_win(self):
        self.wins += 1

    def add_loss(self):
        self.losses += 1

    def get_total_games(self):
        return self.wins + self.losses

    def get_win_rate(self):
        total_games = self.get_total_games()

        if total_games == 0:
            return 0

        return (self.wins / total_games) * 100

    def get_summary(self):
        return (
            f"Matchup: {self.my_hero} vs {self.enemy_hero}\n"
            f"Games Played: {self.get_total_games()}\n"
            f"Wins: {self.wins}\n"
            f"Losses: {self.losses}\n"
            f"Win Rate: {self.get_win_rate():.1f}%\n"
            f"Difficulty: {self.difficulty}\n"
        )