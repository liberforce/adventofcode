import logging

LOGGER = logging.getLogger(__name__)


class Dial:
    def __init__(self, value: int = 50):
        self.value = value
        self.n_passed_on_zero = 0
        self.n_stopped_on_zero = 0
        LOGGER.debug("Initialized at %s", self.value)

    def incr_stopped(self):
        self.n_stopped_on_zero += 1

        LOGGER.debug(
            "Ended on %s%s",
            self.value,
            (", incrementing" if self.value == 0 else ""),
        )

    def incr_passed(self, turns):
        self.n_passed_on_zero += turns

    def set_value(self, value):
        clamped_value = value % 100
        n_times_passed = value // 100

        if clamped_value == 0:
            self.incr_stopped()
            n_times_passed -= 1

        self.incr_passed(n_times_passed)
        self.value = clamped_value

    def turn_right(self, offset):
        value = self.value + offset
        self.set_value(value)

    def turn_left(self, offset):
        value = self.value - offset
        self.set_value(value)

    def turn(self, direction: str, offset: int):
        turn = {"L": self.turn_left, "R": self.turn_right}
        turn[direction](offset)


def solve(instr: list[str]):
    dial = Dial(50)

    for code in instr:
        LOGGER.debug("Turning %s", code)
        dial.turn(code[0], int(code[1:]))

    LOGGER.info(f"{dial.n_stopped_on_zero=}")
    LOGGER.info(f"{dial.n_passed_on_zero=}")
    print(dial.n_passed_on_zero + dial.n_stopped_on_zero)


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        style="{",
        format="{levelname}:{name}:{funcName}:{lineno}:{message}",
    )

    with open("data.txt", "r") as fp:
        instructions = fp.read().split()
        solve(instructions)


if __name__ == "__main__":
    main()
