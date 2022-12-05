# Stacks removed from inputs file since I can't be arsed to parse them by code
import re

stacks = {1: ['F', 'H', 'M', 'T', 'V', 'L', 'D'],
          2: ['P', 'N', 'T', 'C', 'J', 'G', 'Q', 'H'],
          3: ['H', 'P', 'M', 'D', 'S', 'R'],
          4: ['F', 'V', 'B', 'L'],
          5: ['Q', 'L', 'G', 'H', 'N'],
          6: ['P', 'M', 'R', 'G', 'D', 'B', 'W'],
          7: ['Q', 'L', 'H', 'C', 'R', 'N', 'M', 'G'],
          8: ['W', 'L', 'C'],
          9: ['T', 'M', 'Z', 'J', 'Q', 'L', 'D', 'R']}

part1 = False
part2 = True


def getData():
    with open("input") as f:
        return f.read().split('\n')[:-1]


def getMoves(data):
    movesList = {}
    for index, line in enumerate(data):
        moves = re.findall(r'\d+', line)
        movesList[index] = moves
    return movesList


def moveStacks(moveslist):
    for i, moves in moveslist.items():
        howMany = int(moves[0])
        fromStack = int(moves[1])
        toStack = int(moves[2])
        for _ in range(howMany):
            if part1:
                disk = stacks[fromStack].pop(0)
                stacks[toStack].insert(0, disk)
            elif part2:
                disks = stacks[fromStack][:howMany]
                del stacks[fromStack][:howMany]
                stacks[toStack][:0] = disks
                break
    print(stacks)


def main():
    data = getData()
    movesList = getMoves(data)
    moveStacks(movesList)


if __name__ == '__main__':
    main()

