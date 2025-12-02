import logging

LOGGER = logging.getLogger(__name__)


def get_ranges(str_range: str) -> list[range]:
    ranges: list[range] = []
    range_strings = str_range.strip().split(",")
    for range_string in range_strings:
        bounds = [int(v) for v in range_string.split("-")]
        ranges.append(range(bounds[0], bounds[1] + 1))

    return ranges


def is_valid_id(id_: int):
    str_id = str(id_)
    if len(str_id) % 2 == 1:
        return False

    return True


def check_ids(ranges: list[range]) -> list[int]:
    invalid_ids: list[int] = []

    for range_ in ranges:
        for id_ in range_:
            if not is_valid_id(id_):
                invalid_ids.append(id_)
                LOGGER.debug("Found invalid id: %d", id_)

    return invalid_ids


def get_sum_of_invalid_ids() -> int:
    with open("data.txt", "r") as fp:
        ranges = get_ranges(fp.read())
        LOGGER.debug("ranges: %s", ranges)
        invalid_ids = check_ids(ranges)
        LOGGER.debug("invalid ids: %s", invalid_ids)
        return sum(invalid_ids)


def main():
    logging.basicConfig(level=logging.DEBUG)
    print(get_sum_of_invalid_ids())


if __name__ == "__main__":
    main()
