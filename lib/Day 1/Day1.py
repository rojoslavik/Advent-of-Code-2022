def part1():
    carryingCalories = []
    calories = 0
    with open("input", mode="r") as f:
        elfCalories = f.read().split("\n")

    for carrying in elfCalories:
        if carrying:
            calories += int(carrying)
        if not carrying:
            carryingCalories.append(calories)
            calories = 0
    print(max(carryingCalories))
    return carryingCalories


def part2(carryingCalories):
    inOrder = sorted(carryingCalories)
    print(sum(inOrder[-3:]))


def main():
    carryingCalories = part1()
    part2(carryingCalories)


if __name__ == '__main__':
    main()
