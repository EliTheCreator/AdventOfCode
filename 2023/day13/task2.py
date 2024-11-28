
def get_mirror(block: list[str]) -> int|None:
    v_mirrors = []
    for index, (line1, line2) in enumerate(zip(block, block[1:]), 1):
        if line1==line2:
            v_mirrors.append((index, False))
        elif sum(l!=r for l, r in zip(line1, line2)) == 1:
            v_mirrors.append((index, True))

    for v_mirror, found_smudge in v_mirrors:
        for d in range(1, min(len(block)-v_mirror, v_mirror)):
            if found_smudge:
                if block[v_mirror-1-d] != block[v_mirror+d]:
                    break
            else:
                if block[v_mirror-1-d] == block[v_mirror+d]:
                    continue
                elif sum(l!=r for l, r in zip(block[v_mirror-1-d], block[v_mirror+d])) == 1:
                    found_smudge = True
                else:
                    break

        else:
            if found_smudge:
                return v_mirror

    return None


def main():
    with open("input", "r") as file:
        data = [block.split("\n") for block in file.read().split("\n\n")]

    total = 0
    for block in data:
        mirror = get_mirror(block)
        if mirror != None:
            total += mirror*100
            continue

        transposed_block = ["" for _ in range(len(block[0]))]
        for col in range(len(block[0])):
            for row in range(len(block)):
                transposed_block[col] += block[row][col]

        mirror = get_mirror(transposed_block)
        if mirror != None:
            total += mirror

    print(total)

if __name__ == "__main__":
    main()
