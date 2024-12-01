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

    # sort a two list
    ids_1 = sorted(ids_1)
    ids_2 = sorted(ids_2)

    # calculate a diff
    diff = 0
    for id_1, id_2 in zip(ids_1, ids_2, strict=True):
        diff += abs(id_1 - id_2)

    return diff


if __name__ == "__main__":
    print("Ho Ho Ho 🎄 It's your second task!")
    print(f"Answer: {main('./input.txt')}")
