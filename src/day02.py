from src.utils import get_data

selection_bonuses = {"rock": 1, "paper": 2, "scissors": 3}
beat = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
scoring = {"lose": 0, "draw": 3, "win": 6}


def result(a, b):
    if a == b:
        return "draw"
    if beat[a] == b:
        return "lose"
    return "win"


def run_part_a() -> str:
    data = get_data()

    mapping = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }

    score = 0
    for rps_round in data:
        choices = rps_round.split(" ")
        opp_choice = mapping[choices[0]]
        my_choice = mapping[choices[1]]

        round_result = result(my_choice, opp_choice)
        score += scoring[round_result] + selection_bonuses[my_choice]

    return str(score)


def run_part_b() -> str:
    data = get_data()

    opp_mapping = {"A": "rock", "B": "paper", "C": "scissors"}
    needed_result = {"X": "lose", "Y": "draw", "Z": "win"}

    score = 0
    for rps_round in data:
        choices = rps_round.split(" ")
        opp_choice = opp_mapping[choices[0]]
        round_result = needed_result[choices[1]]

        my_choice = None
        for choice in selection_bonuses.keys():
            if result(choice, opp_choice) == round_result:
                my_choice = choice
                break
        assert my_choice is not None

        score += scoring[round_result] + selection_bonuses[my_choice]

    return str(score)
