# !/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

UTILS_PATH = '/Users/vamshikrishnarasabathula/Documents/git/python_github_actions_example/src'
INIT_FILE = '{}/'.format(UTILS_PATH)
sys.path.insert(0, '{}'.format(INIT_FILE))

from app import index


def test_index():
    assert index() == "Welcomr to my first flask app"

