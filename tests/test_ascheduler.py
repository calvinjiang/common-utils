#! /usr/bin/env python
# coding=UTF-8

import sys
import unittest
import time
import datetime
import logging
sys.path.append("..")
from utils.ascheduler import TimeAfterTimeScheduler
from utils.ascheduler import TimeRangeScheduler
from utils.errors import FunctionReturnsValueError
from utils.errors import FunctionMissingReturnsValueError


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

class TestTimeAfterTimeSchedulerMethods(unittest.TestCase):

    def condition_func(self):
        return self.value==1

    def terminal_func(self):
        return self.value==0

    def action_func(self):
        print "hello %s" % (time.time())
        self.value=self.value+1
        return True

    def task_func_failed(self,scheduler):
        print "hello %s" %(scheduler.current_time)
        return False

    def setUp(self):
        self.value=0

    def test_basic_functionality(self):
        self.value=0
        s = TimeAfterTimeScheduler(delay_time=0, max_times=3)
        s.register_task_func(self.action_func)
        s.run()
        self.assertEqual(3,s.times,"the max times didn't work well.")

    def test_functionality_with_condition(self):
        self.value=0
        s = TimeAfterTimeScheduler(delay_time=0, max_times=5)
        s.register_task_func(self.action_func,self.condition_func)
        s.run()
        self.assertEqual(5,s.times,"the max times didn't work well.")

    def test_errors(self):
        self.value=0
        s = TimeAfterTimeScheduler(delay_time=0, max_times=5)
        self.assertRaises(TypeError,s.register_task_func,"task","condition")

    def test_task_failed_mode(self):
        self.value=0
        start_time=datetime.datetime.strptime("2016070523","%Y%m%d%H")
        end_time=datetime.datetime.strptime("2016070520","%Y%m%d%H")
        s = TimeAfterTimeScheduler(delay_time=0, max_times=3,task_failed_mode='skip')

        s.register_task_func(self.task_func_failed)
        s.run()
        self.assertEqual(3,s.times,"This process is terminal.")

   
class TimeRangeSchedulerMethods(unittest.TestCase):

    def condition_func(self):
        return self.value==1

    def terminal_func(self):
        return self.value==0

    def action_func(self,scheduler):
        print "hello %s" % (scheduler.current_time)
        return True

    def task_func(self,scheduler):
        print "hello %s" %(scheduler.current_time)

    def task_func_returns_error_type(self,scheduler):
        print "hello %s" %(scheduler.current_time)
        return 1

    def task_func_failed(self,scheduler):
        print "hello %s" %(scheduler.current_time)
        return False

    def setUp(self):
        self.value=0

    def test_basic_functionality(self):
        self.value=0
        start_time=datetime.datetime.strptime("2016070523","%Y%m%d%H")
        end_time=datetime.datetime.strptime("2016070520","%Y%m%d%H")
        s = TimeRangeScheduler(start_time,end_time,'hours',1,delay_time=0, max_times=3)

        s.register_task_func(self.action_func,{"scheduler":s})
        s.run()
        self.assertEqual(3,s.times,"the max times didn't work well.")

    def test_errors(self):
        self.value=0
        start_time=datetime.datetime.strptime("2016070523","%Y%m%d%H")
        end_time=datetime.datetime.strptime("2016070520","%Y%m%d%H")
        s = TimeRangeScheduler(start_time,end_time,'hours',1,delay_time=0, max_times=3)
        self.assertRaises(TypeError,s.register_task_func,"task","not dict","condition","terminal")

    def test_perform_function_errors(self):
        self.value=0
        start_time=datetime.datetime.strptime("2016070523","%Y%m%d%H")
        end_time=datetime.datetime.strptime("2016070520","%Y%m%d%H")
        s = TimeRangeScheduler(start_time,end_time,'hours',1,delay_time=0, max_times=3)

        s.register_task_func(self.task_func,{"scheduler":s})
        s.run()
        self.assertEqual(1,s.times,"This process is terminal.")

        self.value=0
        start_time=datetime.datetime.strptime("2016070523","%Y%m%d%H")
        end_time=datetime.datetime.strptime("2016070520","%Y%m%d%H")
        s = TimeRangeScheduler(start_time,end_time,'hours',1,delay_time=0, max_times=3)

        s.register_task_func(self.task_func_returns_error_type,{"scheduler":s})
        s.run()
        self.assertEqual(1,s.times,"This process is terminal.")
        
    def test_task_failed_mode(self):
        self.value=0
        start_time=datetime.datetime.strptime("2016070523","%Y%m%d%H")
        end_time=datetime.datetime.strptime("2016070520","%Y%m%d%H")
        s = TimeRangeScheduler(start_time,end_time,'hours',1,delay_time=0, max_times=3,task_failed_mode='skip')

        s.register_task_func(self.task_func_failed,{"scheduler":s})
        s.run()
        self.assertEqual(3,s.times,"This process is terminal.")

if __name__ == '__main__':
    unittest.main()
