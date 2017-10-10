#! /usr/bin/env python
# coding=UTF-8

import sys
import subprocess

if sys.version > '3':
    PY3 = True
else:
    PY3 = False


class CommandResult(object):
    """The class will be used to stored result of some methods in HivExecutor.

    Up to now the class only be used in the method of _execute_system_command
    in the class HiveExecutor.

    Attributes
    ----------
    stdout_text : str
        The result of standart out.
    stderr_text : str
        The result of standart error.
    status : int
        The status of system command returns.

    """

    def __init__(self, stdout_text, stderr_text, status):
        self.stdout_text = stdout_text
        self.stderr_text = stderr_text
        self.status = status

class CommandExecutor:
    
    @classmethod
    def system(cls,command):
        status = 0
        process = subprocess.Popen(
            command, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = process.communicate()
        status = process.poll()

        if PY3:
            if output:
                output=output.decode('utf-8')
            if err:
                err=err.decode('utf-8')

        return CommandResult(output, err, status)
