from pathlib import Path

import pytest

from hash_all import hash_all
from hash_all import HASH_LEN


def test_simple_example(fs):
    sentance = "This file contains one sentance"
    with open("alpha.txt", "w") as writer:
        writer.write(sentance)
    assert Path("alpha.txt").exists()
    with open("alpha.txt", "r") as reader:
        assert reader.read() == sentance


@pytest.fixture
def our_fs(fs):
    fs.create_file("a.txt", contents="aaa")
    fs.create_file("b.txt", contents="bbbbb")
    fs.create_file("sub_dir/c.txt", contents="ccccc")


def test_nested_example(our_fs):
    assert Path("a.txt").exists()
    assert Path("b.txt").exists()
    assert Path("sub_dir/c.txt").exists()


def test_deletion_example(our_fs):
    assert Path("a.txt").exists()
    Path("a.txt").unlink()
    assert not Path("a.txt").exists()


def test_hashing(our_fs):
    result = hash_all(".")
    expected = {"a.txt", "b.txt", "sub_dir/c.txt"}
    assert {r[0] for r in result} == expected
    assert all(len(r[1]) == HASH_LEN for r in result)


def test_change(our_fs):
    original = hash_all(".")
    original = [entry for entry in original if entry[0] == "a.txt"][0]
    with open("a.txt", "w") as writer:
        writer.write("this is new content for a.txt")
    changed = hash_all(".")
    changed = [entry for entry in changed if entry[0] == "a.txt"][0]
    assert original != changed
