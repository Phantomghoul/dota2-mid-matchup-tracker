from matchup import Matchup


def main():
    puck_vs_huskar = Matchup(
        "Puck",
        "Huskar",
        "Hard",
    )

    qop_vs_invoker = Matchup(
        "Queen of Pain",
        "Invoker",
        "Even",
    )

    puck_vs_huskar.add_loss()
    puck_vs_huskar.add_loss()
    puck_vs_huskar.add_win()
    puck_vs_huskar.add_win()
    puck_vs_huskar.add_loss()

    qop_vs_invoker.add_win()
    qop_vs_invoker.add_loss()
    qop_vs_invoker.add_win()

    print(puck_vs_huskar.get_summary())
    print()
    print(qop_vs_invoker.get_summary())


if __name__ == "__main__":
    main()