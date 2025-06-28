import copy
from math import floor

from participant_management import Participants


def increment_pity(participant_data: Participants, winner: str) -> Participants:
    new_participant_data = copy.deepcopy(participant_data)
    for participant in participant_data.keys():
        if participant == winner:
            new_participant_data[participant] = 1
            continue
        new_participant_data[participant] += 1
        new_participant_data[participant] *= 1.3
        new_participant_data[participant] = floor(new_participant_data[participant])
    return new_participant_data
