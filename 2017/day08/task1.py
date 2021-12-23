from collections import defaultdict


def main():
    with open("input", "r") as file:
        instructions = [[part.split(" ") for part in line.strip().split(" if ")]
                        for line in file.readlines()]

    regs = defaultdict(lambda: 0)
    for action, condition in instructions:
        condRegVal = regs[condition[0]]
        condConstVal = int(condition[2])
        condVal = 0
        match condition[1]:
            case ">":
                condVal = condRegVal > condConstVal
            case ">=":
                condVal = condRegVal >= condConstVal
            case "<":
                condVal = condRegVal < condConstVal
            case "<=":
                condVal = condRegVal <= condConstVal
            case "==":
                condVal = condRegVal == condConstVal
            case "!=":
                condVal = condRegVal != condConstVal
            case _:
                pass

        if condVal:
            actRegName = action[0]
            actConstVal = int(action[2])
            match action[1]:
                case "inc":
                    regs[actRegName] += actConstVal
                case "dec":
                    regs[actRegName] -= actConstVal
                case _:
                    pass

    print(max(regs.values()))


if __name__ == "__main__":
    main()
