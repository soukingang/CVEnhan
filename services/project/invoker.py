#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   invoker.py
@Time    :   2024/06/03 16:11:13
@Author  :   Song榆钱儿
@description   :   项目经历处理模块
'''

from model.enum import Chat_MODEL
from model.prompts.base import Project_Prompts
from services.base.dealwith import DealWith
from model.schema.outputs import project_output_parser, project_analysis_output_parser
from fastapi import APIRouter
from model.schema.inputs import Project_Input_Schema
from model.response.datas import Project_Response
from langchain_core.output_parsers import StrOutputParser
import traceback

project = APIRouter()
class Invoker(DealWith):
    def __init__(self, model: Chat_MODEL=Chat_MODEL.QianfanChat,
                 prompt_type: Project_Prompts=None,
                 params: dict={},
                 parser=project_output_parser):
        prompt = getattr(Project_Prompts, prompt_type)
        super().__init__(model, prompt, params, parser)

parser_map = {
    "ANALYSIS": project_analysis_output_parser,
    "GENERATE": project_output_parser,
    "OPTIMIZATE": project_output_parser
}

@project.post("/process", response_model=Project_Response, response_model_exclude_unset=True)
async def process(data: Project_Input_Schema):
    try:
        res = await Invoker(prompt_type=data.type,
                            params=data.dict(),
                            parser=parser_map[data.type]
                            ).arun()
    except Exception:
        return Project_Response(result="fail", content=str(traceback.format_exc()))
    return Project_Response(result="success", content=res.dict())
