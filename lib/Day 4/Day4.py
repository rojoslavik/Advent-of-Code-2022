def getData():
    with open("input") as f:
        return f.read().split("\n")[:-1]


def findOverlapping(data):
    overlapping = 0
    possibilities = 0
    for line in data:
        splitted1, splitted2 = line.split(",")
        firstPartStart, firstPartEnd = splitted1.split('-')
        secondPartStart, secondPartEnd = splitted2.split('-')
        if int(firstPartStart) <= int(secondPartStart) and int(secondPartEnd) <= int(firstPartEnd) or int(
                secondPartStart) <= int(firstPartStart) and int(firstPartEnd) <= int(secondPartEnd):
            overlapping += 1
        if int(firstPartEnd) >= int(secondPartStart) and int(firstPartStart) <= int(secondPartEnd):
            possibilities += 1
        print(f"Part 1: {overlapping}, Part 2: {possibilities}")


def main():
    data = getData()
    findOverlapping(data)


if __name__ == '__main__':
    main()
