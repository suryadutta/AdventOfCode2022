from utils import get_data


def run_part_a() -> str:
    data = get_data()

    top_calorie_count = 0

    calorie_count = 0
    for line in data:
        if line == "":
            if calorie_count > top_calorie_count:
                top_calorie_count = calorie_count
            calorie_count = 0
            continue
        calorie_count += int(line)

    return str(top_calorie_count)


def run_part_b() -> str:
    data = get_data()

    top_three_calorie_counts = [0, 0, 0]

    calorie_count = 0

    for line in data:
        if line == "":
            if calorie_count > top_three_calorie_counts[0]:
                top_three_calorie_counts.pop(0)
                top_three_calorie_counts.append(calorie_count)
                top_three_calorie_counts.sort()
            calorie_count = 0
            continue
        calorie_count += int(line)

    return str(sum(top_three_calorie_counts))
