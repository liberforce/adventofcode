def solve(instr: list[str]) -> int:
    def add(x, y):
        return (x + y) % 100

    def sub(x, y):
        return (x - y) % 100

    turn = {"L": sub, "R": add}
    acc = 50
    count = 0

    for code in instr:
        acc = turn[code[0]](acc, int(code[1:]))
        if acc == 0:
            count += 1

    return count

def main():
    with open("data.txt", "r") as fp:
        instructions = fp.read().split()
        print(solve(instructions))


if __name__ == "__main__":
    main()
