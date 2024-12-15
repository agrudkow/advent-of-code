import re

MUL_PATTERN = re.compile(r"(mul\(\d{1,3},\d{1,3}\))")


def parse_input(path: str) -> list[tuple[int, int]]:
    with open(path, "r") as f:
        raw_input = "".join([line.strip() for line in f.readlines()])
    return [mul[4:-1].split(",", maxsplit=2) for mul in MUL_PATTERN.findall(raw_input)]

def mul_add(input: list[tuple[int, int]]) -> int:
    return sum([int(a) * int(b) for a, b in input])

def main(path: str) -> int:
    return mul_add(parse_input(path))


if __name__ == "__main__":
    print("Ho Ho Ho 🎄 It's your fifth task!")
    print(f"Answer: {main('./input.txt')}")
