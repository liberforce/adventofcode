import logging

LOGGER = logging.getLogger(__name__)


def get_ranges(str_range: str) -> list[range]:
    ranges: list[range] = []
    range_strings = str_range.strip().split(",")
    for range_string in range_strings:
        bounds = [int(v) for v in range_string.split("-")]
        ranges.append(range(bounds[0], bounds[1] + 1))

    return ranges


def cut_in(string: str, n_slices: int) -> list[str]:
    if len(string) % n_slices != 0:
        # Can't be cut exactly in that amount of slices
        raise ValueError

    slice_length = len(string) // n_slices
    slices = []

    for idx in range(n_slices):
        a_slice = string[idx * slice_length : (idx + 1) * slice_length]
        slices.append(a_slice)

    return slices


def are_slices_equal(slices: list[str]):
    reference = slices.pop()
    for slice_ in slices:
        if slice_ != reference:
            return False

    return True


def is_valid_id(id_: int):
    str_id = str(id_)
    length = len(str_id)

    # At most, all digits could be identical
    for n_slices in range(2, length + 1):
        try:
            slices = cut_in(str_id, n_slices)
        except ValueError:
            pass
        else:
            if are_slices_equal(slices):
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
