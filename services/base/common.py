#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   interface.py
@Time    :   2024/06/03 13:15:50
@Author  :   Song榆钱儿
@description   :   通用方法
'''

from langchain_core.prompts.base import BasePromptTemplate
from langchain_core.prompts import ChatPromptTemplate

class PromptInvoker:
    def __init__(self, prompt: BasePromptTemplate, params: dict):
        self.prompt = prompt
        self.params = params
    
    def __call__(self) -> ChatPromptTemplate:
        return self.prompt.partial(**self.params)
