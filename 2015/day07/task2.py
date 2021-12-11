from enum import Enum
from functools import reduce


class OP(Enum):
    AND = 0
    OR = 1
    LSHIFT = 2
    RSHIFT = 3
    NOT = 4
    FORWARD = 5


class Operand():
    pass


class Node:
    def __init__(self, name: str, op: OP, inWireL: Operand = None, outWire: Operand = None, inWireR: Operand = None, amount=0):
        self.name = name
        self.op = op
        self.comingIn = set()
        self.goingOut = set()
        self.amount = amount

        if inWireL is not None:
            self.comingIn.add(inWireL)
        if inWireR is not None:
            self.comingIn.add(inWireR)
        if outWire is not None:
            self.goingOut.add(outWire)

    def __str__(self):
        return f"{self.name}: {self.comingIn} {self.op} {self.goingOut}"


class Graph:
    def __init__(self):
        self.wires: dict[str, int] = {}
        self.nodes: set[Node] = set()


class Constant(Operand):
    def __init__(self, value: int):
        self.value = value

    def __str__(self):
        return str(self.value)

    def get_val(self) -> int:
        return self.value

    def set_val(self, value):
        self.value = value


class Wire(Operand):
    def __init__(self, graph: Graph, name: str):
        self.graph = graph
        self.name = name
        if name not in self.graph.wires:
            self.graph.wires[name] = 0

    def __str__(self):
        return self.name

    def get_val(self) -> int:
        return self.graph.wires[self.name]

    def set_val(self, value: int):
        self.graph.wires[self.name] = value


def parse_operand(graph: Graph, oprnd: str) -> Operand:
    try:
        value = int(oprnd)
        return Constant(value)
    except ValueError:
        return Wire(graph, oprnd)


def main():
    graph = Graph()
    with open("input", "r") as file:
        for line in file.readlines():
            match line.strip().split(" "):
                case inOprnd, "->", inResult:
                    oprnd = parse_operand(graph, inOprnd)
                    result = parse_operand(graph, inResult)
                    nodeName = "".join([inOprnd, "FOREWARD", inResult])
                    node = Node(nodeName, OP.FORWARD, oprnd, result)
                    graph.nodes.add(node)

                case inOprndL, "AND", inOprndR, "->", inResult:
                    oprndL = parse_operand(graph, inOprndL)
                    oprndR = parse_operand(graph, inOprndR)
                    result = parse_operand(graph, inResult)
                    nodeName = "".join([inOprndL, "AND", inOprndR, inResult])
                    node = Node(nodeName, OP.AND, oprndL, result, oprndR)
                    graph.nodes.add(node)

                case inOprndL, "OR", inOprndR, "->", inResult:
                    oprndL = parse_operand(graph, inOprndL)
                    oprndR = parse_operand(graph, inOprndR)
                    result = parse_operand(graph, inResult)
                    nodeName = "".join([inOprndL, "OR", inOprndR, inResult])
                    node = Node(nodeName, OP.OR, oprndL, result, oprndR)
                    graph.nodes.add(node)

                case inOprnd, "LSHIFT", amount, "->", inResult:
                    oprnd = parse_operand(graph, inOprnd)
                    result = parse_operand(graph, inResult)
                    nodeName = "".join([inOprnd, "LSHIFT", inResult])
                    node = Node(nodeName, OP.LSHIFT, oprnd,
                                result, None, int(amount))
                    graph.nodes.add(node)

                case inOprnd, "RSHIFT", amount, "->", inResult:
                    oprnd = parse_operand(graph, inOprnd)
                    result = parse_operand(graph, inResult)
                    nodeName = "".join([inOprnd, "RSHIFT", inResult])
                    node = Node(nodeName, OP.RSHIFT, oprnd,
                                result, None, int(amount))
                    graph.nodes.add(node)

                case "NOT", inOprnd, "->", inResult:
                    oprnd = parse_operand(graph, inOprnd)
                    result = parse_operand(graph, inResult)
                    nodeName = "".join([inOprnd, "NOT", inResult])
                    node = Node(nodeName, OP.NOT, oprnd, result)
                    graph.nodes.add(node)

                case _ as ins:
                    print(f"Unknown instruction {ins} encountered")

    simulate(graph)
    firstRoundA = graph.wires["a"]
    for node in graph.nodes:
        if node.name == "44430FOREWARDb":
            list(node.comingIn)[0].set_val(firstRoundA)
    simulate(graph)
    print(graph.wires["a"])


def simulate(graph: Graph):
    for _ in range(len(graph.nodes)):
        for node in graph.nodes:
            match node.op:
                case OP.FORWARD:
                    incoming = list(node.comingIn)[0]
                    value = incoming.get_val()
                    for wire in node.goingOut:
                        wire.set_val(value)
                case OP.AND:
                    value = reduce(lambda w1, w2: w1.get_val() &
                                   w2.get_val(), node.comingIn)
                    for wire in node.goingOut:
                        wire.set_val(value)
                case OP.OR:
                    value = reduce(lambda w1, w2: w1.get_val() |
                                   w2.get_val(), node.comingIn)
                    for wire in node.goingOut:
                        wire.set_val(value)
                case OP.LSHIFT:
                    incoming = list(node.comingIn)[0]
                    value = incoming.get_val() << node.amount
                    for wire in node.goingOut:
                        wire.set_val(value)
                case OP.RSHIFT:
                    incoming = list(node.comingIn)[0]
                    value = incoming.get_val() >> node.amount
                    for wire in node.goingOut:
                        wire.set_val(value)
                case OP.NOT:
                    incoming = list(node.comingIn)[0]
                    value = 65535 - incoming.get_val()
                    for wire in node.goingOut:
                        wire.set_val(value)
                case _:
                    print("error")


if __name__ == "__main__":
    main()
