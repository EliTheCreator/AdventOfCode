import re


def main():
    with open("input", "r") as file:
        replacementsRaw, molecule = (part.strip()
                                     for part in file.read().split("\n\n"))

    replacements = [line.split(" => ") for line in replacementsRaw.split("\n")]

    newMolecules = set()
    for atom, replacement in replacements:
        for match in re.finditer(atom, molecule):
            newMolecules.add(molecule[:match.start()] +
                             replacement + molecule[match.end():])

    print(len(newMolecules))


if __name__ == "__main__":
    main()
