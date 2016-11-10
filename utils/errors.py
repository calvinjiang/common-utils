#! /usr/bin/env python
# coding=UTF-8
"""Core exceptions raised by the package of common-utils."""

class CommonUtilsError(Exception):
    pass

class SystemCommandExecuteError(CommonUtilsError):
    pass

class UnSupportedMethodError(CommonUtilsError):
    pass

class ConnectTimeoutError(CommonUtilsError):
    pass

class TransferFilesError(CommonUtilsError):
    pass

class FunctionReturnsValueError(CommonUtilsError):
    pass

class TaskFunctionExecutedError(CommonUtilsError):
    pass

class FunctionMissingReturnsValueError(FunctionReturnsValueError):
    pass

class FunctionReturnsValueTypeError(FunctionReturnsValueError):
    pass