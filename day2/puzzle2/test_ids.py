import pytest

from find_sum_of_bad_ids import check_ids, get_ranges, is_valid_id


def test_get_ranges():
    assert get_ranges("1-2") == [range(1, 3)]
    assert get_ranges("1-2,11-22") == [range(1, 3), range(11, 23)]


@pytest.mark.parametrize(
    "invalid_id",
    [
        11,
        22,
        99,
        1010,
        1188511885,
        222222,
        446446,
        38593859,
    ],
)
def test_check_invalid_ids(invalid_id):
    assert not is_valid_id(invalid_id)


@pytest.mark.parametrize(
    "str_range, invalid_ids",
    [
        ("11-22", [11, 22]),
        ("95-115", [99]),
        ("998-1012", [1010]),
        ("1188511880-1188511890", [1188511885]),
        ("222220-222224", [222222]),
        ("1698522-1698528", []),
        ("446443-446449", [446446]),
        ("38593856-38593862", [38593859]),
        ("565653-565659", []),
        ("824824821-824824827", []),
        ("2121212118-2121212124", []),
    ],
)
def test_invalid_ids(str_range, invalid_ids):
    expected = invalid_ids
    ranges = get_ranges(str_range)
    actual = check_ids(ranges)
    assert actual == expected
