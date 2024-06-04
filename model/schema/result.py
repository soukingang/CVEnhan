#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   result.py
@Time    :   2024/06/03 11:46:35
@Author  :   Song榆钱儿
@description   :   （备用）
'''

from langchain.pydantic_v1 import BaseModel
from typing import Union
from .outputs import Project_Output_Schema, Job_Output_Schema

class Result_Schema(BaseModel):
    result: Union[Project_Output_Schema, Job_Output_Schema]