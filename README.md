# common-utils

TimeRangeScheduler:
Examples
--------
```
    >>> import datetime
    >>> from utils.ascheduler import TimeRangeScheduler
    >>> def say_hello(scheduler): print("hello ,times:%s,current_time:%s" %(scheduler.times,scheduler.current_time))
    >>> s_time=datetime.datetime.strptime("2016060112","%Y%m%d%H")
    >>> e_time=datetime.datetime.strptime("2016060123","%Y%m%d%H")
    >>> scheduler=TimeRangeScheduler(s_time,e_time,"hours",1)
    >>> scheduler.register_task_func(task_func=say_hello,task_func_args={"scheduler":scheduler})
    >>> scheduler.run()
    hello ,times:0,current_time:2016-06-01 12:00:00
    hello ,times:1,current_time:2016-06-01 13:00:00
    .....
    hello ,times:10,current_time:2016-06-01 22:00:00
    hello ,times:11,current_time:2016-06-01 23:00:00
    >>>
    >>> scheduler=TimeRangeScheduler(e_time,s_time,"hours",1)
    >>> scheduler.register_task_func(task_func=say_hello,task_func_args={"scheduler":scheduler})
    >>> scheduler.run()
    hello ,times:0,current_time:2016-06-01 23:00:00
    hello ,times:1,current_time:2016-06-01 22:00:00
    .....
    hello ,times:10,current_time:2016-06-01 13:00:00
    hello ,times:11,current_time:2016-06-01 12:00:00
    """
```

CommandExecutor:
Examples
--------
```
    >>> from utils.cmd import CommandResult
    >>> from utils.cmd import CommandExecutor
    >>> rc = CommandExecutor.system("ls -al *")
    >>> print(rc.stdout_text)
    >>> print(rc.stderr_text)
    >>> print(rc.status)
    >>> 
```

Rsync:
Examples
---------
```
    >>> from utils.rsync import Rsync
    >>> rsync = Rsync("counter96", "root", "192.168.7.96")
    >>> files=self.rsync.remote_files(include="counter.log-2016-06-15-2*",exclude="*")
    >>> print(files)
    >>> ["counter.log-2016-06-15-20","counter.log-2016-06-15-21","counter.log-2016-06-15-22","counter.log-2016-06-15-23"]
```


        

