#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   inputs.py
@Time    :   2024/06/03 11:26:06
@Author  :   Song榆钱儿
@description   :   基础的数据模型
'''

from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class Customer_Info(BaseModel):
    customer_name: Optional[str] = Field(description="姓名", default="")


class Resume_Base_Info(BaseModel):
    intend_city: Optional[str] = Field(description="意向城市", default="")
    intend_position: Optional[str] = Field(description="意向岗位", default="")

class Resume_Edu_Info(BaseModel):
    school_name: Optional[str] = Field(description="学校名称", default="")
    major: Optional[str] = Field(description="专业", default="")

class Job_Info(BaseModel):
    company_name: Optional[str] = Field(description="公司名称", default="")
    dept: Optional[str] = Field(description="部门", default="")
    title: Optional[str] = Field(description="职位", default="")
    start_time: Optional[date] = Field(description="开始时间", default=date.today())
    end_time: Optional[date] = Field(description="结束时间", default=date.today())
    job_desc: Optional[str] = Field(description="工作描述", default="")
    intend_position: Optional[str] = Field(description="意向岗位", default="")

class Project_Info(BaseModel):
    company_name: Optional[str] = Field(description="公司名称", default="")
    project_name: Optional[str] = Field(description="项目名称", default="")
    project_role: Optional[str] = Field(description="项目角色", default="")
    project_desc: Optional[str] = Field(description="项目经历描述", default="")
    start_time: Optional[date] = Field(description="开始时间", default=date.today())
    end_time: Optional[date] = Field(description="结束时间", default=date.today())
