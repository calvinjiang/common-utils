#! /usr/bin/env python
# coding=UTF-8

import sys
import unittest
sys.path.append("..")

from utils.cmd import CommandExecutor as ce
from utils.rsync import Rsync
from utils.errors import UnSupportedMethodError
from utils.errors import ConnectTimeoutError

# rsync -avu --delete-excluded --include="counter.log-2016-06-14-*"
# --exclude="*" root@192.168.7.96::counter96 --list-only ./

# Requires:Rsync version 3.0.0

class TestRsyncMethods(unittest.TestCase):

    def setUp(self):
        #"root@192.168.7.96::counter96"
        self.rsync = Rsync("counter96", "root", "192.168.7.96")

    def tearDown(self):
        self.rsync = None

    def test_version(self):
        cr=ce.system("rsync --version | grep version")
        self.assertEqual(cr.stdout_text.strip(),self.rsync.version())

    def test_version_number(self):
        cr=ce.system("rsync --version | grep version")
        self.assertEqual(int(cr.stdout_text.strip().split(" ")[-1]),self.rsync.version_number())

    def test_test_connect(self):
        if self.rsync.version_number()>=30:
            rsync = Rsync("test", "test", "192.168.7.123")
            self.assertFalse(rsync.test_connect(2))
        else:
            self.assertRaises(UnSupportedMethodError,self.rsync.test_connect,2)

    def test_remote_files(self):
        if self.rsync.test_connect():
            files=self.rsync.remote_files(include="counter.log-2016-06-15-2*",exclude="*")
            self.assertEqual(files,["counter.log-2016-06-15-20","counter.log-2016-06-15-21","counter.log-2016-06-15-22","counter.log-2016-06-15-23"])

if __name__ == '__main__':
    unittest.main()
