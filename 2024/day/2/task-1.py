from typing import Literal


def main(path: str) -> int:
    # load a file
    with open(path, "r") as f:
        lines = f.read().splitlines()

    # parse lines and get reports
    reports: list[list[int]] = []
    for line in lines:
        levels = [int(s) for s in line.split()]
        reports.append(levels)

    # eval safeties of reports
    safe_reports_count: int = 0
    for levels in reports:
        order: Literal["asc", "desc"] | None = None
        for i in range((len(levels) - 1)):
            l_1, l_2 = levels[i], levels[i + 1]

            if l_1 > l_2:
                if order is None:
                    order = "desc"
                elif order != "desc":
                    break
            elif l_1 < l_2:
                if order is None:
                    order = "asc"
                elif order != "asc":
                    break

            if 1 <= abs(l_1 - l_2) <= 3:
                continue

            break
        else:
            safe_reports_count += 1

    return safe_reports_count


if __name__ == "__main__":
    print("Ho Ho Ho 🎄 It's your third task!")
    print(f"Answer: {main('./input.txt')}")
