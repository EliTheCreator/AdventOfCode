import re
from collections import deque


def main():
    file = open("input", "r")
    p1_raw, p2_raw = file.read().split("\n\n")
    file.close()
    p1 = deque([int(x) for x in re.findall(r"\d+", p1_raw)][1:])
    p2 = deque([int(x) for x in re.findall(r"\d+", p2_raw)][1:])

    # dp = {}

    def recursive_combat(p1, p2):
        p1_configs = set()
        p2_configs = set()
        while p1 and p2:
            p1_config = 0
            for i, v in enumerate(p1):
                p1_config += 10**i * v
            p2_config = 0
            for i, v in enumerate(p2):
                p2_config += 10**i * v

            # if (p1_config, p2_config) in dp:
            #     return dp[(p1_config, p2_config)]

            if p1_config in p1_configs or p2_config in p2_configs:
                p2 = []
                break
            else:
                p1_configs.add(p1_config)
                p2_configs.add(p2_config)

            max_p1 = max(p1)
            if max_p1 > max(p2) and max_p1 > len(p1) + len(p2):
                return 0

            card_p1 = p1.popleft()
            card_p2 = p2.popleft()

            if card_p1 > len(p1) or card_p2 > len(p2):
                if card_p1 > card_p2:
                    p1.append(card_p1)
                    p1.append(card_p2)
                else:
                    p2.append(card_p2)
                    p2.append(card_p1)
            else:
                result = recursive_combat(
                    deque(list(p1)[:card_p1]), deque(list(p2)[:card_p2]))
                if result:
                    p2.append(card_p2)
                    p2.append(card_p1)
                else:
                    p1.append(card_p1)
                    p1.append(card_p2)

        if p1:
            # dp[(p1_config, p2_config)] = 0
            return 0
        else:
            # dp[(p1_config, p2_config)] = 1
            return 1

    recursive_combat(p1, p2)

    score = 0
    if p1:
        p1.reverse()
        for i, v in enumerate(p1, start=1):
            score += i * v
    else:
        p2.reverse()
        for i, v in enumerate(p2, start=1):
            score += i * v

    print(score)


if __name__ == "__main__":
    main()
