#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   invoker.py
@Time    :   2024/06/03 19:00:59
@Author  :   Song榆钱儿
@description   :   工作经历处理模块
'''

from model.enum import Chat_MODEL
from services.base.model import CVChatModel
from model.prompts.base import Job_Prompts
from services.base.dealwith import DealWith
from model.schema.outputs import job_output_parser, job_analysis_output_parser
from fastapi import APIRouter
from model.schema.inputs import Job_Input_Schema
from model.response.datas import Job_Response
from langchain.output_parsers import OutputFixingParser
import traceback

job = APIRouter()

class Invoker(DealWith):
    def __init__(self, model: Chat_MODEL=Chat_MODEL.QianfanChat,
                 prompt_type: Job_Prompts=None,
                 params: dict={},
                 parser=job_output_parser):
        prompt = getattr(Job_Prompts, prompt_type)
        super().__init__(model, prompt, params, parser)

parser_map = {
    "ANALYSIS": job_analysis_output_parser,
    "GENERATE": job_output_parser,
    "OPTIMIZATE": job_output_parser
}

@job.post("/process", response_model=Job_Response, response_model_exclude_unset=True)
async def process(data: Job_Input_Schema):
    try:
        res = await Invoker(prompt_type=data.type,
                            params=data.dict(),
                            parser=parser_map[data.type]
                            ).arun()
    except Exception:
        return Job_Response(result="fail", content=str(traceback.format_exc()))
    return Job_Response(result="success", content=res.dict())
