from collections import Counter

def main(path: str) -> int:
    # load a file
    with open(path, "r") as f:
        lines = f.read().splitlines()

    ids_1: list[int] = []
    ids_2: list[int] = []

    for line in lines:
        sid_1, sid_2 = line.split(maxsplit=2)
        ids_1.append(int(sid_1))
        ids_2.append(int(sid_2))

    # create a counter for second list
    ids_2_counter = Counter(ids_2)

    # Count similarity score
    score = 0
    for id_1 in ids_1:
        score += id_1 * ids_2_counter.get(id_1, 0)

    return score


if __name__ == "__main__":
    print("Ho Ho Ho 🎄 It's your second task!")
    print(f"Answer: {main('./input.txt')}")
