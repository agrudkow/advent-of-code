
import re


def parse_input(path: str) -> int:
    with open(path, "r") as f:
        raw_input = [line.strip() for line in f.readlines()]
    assert all([len(row) == len(raw_input[0]) for row in raw_input])
    dims = (len(raw_input[0]), len(raw_input))

    word = "XMAS"
    reversed_word = word[::-1]
    diagonal_re = "".join([rf"({c})(?=(.{{{dims[0] + 1}}})|\n)" for c in word])
    # reversed_diagonal_re = "".join([rf"({c})(?=(.{{{dims[0] + 1}}})|\n)" for c in reversed_word])

    # vertical_re = "".join([rf"({c})(?=(.{{{dims[0] + 0}}})|\n)" for c in word])
    # reversed_vertical_re = "".join([rf"({c})(?=(.{{{dims[0] + 0}}})|\n)" for c in reversed_word])

    # second_diagonal_re = "".join([rf"({c})(?=(.{{{dims[0] -1 }}})|\n)" for c in word])
    # reversed_second_diagonal_re = "".join([rf"({c})(?=(.{{{dims[0] -1 }}})|\n)" for c in reversed_word])

    str_input = "\n".join(raw_input) + "\n"
    all_matches = 0
    
    return all_matches


if __name__ == "__main__":
    print("Ho Ho Ho 🎄 It's your 7-TH task!")
    print(f"Answer: {parse_input('./simple-input.txt')}")
