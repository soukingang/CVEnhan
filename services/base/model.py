#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   model.py
@Time    :   2024/06/03 14:08:35
@Author  :   Song榆钱儿
@description   :   引用模型包装类
'''

from typing import Any
from enum import Enum
from model.enum import Chat_MODEL
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_community.chat_models.ollama import ChatOllama
from langchain_community.chat_models.baidu_qianfan_endpoint import QianfanChatEndpoint

class CVChatModel:
    def __init__(self, model: Enum):
        self.model = model
    def __call__(self, *args: Any, **kwds: Any) -> BaseChatModel:
        if self.model == Chat_MODEL.ChatTongyi:
            return ChatTongyi(model="qwen-turbo")
        elif self.model == Chat_MODEL.ChatOllama:
            return ChatOllama(model="llama3")
        elif self.model == Chat_MODEL.QianfanChat:
            return QianfanChatEndpoint(model="ERNIE-3.5-8K", temperature=0.1)
        return ChatOpenAI()
