from participant_management import get_participants, participant_summary
from pity_system import increment_pity
from weighted_lottery_system import pull_winner


def main():
    participant_data = get_participants(0)

    num_simulations = 24
    total_wins = {p: 0 for p in participant_data.keys()}
    for sim in range(num_simulations):
        participant_summary(participant_data)

        winner = pull_winner(participant_data)
        total_wins[winner] += 1
        print(f"Simulated lottery {sim + 1} winner: {winner}")
        participant_data = increment_pity(participant_data, winner)

    print("Winner summary")
    for participant, wins in total_wins.items():
        print(f"{participant}: {wins}")


if __name__ == '__main__':
    main()
