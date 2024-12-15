import re

import numpy as np


def get_all_diagonals(matrix: np.ndarray) -> list[list[str]]:
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    diagonals: list[list[str]] = []

    # Collect main diagonals (top-left to bottom-right)
    for d in range(-(rows - 1), cols):
        diagonal: list[str] = []  # Collect one diagonal
        for i in range(rows):
            j = i + d  # Calculate the column index for this diagonal
            if 0 <= j < cols:  # Ensure column index is within bounds
                diagonal.append(matrix[i][j])
        if diagonal:
            diagonals.append(diagonal)

    # Collect anti-diagonals (top-right to bottom-left)
    for d in range(rows + cols - 1):
        diagonal: list[str] = []  # Collect one diagonal
        for i in range(rows):
            j = d - i  # Calculate the column index for this diagonal
            if 0 <= j < cols:  # Ensure column index is within bounds
                diagonal.append(matrix[i][j])
        if diagonal:
            diagonals.append(diagonal)

    return diagonals


def task_1(path: str) -> int:
    with open(path, "r") as f:
        raw_input = [list(line.strip()) for line in f.readlines()]

    matrix = np.array(raw_input)
    all_rows = ["".join(row) for row in matrix]
    all_rows += ["".join(row) for row in matrix.T]
    all_rows += ["".join(row) for row in get_all_diagonals(matrix)]

    xmas_re = re.compile(r"(?=(XMAS|SAMX))")
    count = 0
    for row in all_rows:
        matches = xmas_re.findall(row)
        count += len(matches)
    return count


def task_2(path: str) -> int:
    with open(path, "r") as f:
        raw_input = [list(line.strip()) for line in f.readlines()]

    count = 0
    matrix = np.array(raw_input)
    for i in range(1, matrix.shape[1] - 1):
        for j in range(1, matrix.shape[0] - 1):
            if matrix[i, j] == "A":
                diag_1 = matrix[i - 1, j - 1] + matrix[i, j] + matrix[i + 1, j + 1]
                diag_2 = matrix[i + 1, j - 1] + matrix[i, j] + matrix[i - 1, j + 1]

                mases = {"MAS", "SAM"}
                if diag_1 in mases and diag_2 in mases:
                    count += 1

    return count


if __name__ == "__main__":
    print("Ho Ho Ho 🎄 It's your 7-TH task!")
    print(f"Answer: {task_2('./input.txt')}")
