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
    category_ranges_list: list[list[Range]] = []
    for block in data[1:]:
        category_ranges: list[Range] = []
        for line in block[1:]:
            category_ranges.append(Range(*[
                int(x) for x in line.split(" ")
            ]))

        category_ranges.sort(key=lambda x: x.src_start)
        category_ranges_list.append(category_ranges)

    for category_ranges in category_ranges_list:
        index = 0
        start_pos = 0
        while index < len(category_ranges):
            r = category_ranges[index]
            if start_pos < r.src_start:
                category_ranges.insert(index, Range(start_pos, start_pos, r.src_start-start_pos))
                index += 2
            else:
                index += 1
            start_pos = r.src_start + r.length
        start_pos = category_ranges[-1].src_start + category_ranges[-1].length
        if start_pos < 2**64:
            category_ranges.append(Range(start_pos, start_pos, 2**64-start_pos))

    for index in range(len(category_ranges_list)-1):
        first = category_ranges_list[index]
        first.sort(key=lambda x: x.dest_start)
        second = category_ranges_list[index+1]

        new_category_ranges: list[Range] = []
        i = 0
        j = 0
        while i<len(category_ranges_list[index]) and j < len(category_ranges_list[index+1]):
            cf = first[i]
            cs = second[j]
            if cf.dest_start+cf.length < cs.src_start+cs.length:
                new_category_ranges.append(Range(cs.dest_start, cf.src_start, cf.length))
                i += 1
                cs.dest_start += cf.length
                cs.src_start += cf.length
                cs.length -= cf.length
            elif cf.dest_start+cf.length > cs.src_start+cs.length:
                new_category_ranges.append(Range(cs.dest_start, cf.src_start, cs.length))
                j += 1
                cf.dest_start += cs.length
                cf.src_start += cs.length
                cf.length -= cs.length
            else:
                new_category_ranges.append(Range(cs.dest_start, cf.src_start, cf.length))
                i += 1
                j += 1

        category_ranges_list[index+1] = new_category_ranges

    category_ranges = category_ranges_list[-1]
    category_ranges.sort(key=lambda x: x.src_start)
    seed_ranges = list(zip(seeds, seeds[1:]))[::2]
    seed_ranges.sort(key=lambda x: x[0])
    seeds = []
    for start, length in seed_ranges:
        i = 0
        while True:
            cr = category_ranges[i]
            if cr.src_start + cr.length < start:
                i += 1
                continue

            if cr.src_start <= start < cr.src_start+cr.length:
                seeds.append(start)

            if start+length < cr.src_start+cr.length:
                break

            start, length = (cr.src_start+cr.length, start+length-cr.src_start-cr.length)
            i += 1


    targets = set()
    for seed in seeds:
        target = -1
        for r in category_ranges:
            if r.in_range(seed):
                target = r.translate(seed)
                break

        if target != -1:
            targets.add(target)

    print(min(targets))


if __name__ == "__main__":
    main()
