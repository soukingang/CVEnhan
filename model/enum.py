#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   enum.py
@Time    :   2024/06/03 13:27:50
@Author  :   Song榆钱儿
@description   :   模型枚举
'''

from enum import Enum

class Chat_MODEL(Enum):
    ChatTongyi = "ChatTongyi"
    ChatOllama = "ChatOllama"
    ChatOpenAI = "ChatOpenAI"
    QianfanChat = "QianfanChat"