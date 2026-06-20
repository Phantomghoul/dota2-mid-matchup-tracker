class Matchup:
    def __init__(self, my_hero, enemy_hero, difficulty, notes, wins=0, losses=0):
        self.my_hero = my_hero
        self.enemy_hero = enemy_hero
        self.difficulty = difficulty
        self.notes = notes
        self.wins = int(wins)
        self.losses = int(losses)

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
            f"Notes: {self.notes}"
        )

    def to_dict(self):
        return {
            "my_hero": self.my_hero,
            "enemy_hero": self.enemy_hero,
            "wins": self.wins,
            "losses": self.losses,
            "difficulty": self.difficulty,
            "notes": self.notes
        }