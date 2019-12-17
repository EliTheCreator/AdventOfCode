import collections
import re


def recr(recipes: dict, product: str, amount: int, overhead: dict):
    oreSum = 0
    ingredients = recipes[product][1]
    for numNeeded, name in ingredients:
        numNeeded *= amount
        if name != "ORE":
            inStore = overhead[name]
            if inStore >= numNeeded:
                overhead[name] = inStore - numNeeded
            else:
                perRecipe = recipes[name][0]
                i = numNeeded // perRecipe
                if i * perRecipe + inStore <= numNeeded:
                    i += 1
                total = inStore + i * perRecipe
                overhead[name] = total - numNeeded
                oreSum += recr(recipes, name, i, overhead)

            # oreSum += recr(recipes, name, overhead)
        else:
            oreSum += numNeeded

    return oreSum


def main():
    file = open("input", "r")
    data = [[recipe.split() for recipe in re.findall(
        r"\d+ [A-Z]+", line)] for line in file]
    file.close()

    recipes = {}
    for recipe in data:
        num, product = recipe[-1]
        num = int(num)
        ingredients = set()
        for ingredient in recipe[:-1]:
            ingredients.add((int(ingredient[0]), ingredient[1]))
        recipes[product] = (num, ingredients)

    maxFuel = 2509000
    while recr(recipes, "FUEL", maxFuel, collections.defaultdict(lambda: 0)) < 1000000000000:
        maxFuel += 1
    print(maxFuel-1)

    # print(recr(recipes, "FUEL", 2509000, collections.defaultdict(lambda: 0)))
    # print(recipes.items())
    # for name, (num, ingredients) in recipes.items():
    #     print(num, name, ingredients)


if __name__ == "__main__":
    main()
