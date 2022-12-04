def priorities(gift):
    if gift.islower():
        return ord(gift) - ord('a') + 1
    else:
        return ord(gift) - ord('A') + 27


def commonItems():
    commons = []
    with open("input") as f:
        lines = f.read().split('\n')[:-1]

    for line in lines:
        firstPart, secondPart = slice(0, len(line) // 2), slice(len(line) // 2, len(line))
        uniques = []
        for a in line[firstPart]:
            if a not in uniques:
                uniques.append(a)
        commons.extend(c for c in uniques if c in line[secondPart])
    return commons


def badges():
    groups = []
    with open("input") as f:
        lines = f.read().split('\n')[:-1]

    for i in range(0, len(lines), 3):
        bag1, bag2, bag3 = lines[i:i + 3]
        badge = set(bag1) & set(bag2) & set(bag3)
        groups.append(badge.pop())
    return groups


def main():
    common = [priorities(i) for i in commonItems()]
    allBadges = [priorities(i) for i in badges()]
    print(f"Part 1: {sum(common)}, Part 2: {sum(allBadges)}")


if __name__ == '__main__':
    main()
