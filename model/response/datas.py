#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   datas.py
@Time    :   2024/06/03 12:17:47
@Author  :   Song榆钱儿
@description   :   response数据模型
'''
from pydantic import BaseModel
from typing import Optional, Union

class Project_Response(BaseModel):
    result: str
    content: Union[str,dict]
    err_message: Optional[str] = None

class Job_Response(BaseModel):
    result: str
    content: Union[str,dict]
    err_message: Optional[str] = None

class Summary_Response(BaseModel):
    result: str
    content: Union[str,dict]
    err_message: Optional[str] = None