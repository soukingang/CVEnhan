#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   outputs.py
@Time    :   2024/06/03 11:44:16
@Author  :   Song榆钱儿
@description   :   输出格式化（备用）
'''

from langchain.pydantic_v1 import BaseModel, Field
from typing import Optional, List, Dict, Any
from langchain_core.output_parsers import PydanticOutputParser

class Job_Output_Schema(BaseModel):
    # job_desc: List[str] = Field(description="工作的详细描述内容")
    duty: List[str] = Field(description="核心职责的详细描述内容")
    contribution: List[str] = Field(description="主要贡献、价值体现的详细描述内容")

class Job_Analysis_Output_Schema(BaseModel):
    suggestion: List[str] = Field(description="修改分析建议的详细描述内容")
    improvement: List[str] = Field(description="改进方案的详细描述内容")

class Project_Output_Schema(BaseModel):
    # project_desc: List[str] = Field(description="项目的详细描述内容")
    duty: List[str] = Field(description="核心职责的详细描述内容")
    contribution: List[str] = Field(description="主要贡献、价值体现的详细描述内容")

class Project_Analysis_Output_Schema(BaseModel):
    suggestion: List[str] = Field(description="修改分析建议的详细描述内容")
    improvement: List[str] = Field(description="改进方案的详细描述内容")

class Summary_Output_Schema(BaseModel):
    summary: List[str] = Field(description="总结内容")

class Summary_Analysis_Output_Schema(BaseModel):
    suggestion: List[str] = Field(description="修改分析建议的详细描述内容")
    improvement: List[str] = Field(description="改进方案的详细描述内容")

project_output_parser = PydanticOutputParser(pydantic_object=Project_Output_Schema)
project_analysis_output_parser = PydanticOutputParser(pydantic_object=Project_Analysis_Output_Schema)
job_output_parser = PydanticOutputParser(pydantic_object=Job_Output_Schema)
job_analysis_output_parser = PydanticOutputParser(pydantic_object=Job_Analysis_Output_Schema)
summary_output_parser = PydanticOutputParser(pydantic_object=Summary_Output_Schema)
summary_analysis_output_parser = PydanticOutputParser(pydantic_object=Summary_Analysis_Output_Schema)







# for qwen-turbo
class _Analysis_Point(BaseModel):
    point: Dict = Field(description="建议点")
    # description: str = Field(description="改进内容")
    # type: str = Field(description="type")
    # content: dict = Field(description="改进")
    # experience_summary: Optional[str] = Field(description="experience_summary")

# for qwen-turbo
class _Analysis_Stragery(BaseModel):
    strategy: Dict = Field(description="改进点")

# for baidu
class _Analysis(BaseModel):
    title: str = Field(description="标题")
    description: str = Field(description="描述")
    properties: Dict = Field(description="属性")



    # for qwen-turbo
    # suggestion: _Analysis_Point = Field(description="修改建议")
    # improvement: _Analysis_Stragery = Field(description="改进方案")
    # suggestion: _Analysis = Field(description="修改建议")
    # improvement: _Analysis = Field(description="改进方案")    