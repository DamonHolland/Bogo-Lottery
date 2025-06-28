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


def participant_summary(participant_data: Participants):
    print("".center(50, "-"))
    for name, pity in participant_data.items():
        print(f"{name}: {pity}")
    print("".center(50, "-"))
