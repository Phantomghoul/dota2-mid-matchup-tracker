import csv
import os
from matchup import Matchup


class MatchupTracker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.matchups = []

    def load_matchups(self):
        if not os.path.exists(self.file_path):
            return

        with open(self.file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                matchup = Matchup(
                    row["my_hero"],
                    row["enemy_hero"],
                    row["difficulty"],
                    row["notes"],
                    row["wins"],
                    row["losses"]
                )

                self.matchups.append(matchup)

    def save_matchups(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["my_hero", "enemy_hero", "wins", "losses", "difficulty", "notes"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for matchup in self.matchups:
                writer.writerow(matchup.to_dict())

    def add_matchup(self, matchup):
        self.matchups.append(matchup)

    def print_all_matchups(self):
        if len(self.matchups) == 0:
            print("No matchups found.")
            return

        for matchup in self.matchups:
            print(matchup.get_summary())
            print()

    def find_matchup(self, my_hero, enemy_hero):
        for matchup in self.matchups:
            if matchup.my_hero == my_hero and matchup.enemy_hero == enemy_hero:
                return matchup

        return None