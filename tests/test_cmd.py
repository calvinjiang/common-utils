# coding=UTF-8

import unittest
import sys
import os
sys.path.append("..")
from utils.cmd import CommandResult
from utils.cmd import CommandExecutor

class TestCommandExecutorMethods(unittest.TestCase):
    def test_exec_command(self):
        rc = CommandExecutor.system("ls ")
        self.assertTrue(isinstance(rc, CommandResult),
                        "return value type error,not a CommandResult instance.")

   

if __name__ == '__main__':
    unittest.main()
