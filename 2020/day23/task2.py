import re


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.value}"


def main():
    file = open("input", "r")
    input_cups = [int(x) for x in re.findall(r"\d", file.readline())]
    file.close()

    number_of_cups = 1000000
    number_of_moves = 10000000

    cups = [Node(n) for n in range(0, number_of_cups + 1)]
    for n in range(10, number_of_cups):
        cups[n].right = cups[n+1]
        cups[n+1].left = cups[n]

    cups[input_cups[0]].left = cups[number_of_cups]
    cups[number_of_cups].right = cups[input_cups[0]]
    cups[input_cups[-1]].right = cups[10]
    cups[10].left = cups[input_cups[-1]]

    for n in range(len(input_cups) - 1):
        cups[input_cups[n]].right = cups[input_cups[n+1]]
        cups[input_cups[n+1]].left = cups[input_cups[n]]

    current_cup = cups[input_cups[0]]
    for _ in range(number_of_moves):
        # get the three cups to the right of the current cup
        a = current_cup.right
        b = a.right
        c = b.right

        # remove the three cups from the circle
        current_cup.right = c.right
        current_cup.right.left = current_cup

        # select the destinatino cup
        destination_value = ((current_cup.value - 2) % number_of_cups) + 1

        values = [x.value for x in (a, b, c)]
        while destination_value in values:
            destination_value = ((destination_value - 2) % number_of_cups) + 1

        destination_cup = cups[destination_value]

        # place the three cups back into the circle immediately to
        # the right of the destination cup
        c.right = destination_cup.right
        c.right.left = c
        a.left = destination_cup
        destination_cup.right = a

        # select the new current cup
        current_cup = current_cup.right

    print(cups[1].right.value * cups[1].right.right.value)


if __name__ == "__main__":
    main()
