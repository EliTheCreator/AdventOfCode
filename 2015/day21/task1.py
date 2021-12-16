from itertools import combinations
from math import ceil
from operator import add


def main():
    with open("input", "r") as file:
        bossStats = dict(((name, int(value)) for name, value in (
            line.strip().split(": ") for line in file.readlines())))

    playerHealth = 100

    nothing = [[0, 0, 0]]

    weapons = [[8, 4, 0],
               [10, 5, 0],
               [25, 6, 0],
               [40, 7, 0],
               [74, 8, 0]]

    mails = [[13, 0, 1],
             [31, 0, 2],
             [53, 0, 3],
             [75, 0, 4],
             [102, 0, 5]]

    rings = [[25, 1, 0],
             [50, 2, 0],
             [100, 3, 0],
             [20, 0, 1],
             [40, 0, 2],
             [80, 0, 3]]

    twoRings = list(list(map(add, f, s)) for f, s in combinations(rings, 2))

    minCost = 1000
    for weaponCost, weaponDmg, _ in weapons:
        for mailCost, _, mailArmour in nothing + mails:
            for ringCost, ringDmg, ringArmour in nothing + rings + twoRings:
                cost = weaponCost + mailCost + ringCost
                health = playerHealth
                dmg = weaponDmg + ringDmg
                armour = mailArmour + ringArmour

                bossHealth = bossStats["Hit Points"]
                bossDmg = bossStats["Damage"]
                bossArmour = bossStats["Armor"]

                hitsOnBoss = ceil(bossHealth / max(1, dmg - bossArmour))
                hitsOnPlayer = ceil(health / max(1, bossDmg - armour))

                if hitsOnBoss <= hitsOnPlayer:
                    minCost = min(cost, minCost)

    print(minCost)


if __name__ == "__main__":
    main()
