#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   inputs.py
@Time    :   2024/06/03 11:41:24
@Author  :   Song榆钱儿
@description   :   请求数据模型
'''

# from langchain.pydantic_v1 import BaseModel, Field
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date

from .baseInfo import (
    Customer_Info,
    Resume_Base_Info,
    Resume_Edu_Info,
    Job_Info,
    Project_Info
)

class Project_Input_Schema(BaseModel):
    type: Optional[str] = Field(description="请求类型：生成-GENERATE，优化-OPTIMIZATE，分析-ANALYSIS")
    start_time: Optional[date] = Field(description="开始时间", default=date.today())
    end_time: Optional[date] = Field(description="结束时间", default=date.today())
    company: Optional[str] = Field(description="公司名称", default="")
    project_name: Optional[str] = Field(description="项目名称", default="")
    project_role: Optional[str] = Field(description="项目角色", default="")
    project_desc: Optional[str] = Field(description="项目经历描述", default="")
    intend_position: Optional[str] = Field(description="意向岗位", default="")

class Job_Input_Schema(BaseModel):
    type: Optional[str] = Field(description="请求类型：生成-GENERATE，优化-OPTIMIZATE，分析-ANALYSIS")
    start_time: Optional[date] = Field(description="开始时间", default=date.today())
    end_time: Optional[date] = Field(description="结束时间", default=date.today())
    company: Optional[str] = Field(description="公司名称", default="")
    dept: Optional[str] = Field(description="部门", default="")
    title: Optional[str] = Field(description="职位", default="")
    job_desc: Optional[str] = Field(description="工作描述", default="")
    intend_position: Optional[str] = Field(description="意向岗位", default="")


# class Job_Input_Schema(BaseModel):
#     customer_info: Customer_Info
#     resume_base_info: Resume_Base_Info
#     resume_edu_info: Resume_Edu_Info
#     project_info: Project_Info

class Summary_Data(BaseModel):
    customer_info: Customer_Info
    resume_base_info: Resume_Base_Info
    resume_edu_info: List[Resume_Edu_Info]
    project_info: List[Project_Info]
    job_info: List[Job_Info]

class Summary_Input_Schema(BaseModel):
    type: Optional[str] = Field(description="请求类型：生成-GENERATE，优化-OPTIMIZATE，分析-ANALYSIS")
    content: Summary_Data
    summary: Optional[str] = Field(description="个人总结", default="")
    intend_position: Optional[str] = Field(description="意向岗位", default="")