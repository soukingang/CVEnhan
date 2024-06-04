#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dealtime.py
@Time    :   2024/06/03 11:24:04
@Author  :   Song榆钱儿
@description   :   调用耗时统计工具
'''

import time
from functools import update_wrapper

def deal_time(func):
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(
            f"cost time {time.time() - start}, __Func__ {func.__name__}"
        )
        return result
    return update_wrapper(wrap, func)