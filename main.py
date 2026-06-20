from matchup import Matchup
from tracker import MatchupTracker


def main():
    tracker = MatchupTracker("data/matchups.csv")

    tracker.load_matchups()

    if len(tracker.matchups) == 0:
        puck_vs_huskar = Matchup(
            "Puck",
            "Huskar",
            "Hard",
            "Avoid long trades early. Prioritize levels and rotate after Dream Coil.",
            2,
            3
        )

        qop_vs_invoker = Matchup(
            "Queen of Pain",
            "Invoker",
            "Even",
            "Pressure early. Watch for Cold Snap and Tornado setups.",
            2,
            1
        )

        tracker.add_matchup(puck_vs_huskar)
        tracker.add_matchup(qop_vs_invoker)

        tracker.save_matchups()

    print("Dota 2 Mid-Lane Matchup Tracker")
    print("--------------------------------")
    print()

    tracker.print_all_matchups()


if __name__ == "__main__":
    main()