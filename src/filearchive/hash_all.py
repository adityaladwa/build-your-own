from glob import glob
from hashlib import sha256
from pathlib import Path
from pprint import pprint

HASH_LEN = 16


def hash_all(root):
    result = []

    for name in glob("**/*.*", root_dir=root, recursive=True):
        full_name = Path(root, name)
        with open(full_name, "rb") as reader:
            data = reader.read()
            hash_code = sha256(data).hexdigest()[:HASH_LEN]
            result.append((name, hash_code))
    return result


if __name__ == "__main__":
    pprint(hash_all("../"))
