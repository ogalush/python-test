#!/usr/bin/python3

import sys
sys.path.append('/var/lib/jenkins/jobs/Python-test/workspace')
import hello

from nose.tools import ok_

def test_is_prime():
    for num in [3, 5]:
        yield ok_, is_prime(num)
