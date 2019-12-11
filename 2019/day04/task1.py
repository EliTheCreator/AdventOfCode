import re

def main():
    file = open("input", "r")
    mmin, mmax, *_ = [int(x) for x in re.findall("[0-9]+", file.readline())]
    file.close()

    count = 0
    



main()