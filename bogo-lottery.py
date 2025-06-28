import copy
import json
import random
from math import floor
from typing import Dict

Participants = Dict[str, float]


def participant_summary(participant_data: Participants):
    print("".center(50, "-"))
    for name, pity in participant_data.items():
        print(f"{name}: {pity}")
    print("".center(50, "-"))


def pull_winner(participant_data: Participants) -> str:
    participant_names = list(participant_data.keys())
    participant_pity = list(participant_data.values())
    winner = random.choices(participant_names, weights=participant_pity, k=1)[0]
    return winner


def increment_pity(participant_data: Participants, winner: str) -> Participants:
    new_participant_data = copy.deepcopy(participant_data)
    for participant in participant_data.keys():
        if participant == winner:
            new_participant_data[participant] = 1
            continue
        new_participant_data[participant] += 1
        new_participant_data[participant] *= 1.35
        new_participant_data[participant] = floor(new_participant_data[participant])
    return new_participant_data


def main():
    with open("./data/participants.json", "r") as file:
        participant_data = json.loads(file.read())

    num_simulations = 50
    total_wins = {}
    for sim in range(num_simulations):
        participant_summary(participant_data)

        winner = pull_winner(participant_data)
        if winner not in total_wins:
            total_wins[winner] = 0
        total_wins[winner] += 1
        print(f"Simulated lottery {sim + 1} winner: {winner}")
        participant_data = increment_pity(participant_data, winner)

    print("Winner summary")
    for participant, wins in total_wins.items():
        print(f"{participant}: {wins}")


if __name__ == '__main__':
    main()
