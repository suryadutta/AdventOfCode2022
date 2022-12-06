from src.utils import get_data


def get_first_marker(input: str, num_distinct: int) -> int:
    start_of_packet_index = None
    for i in range(len(input)):
        window = input[i:i+num_distinct]
        if len(set(window)) == num_distinct:
            start_of_packet_index = i + num_distinct
            break
    assert start_of_packet_index is not None, "No packet start detected"
    return start_of_packet_index


def run_part_a() -> str:

    data = get_data()
    return str(get_first_marker(data[0], 4))


def run_part_b() -> str:
    data = get_data()
    return str(get_first_marker(data[0], 14))
