def part1():
    with open("input") as f:
        data = f.read().split('\n')[:-1]

    scores = []
    cheatingScores = []
    choice = {'X': 1, 'Y': 2, 'Z': 3}

    hands = {'A X': 3, 'A Y': 6, 'A Z': 0,
             'B X': 0, 'B Y': 3, 'B Z': 6,
             'C X': 6, 'C Y': 0, 'C Z': 3}

    strategy = {'A X': 'A Z', 'A Y': 'A X', 'A Z': 'A Y',
                'B X': 'B X', 'B Y': 'B Y', 'B Z': 'B Z',
                'C X': 'C Y', 'C Y': 'C Z', 'C Z': 'C X'}

    for line in data:
        scores.extend(handScore + choice[i[-1]] for i, handScore in hands.items() if i in line)
        if line in strategy:
            neededResult = strategy[line]
            cheatingScores.extend(hands[neededResult] + choice[neededResult[-1]] for hand in hands if hand in neededResult)

    print(f"Part 1 result: {sum(scores)}, Part 2 result: {sum(cheatingScores)}")


def main():
    part1()


if __name__ == '__main__':
    main()
