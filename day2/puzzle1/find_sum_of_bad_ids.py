import logging

LOGGER = logging.getLogger(__name__)


def get_ranges(str_range) -> list[tuple[int, int]]:
    ranges = str_range.strip().split(",")
    logging.debug("Ranges: %s", ranges)
    return ranges


def check_ids(ranges: list[tuple[int, int]]) -> list[int]:
    invalid_ids: list[int] = []
    return invalid_ids


def get_sum_of_invalid_ids() -> int:
    with open("data.txt", "r") as fp:
        ranges = get_ranges(fp.read())
        invalid_ids = check_ids(ranges)
        return sum(invalid_ids)


def main():
    logging.basicConfig(level=logging.DEBUG)
    print(get_sum_of_invalid_ids())


if __name__ == "__main__":
    main()
