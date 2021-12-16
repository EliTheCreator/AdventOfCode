from copy import copy


class Player():
    def __init__(self, health: int, mana: int, armour: int):
        self.health = health
        self.mana = mana
        self.armour = armour


class Spell():
    def __init__(self, cost, duration, dmg, armour, health, mana):
        self.cost = cost
        self.duration = duration
        self.dmg = dmg
        self.armour = armour
        self.health = health
        self.mana = mana


class Boss():
    def __init__(self, health: int, dmg: int):
        self.health = health
        self.dmg = dmg


# cost, duration, dmg, armour, health, mana
spells = (
    Spell(229, 5, 0, 0, 0, 101),
    Spell(173, 6, 3, 0, 0, 0),
    Spell(113, 6, 0, 7, 0, 0),
    Spell(53, 0, 4, 0, 0, 0),
    Spell(73, 0, 2, 0, 2, 0),
)

minCost = 100000


def applyEffects(player: Player, boss: Boss, activeSpells):
    for activeSpellId, remainingDuration in enumerate(activeSpells):
        if remainingDuration:
            effectSpell = spells[activeSpellId]
            player.health += effectSpell.health
            player.mana += effectSpell.mana
            if effectSpell.armour:
                if remainingDuration == effectSpell.duration:
                    player.armour += effectSpell.armour
                elif remainingDuration == 1:
                    player.armour -= effectSpell.armour

            boss.health -= effectSpell.dmg

            activeSpells[activeSpellId] -= 1


def battle(player: Player, boss: Boss, activeSpells, spellId, cost):
    global minCost
    ##### Player Round #####
    ### Effects ###
    applyEffects(player, boss, activeSpells)

    if boss.health <= 0:
        minCost = min(cost, minCost)
        return

    ### Player Casts Spell ###
    spell = spells[spellId]
    if spell.cost <= player.mana and not activeSpells[spellId]:
        cost += spell.cost
        if cost > minCost:
            return
        player.mana -= spell.cost
        if spell.duration:
            activeSpells[spellId] = spell.duration
        else:
            player.health += spell.health
            player.mana += spell.mana
            player.armour += spell.armour
            boss.health -= spell.dmg
    else:
        return

    if boss.health <= 0:
        minCost = min(cost, minCost)
        return

    ##### Boss Round #####
    applyEffects(player, boss, activeSpells)

    if boss.health <= 0:
        minCost = min(cost, minCost)
        return

    ### Boss Attacks ###
    player.health -= max(1, boss.dmg - player.armour)

    if player.health <= 0:
        return

    for nextSpell in range(len(spells)):
        battle(copy(player), copy(boss),
               activeSpells.copy(), nextSpell, cost)


def main():
    filename = "input"
    with open(filename, "r") as file:
        bossStats = dict(((name, int(value)) for name, value in (
            line.strip().split(": ") for line in file.readlines())))

    playerBaseHealth = 50
    playerBaseMana = 500
    playerBaseArmour = 0
    if filename == "example":
        playerBaseHealth = 10
        playerBaseMana = 250

    bossBaseHealth = bossStats["Hit Points"]
    bossBaseDmg = bossStats["Damage"]

    player = Player(playerBaseHealth, playerBaseMana, playerBaseArmour)
    boss = Boss(bossBaseHealth, bossBaseDmg)
    for startingSpell in range(len(spells)):
        battle(copy(player), copy(boss),
               [0 for _ in range(len(spells))], startingSpell, 0)

    print(minCost)


if __name__ == "__main__":
    main()
