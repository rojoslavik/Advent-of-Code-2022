part1 = True
part2 = False


def parseInput():
    with open("input") as f:
        return f.read()


def splitInput(data):
    n = 0
    if part1:
        n = 4
    elif part2:
        n = 14

    for i in range(len(data) - 3):
        substring = data[i:i + n]
        if len(set(substring)) == n:
            index = i + len(substring)
            print(index)
            break


def main():
    data = parseInput()
    splitInput(data)


if __name__ == '__main__':
    main()
