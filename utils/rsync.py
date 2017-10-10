#! /usr/bin/env python
# coding=UTF-8

import sys
import re


if sys.version > '3':
    PY3 = True
else:
    PY3 = False

if PY3:
    from .errors import SystemCommandExecuteError
    from .errors import UnSupportedMethodError
    from .errors import TransferFilesError
    from .cmd import CommandExecutor as ce
    from .cmd import CommandResult
else:
    from errors import SystemCommandExecuteError
    from errors import UnSupportedMethodError
    from errors import TransferFilesError
    from cmd import CommandExecutor as ce
    from cmd import CommandResult


class Rsync:

    def __init__(self, module_name, user, host, port=873):
        self.user = user
        self.host = host
        self.port = port
        self.module_name = module_name
        self.remote_rsync_module = "rsync://%s@%s:%s/%s" % (
            self.user, self.host, self.port, self.module_name)

    def test_connect(self, connect_timeout=2):
        cmd = "rsync -avu --contimeout %s %s" % (
            connect_timeout, self.remote_rsync_module)
        if self.version_number() >= 30:
            cr = ce.system(cmd)
            if cr.status == 0:
                return True
        else:
            raise UnSupportedMethodError(
                "the current version of rsync hasn't `contimeout` option.")
        return False

    def version(self):
        command = "rsync --version | grep version"
        cr = ce.system(command)
        if cr.status != 0:
            raise SystemCommandExecuteError(
                "the command %s failed! Error Info:%s" % (command, cr.stderr_text))

        return cr.stdout_text.strip()

    def version_number(self):
        version_info = self.version()
        if version_info:
            sequences = re.split("\s+", version_info)
            if len(sequences) >= 6:
                try:
                    return int(sequences[5])
                except ValueError:
                    return None
        return None

    def transfer_from_remote(self, local_dir, include=None, exclude=None, delete_excluded=False):
        if delete_excluded:
            delete_excluded = "--delete-excluded"
        else:
            delete_excluded = ""

        if include:
            include = "--include=\"%s\"" % (include)
        else:
            include = ""
        if exclude:
            exclude = "--exclude=\"%s\"" % (exclude)
        else:
            exclude = ""

        cmd = "rsync -avu %s %s %s %s %s" % (delete_excluded,
                                             include, exclude, self.remote_rsync_module, local_dir)

        cr = ce.system(cmd)
        if cr.status==0:
            return True
        else:
            raise TransferFilesError(cr.stderr_text)
        return False

    def transfer_to_remote(self, local_dir, include=None, exclude=None, delete_excluded=False):
        if delete_excluded:
            delete_excluded = "--delete-excluded"
        else:
            delete_excluded = ""

        if include:
            include = "--include=\"%s\"" % (include)
        else:
            include = ""
        if exclude:
            exclude = "--exclude=\"%s\"" % (exclude)
        else:
            exclude = ""

        cmd = "rsync -avu %s %s %s %s %s" % (delete_excluded,
                                             include, exclude, local_dir, self.remote_rsync_module)

        cr = ce.system(cmd)
        if cr.status==0:
            return True
        else:
            raise TransferFilesError(cr.stderr_text)
        return False

    def remote_files(self, include=None, exclude=None):
        if include:
            include = "--include=\"%s\"" % (include)
        else:
            include = ""
        if exclude:
            exclude = "--exclude=\"%s\"" % (exclude)
        else:
            exclude = ""

        cmd = "rsync --list-only %s %s %s" % (
            include, exclude, self.remote_rsync_module)

        cr = ce.system(cmd)
        files = []
        if cr.status == 0:
            for file in cr.stdout_text.split("\n"):
                fields = re.split("\s+", file.strip())
                if fields[-1] != "." and fields[-1] != "":
                    files.append(fields[-1])
        return files
