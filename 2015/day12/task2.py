from json import loads
import re


def main():
    with open("input", "r") as file:
        data = file.read()

    def obj_hook(obj):
        if "red" in obj.values():
            return {}
        else:
            return obj

    print(sum((int(x) for x in
          re.findall("-?\d+", str(loads(data, object_hook=obj_hook))))))


if __name__ == "__main__":
    main()
