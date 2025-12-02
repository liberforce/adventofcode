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
        passed = abs(value // 100) if value < 0 or value > 100 else 0
        is_stopped_on_zero = value % 100 == 0

        # If it stopped on 0, it's not considered a pass,
        # unless there was a whole turn
        if is_stopped_on_zero and value > 0 and passed > 0:
            passed -= 1

        if passed > 0:
            LOGGER.debug("Incrementing passed count: %d", passed)
            self.n_passed_on_zero += passed

    def set_value(self, value):
        clamped_value = value % 100
        self.value = clamped_value
        LOGGER.debug("Ended on %s", self.value)

        self.update_stopped_count(value)
        self.update_passed_count(value)

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
