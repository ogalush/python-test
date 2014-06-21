#!/usr/bin/python3

from nose.tools import ok_

def test_is_prime():
    for num in [3, 5]:
        yield ok_, is_prime(num)
