import pytest

from codefinder2 import Dial


def test_init():
    dial = Dial()
    assert dial.value == 50


@pytest.mark.parametrize(
    "start_value, turned, expected_val",
    [
        (98, 1, 99),
        (98, 2, 0),
        (98, 3, 1),
        (98, 101, 99),
        (98, 102, 0),
        (98, 103, 1),
        (99, 1, 0),
        (99, 2, 1),
        (99, 3, 2),
        (99, 101, 0),
        (99, 102, 1),
        (99, 103, 2),
        (0, 99, 99),
        (0, 100, 0),
        (0, 101, 1),
        (1, 98, 99),
        (1, 99, 0),
        (1, 100, 1),
    ],
)
def test_dial_value_turn_right(
    start_value,
    turned,
    expected_val,
):
    dial = Dial(start_value)
    dial.turn_right(turned)
    assert dial.value == expected_val


@pytest.mark.parametrize(
    "start_value, turned, expected_val",
    [
        (98, 1, 97),
        (98, 2, 96),
        (98, 3, 95),
        (98, 101, 97),
        (98, 102, 96),
        (98, 103, 95),
        (99, 1, 98),
        (99, 2, 97),
        (99, 3, 96),
        (99, 101, 98),
        (99, 102, 97),
        (99, 103, 96),
        (0, 99, 1),
        (0, 100, 0),
        (0, 101, 99),
        (1, 98, 3),
        (1, 99, 2),
        (1, 100, 1),
    ],
)
def test_dial_value_turn_left(
    start_value,
    turned,
    expected_val,
):
    dial = Dial(start_value)
    dial.turn_left(turned)
    assert dial.value == expected_val


@pytest.mark.parametrize(
    "turned, expected_stops",
    [
        (49, 0),
        (50, 1),
        (51, 0),
        (149, 0),
        (150, 1),
        (151, 0),
        (249, 0),
        (250, 1),
        (251, 0),
    ],
)
def test_dial_stopped_on_turn_right(
    turned,
    expected_stops,
):
    dial = Dial(50)
    dial.turn_right(turned)
    assert dial.n_stopped_on_zero == expected_stops


@pytest.mark.parametrize(
    "turned, expected_stops",
    [
        (49, 0),
        (50, 1),
        (51, 0),
        (149, 0),
        (150, 1),
        (151, 0),
        (249, 0),
        (250, 1),
        (251, 0),
    ],
)
def test_dial_stopped_on_turn_left(
    turned,
    expected_stops,
):
    dial = Dial(50)
    dial.turn_left(turned)
    assert dial.n_stopped_on_zero == expected_stops


@pytest.mark.parametrize(
    "turned, expected_passed",
    [
        (49, 0),
        (50, 1),
        (51, 1),
        (149, 1),
        (150, 2),
        (151, 2),
        (249, 2),
        (250, 3),
        (251, 3),
    ],
)
def test_dial_passed_on_turn_right(
    turned,
    expected_passed,
):
    dial = Dial(50)
    dial.turn_right(turned)
    assert dial.n_passed_on_zero == expected_passed


@pytest.mark.parametrize(
    "turned, expected_passed",
    [
        (49, 0),
        (50, 1),
        (51, 1),
        (149, 1),
        (150, 2),
        (151, 2),
        (249, 2),
        (250, 3),
        (251, 3),
    ],
)
def test_dial_passed_on_turn_left(
    turned,
    expected_passed,
):
    dial = Dial(50)
    dial.turn_left(turned)
    assert dial.n_passed_on_zero == expected_passed


def test_dial_passed_step_by_step():
    dial = Dial(50)

    dial.turn_left(68)
    assert dial.value == 82
    assert dial.n_passed_on_zero == 1

    dial.turn_left(30)
    assert dial.value == 52
    assert dial.n_passed_on_zero == 1

    dial.turn_right(48)
    assert dial.value == 0
    assert dial.n_passed_on_zero == 2

    dial.turn_left(5)
    assert dial.value == 95
    assert dial.n_passed_on_zero == 2

    dial.turn_right(60)
    assert dial.value == 55
    assert dial.n_passed_on_zero == 3

    dial.turn_left(55)
    assert dial.value == 0
    assert dial.n_passed_on_zero == 4

    dial.turn_left(1)
    assert dial.value == 99
    assert dial.n_passed_on_zero == 4

    dial.turn_left(99)
    assert dial.value == 0
    assert dial.n_passed_on_zero == 5

    dial.turn_right(14)
    assert dial.value == 14
    assert dial.n_passed_on_zero == 5

    dial.turn_left(82)
    assert dial.value == 32
    assert dial.n_passed_on_zero == 6
