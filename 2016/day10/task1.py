from collections import defaultdict
import re


def main():
    with open("input", "r") as file:
        bots = defaultdict(lambda: [])
        instrs = {}
        readyForAction = []
        for line in file.readlines():
            numbers = [int(x) for x in re.findall(r"\d+", line)]
            if len(numbers) == 3:
                receivers = re.findall(r"bot|output", line)
                instrs[numbers[0]] = tuple(list(zip(receivers, numbers))[1:])
            else:
                botId = numbers[1]
                bots[botId].append(numbers[0])
                if len(bots[botId]) == 2:
                    readyForAction.append(botId)

    outputs = defaultdict(lambda: set())
    while readyForAction:
        botId = readyForAction.pop(0)
        chips = tuple(sorted(bots[botId]))
        bots[botId] = []
        if chips == (17, 61):
            print(botId)
            break

        for (receiver, id), chip in zip(instrs[botId], chips):
            if receiver == "output":
                outputs[id].add(chip)
            else:
                bots[id].append(chip)
                if len(bots[id]) == 2:
                    readyForAction.append(id)


if __name__ == "__main__":
    main()
