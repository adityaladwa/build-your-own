import sys


def find_duplicate(filenames):
    matches = []
    for left in filenames:
        for right in filenames:
            if same_bytes(left, right):
                matches.append((left, right))
    return matches


def same_bytes(left_name, right_name):
    left_bytes = open(left_name, "rb").read()
    right_bytes = open(right_name, "rb").read()
    return left_bytes == right_bytes


if __name__ == "__main__":
    duplicates = find_duplicate(sys.argv[1:])
    for left, right in duplicates:
        print(left, right)
