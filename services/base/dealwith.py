#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dealwith.py
@Time    :   2024/06/03 13:30:35
@Author  :   Song榆钱儿
@description   :   模型调用基类
'''

from model.enum import Chat_MODEL
from services.base.model import CVChatModel
from services.base.common import PromptInvoker
from langchain_core.prompts.base import BasePromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from utils.dealtime import deal_time

class DealWith:
    def __init__(self, model: Chat_MODEL,
                 prompt_template: BasePromptTemplate,
                 params: dict,
                 parser: JsonOutputParser):
        prompt = PromptInvoker(prompt_template, params)
        self.chain = prompt() | CVChatModel(model)() | parser
    
    @deal_time
    async def arun(self):
        try:
            return await self.chain.ainvoke({})
        except Exception as e:
            raise e
        
    # 方便测试使用
    def run(self):
        return self.chain.invoke({})