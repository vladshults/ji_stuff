import pytest


def reflection(d):
    return {k: v for v, k in d.items()}


def test_simple_negative():
    assert reflection({"one": 1, "two": 2}) != {1: "on", 2: "two"}


def test_simple_positive():
    assert reflection({"one": 1, "two": 2}) == {1: "one", 2: "two"}
