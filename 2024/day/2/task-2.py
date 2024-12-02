from copy import deepcopy
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
        tries: int = 0
        is_safe: bool = False
        ids_to_skip: list[int] = []
        removed_id: int | None = None
        while tries < 2 and is_safe is False:
            order: Literal["asc", "desc"] | None = None
            tmp_levels = deepcopy(levels)

            if ids_to_skip:
                tries += 1
                removed_id = ids_to_skip.pop()
                tmp_levels.pop(removed_id)

            for i in range((len(tmp_levels) - 1)):
                l_1, l_2 = tmp_levels[i], tmp_levels[i + 1]

                if 1 <= abs(l_1 - l_2) <= 3:
                    if l_1 > l_2:
                        if order is None or order == "desc":
                            order = "desc"
                            continue
                    elif l_1 < l_2:
                        if order is None or order == "asc":
                            order = "asc"
                            continue

                if not ids_to_skip and tries < 2:
                    ids_to_skip = [i + 1, i] # reverse since using pop
                break
            else:
                print(tmp_levels)
                is_safe = True
                break
        if is_safe:
            if removed_id:
                print(f"Removing {levels[removed_id]} helped!")
            safe_reports_count += 1
    return safe_reports_count


if __name__ == "__main__":
    print("Ho Ho Ho 🎄 It's your forth task!")
    print(f"Answer: {main('./input.txt')}")
