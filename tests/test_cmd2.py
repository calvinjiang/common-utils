#! /usr/bin/env python
# coding=UTF-8

import unittest
import sys
import os
sys.path.append("..")
from utils.cmd import CommandResult
from utils.cmd import CommandExecutor

name=sys.argv[1]

def test_function():
    cnt=1
    while True:
        cnt=cnt+1
        print "%s---hello" %(name)
        if cnt % 5:
            raise Exception("%s--- errors" %(name))
        

CommandExecutor.system()