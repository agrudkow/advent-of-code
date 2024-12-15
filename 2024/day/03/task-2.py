import re

MUL_PATTERN = re.compile(r"(do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\))")


def parse_input(path: str) -> list[bool | tuple[str, str]]:
    with open(path, "r") as f:
        raw_input = "".join([line.strip() for line in f.readlines()])

    output: list[bool | tuple[str, str]] = []
    for s in MUL_PATTERN.findall(raw_input):
        if "don't" in s:
            output.append(False)
        elif "do" in s:
            output.append(True)
        else:
            output.append(s[4:-1].split(",", maxsplit=2))

    return output


def remove_disabled(input: list[bool | tuple[str, str]]) -> list[tuple[int, int]]:
    is_enabled = True
    mul_instructions: list[tuple[int, int]] = []
    for instruction in input:
        if instruction is False:
            is_enabled = False
            continue
        elif instruction is True:
            is_enabled = True
            continue

        if is_enabled:
            mul_instructions.append((int(instruction[0]), int(instruction[1])))

    return mul_instructions


def mul_add(input: list[tuple[int, int]]) -> int:
    return sum([int(a) * int(b) for a, b in input])


def main(path: str) -> int:
    return mul_add(remove_disabled(parse_input(path)))


if __name__ == "__main__":
    print("Ho Ho Ho 🎄 It's your sixth task!")
    print(f"Answer: {main('./input.txt')}")
