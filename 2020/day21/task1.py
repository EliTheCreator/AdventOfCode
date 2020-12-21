import re
from collections import defaultdict


def main():
    file = open("input", "r")
    raw_ingredient_lists, raw_allergen_lists = zip(
        *[line.strip().split("(contains", maxsplit=1) for line in file.readlines()])
    file.close()

    ingredient_lists = [set(re.findall(r"\w+", line))
                        for line in raw_ingredient_lists]
    allergen_lists = [re.findall(r"\w+", line)
                      for line in raw_allergen_lists]

    all_ingredients = set().union(*ingredient_lists)
    ingredient_per_allergen = defaultdict(lambda: set())

    for num, allergen_list in enumerate(allergen_lists):
        for allergen in allergen_list:
            ingredient_per_allergen[allergen].add(num)

    possible_ingredients = []
    for key in ingredient_per_allergen.keys():
        possible_ingredient = all_ingredients.copy()
        for num in ingredient_per_allergen[key]:
            possible_ingredient.intersection_update(ingredient_lists[num])

        possible_ingredients.append((key, possible_ingredient))

    # translations = {}
    allergen_ingredients = set()
    while possible_ingredients:
        m = min(possible_ingredients, key=lambda x: len(x[1]))
        possible_ingredients.remove(m)
        for i in possible_ingredients:
            i[1].difference_update(m[1])

        # translations[m[0]] = m[1].pop()
        allergen_ingredients.add(m[1].pop())

    s = 0
    for ingredient_list in ingredient_lists:
        s += len(ingredient_list) - \
            len(ingredient_list.intersection(allergen_ingredients))

    print(s)


if __name__ == "__main__":
    main()
