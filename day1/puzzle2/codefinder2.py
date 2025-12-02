import logging

LOGGER = logging.getLogger(__name__)


class Dial:
    def __init__(self, value: int = 50):
        self.value = value
        self.n_passed_on_zero = 0
        self.n_stopped_on_zero = 0
        LOGGER.debug("Initialized at %s", self.value)

    def update_stopped_count(self, value):
        if value % 100 == 0:
            LOGGER.debug("Incrementing stopped count")
            self.n_stopped_on_zero += 1

    def update_passed_count(self, value):
        passed = abs(value // 100)

        if self.value > 0 and value == 0:
            passed += 1

        if self.value == 0 and value < 0:
            passed -= 1

        if passed > 0:
            LOGGER.debug("Incrementing passed count: %d", passed)
            self.n_passed_on_zero += passed

    def set_value(self, value):
        clamped_value = value % 100
        LOGGER.debug("Ended on %s", clamped_value)

        self.update_stopped_count(value)
        self.update_passed_count(value)

        self.value = clamped_value

    def turn_right(self, offset):
        value = self.value + offset
        self.set_value(value)

    def turn_left(self, offset):
        value = self.value - offset
        self.set_value(value)

    def turn(self, direction: str, offset: int):
        LOGGER.debug(
            "Turning %s %d",
            "left" if direction == "L" else "right",
            offset,
        )
        turn = {"L": self.turn_left, "R": self.turn_right}
        turn[direction](offset)


def solve(instr: list[str]):
    dial = Dial(50)

    for code in instr:
        dial.turn(code[0], int(code[1:]))

    print(f"{dial.n_stopped_on_zero=}")
    print(f"{dial.n_passed_on_zero=}")


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
