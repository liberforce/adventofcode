import logging

LOGGER = logging.getLogger(__name__)


class Dial:
    def __init__(self, value: int = 50):
        self.value = value
        self.n_passed_on_zero = 0
        self.n_stopped_on_zero = 0
        LOGGER.debug("Initialized at %s", self.value)

    def check_position(self):
        if self.value == 0:
            self.n_stopped_on_zero += 1
        LOGGER.debug(
            "Ended on %s%s",
            self.value,
            (", incrementing" if self.value == 0 else ""),
        )

    def clamp(self, offset: int) -> int:
        self.n_passed_on_zero += offset // 100
        clamped = offset % 100
        return clamped

    def turn_right(self, offset):
        offset = self.clamp(offset)
        self.value = self.clamp(self.value + offset)
        self.check_position()

    def turn_left(self, offset):
        offset = self.clamp(offset)
        self.value = self.clamp(self.value - offset)
        self.check_position()

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
