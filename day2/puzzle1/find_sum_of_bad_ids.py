def get_ranges(str_range) -> list[tuple[int, int]]:
    return []


def check_ids(ranges: list[tuple[int, int]]) -> int:
    invalid_ids: list[int] = []
    return sum(invalid_ids)


def get_sum_of_invalid_ids() -> int:
    with open("data.txt", "r") as fp:
        ranges = get_ranges(fp.read().split(","))
        result = check_ids(ranges)
        return result


def main():
    print(get_sum_of_invalid_ids())
