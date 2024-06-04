#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   invoker.py
@Time    :   2024/06/04 15:01:13
@Author  :   Song榆钱儿
@description   :   个人总结处理模块
'''

from model.enum import Chat_MODEL
from model.prompts.base import Summary_Prompts
from services.base.dealwith import DealWith
from model.schema.outputs import summary_output_parser, summary_analysis_output_parser
from fastapi import APIRouter
from model.schema.inputs import Summary_Input_Schema
from model.response.datas import Summary_Response
from langchain_core.output_parsers import StrOutputParser
import traceback

summary = APIRouter()
class Invoker(DealWith):
    def __init__(self, model: Chat_MODEL=Chat_MODEL.ChatTongyi,
                 prompt_type: Summary_Prompts=None,
                 params: dict={},
                 parser=summary_output_parser):
        prompt = getattr(Summary_Prompts, prompt_type)
        super().__init__(model, prompt, params, parser)

parser_map = {
    "ANALYSIS": summary_analysis_output_parser,
    "GENERATE": summary_output_parser,
    "OPTIMIZATE": summary_output_parser
}

@summary.post("/process", response_model=Summary_Response, response_model_exclude_unset=True)
async def process(data: Summary_Input_Schema):
    try:
        res = await Invoker(prompt_type=data.type,
                            params=data.model_dump(),
                            parser=parser_map[data.type]
                            ).arun()
    except Exception:
        return Summary_Response(result="fail", content=str(traceback.format_exc()))
    return Summary_Response(result="success", content=res.dict())