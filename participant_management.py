import json
import os
from typing import Dict, Optional

Participants = Dict[str, float]
participants_path = "./data"


def get_latest_participants_key() -> int:
    files = [f for f in os.listdir(participants_path) if os.path.isfile(os.path.join(participants_path, f))]
    cycles = [int("".join(c for c in fn if c.isnumeric())) for fn in files]
    return sorted(cycles, reverse=True)[0]


def get_participants(participant_cycle: Optional[int] = None):
    if participant_cycle is None:
        participant_cycle = get_latest_participants_key()

    with open(f"data/participants_{participant_cycle}.json", "r") as file:
        participant_data = json.loads(file.read())
    return participant_data


def create_next_participants(participant_data: Participants):
    latest_participants = get_latest_participants_key()
    latest_participants += 1
    with open(f"data/participants_{latest_participants}.json", "w") as file:
        json.dump(participant_data, file, indent=4)


def participant_summary(participant_data: dict):
    print("-" * 50)
    total_entries = sum(participant_data.values())
    print(f"{'Participant Odds Summary':^50}")
    print("-" * 50)
    print(f"{'Name':<20} | {'Entries':<10} | {'Odds (%)':<10}")
    print("-" * 50)

    participants = []
    for name, entries in participant_data.items():
        odds = round((entries / total_entries) * 100, 2) if total_entries else 0
        participants.append((name, entries, odds))
    participants.sort(key=lambda x: x[2], reverse=True)

    for name, entries, odds in participants:
        print(f"{name:<20} | {entries:<10} | {odds:<10.2f}")

    print("-" * 50)
    print(f"{'Total entries:':<20} {total_entries}")
    print("-" * 50)
