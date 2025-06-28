import random

from participant_management import Participants


def pull_winner(participant_data: Participants) -> str:
    participant_names = list(participant_data.keys())
    participant_pity = list(participant_data.values())
    winner = random.choices(participant_names, weights=participant_pity, k=1)[0]
    return winner
