from participant_management import get_participants, participant_summary, create_next_participants
from pity_system import increment_pity
from weighted_lottery_system import pull_winner


def main():
    participant_data = get_participants()
    participant_summary(participant_data)

    winner = pull_winner(participant_data)
    print(f"Lottery Winner: {winner}")
    participant_data = increment_pity(participant_data, winner)
    create_next_participants(participant_data)


if __name__ == '__main__':
    main()
