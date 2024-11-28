import re


class Range():
    def __init__(self, dest_start, src_start, length) -> None:
        self.dest_start = dest_start
        self.src_start = src_start
        self.length = length

    def translate(self, location):
        return location - self.src_start + self.dest_start

    def in_range(self, location):
        return self.src_start <= location < (self.src_start + self.length)


def main():
    with open("input", "r") as file:
        data = [block.split("\n") for block in file.read().split("\n\n")]

    seeds = [int(x) for x in re.findall(r"\d+", data[0][0])]
    category_map = {}
    category_ranges_map = {}
    for block in data[1:]:
        from_cat, to_cat = block[0].split(" ")[0].split("-")[::2]
        category_map[from_cat] = to_cat

        category_ranges = []
        for line in block[1:]:
            category_ranges.append(Range(*[
                int(x) for x in line.split(" ")
            ]))

        category_ranges.sort(key=lambda x: x.src_start)
        category_ranges_map[from_cat] = category_ranges

    targets = []
    for seed in seeds:
        target = seed
        category = "seed"
        while category in category_map:
            category_ranges = category_ranges_map[category]
            for r in category_ranges:
                if r.in_range(target):
                    target = r.translate(target)
                    break
            category = category_map[category]

        targets.append(target)

    print(min(targets))


if __name__ == "__main__":
    main()
