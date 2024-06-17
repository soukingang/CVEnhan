#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   inputs.py
@Time    :   2024/06/03 11:26:06
@Author  :   Song榆钱儿
@description   :   基础的数据模型
'''

from pydantic import BaseModel, Field, main
from datetime import date
from typing import Optional

class AllOptional(main.ModelMetaclass):
    def __new__(self, name, bases, namespaces, **kwargs):
        annotations = namespaces.get('__annotations__', {})
        for base in bases:
            annotations.update(base.__annotations__)
        for field in annotations:
            if not field.startswith('__'):
                annotations[field] = Optional[annotations[field]]
        namespaces['__annotations__'] = annotations
        return super().__new__(self, name, bases, namespaces, **kwargs)

#class Customer_Info(BaseModel):
#    customerName: Optional[str] = Field(description="姓名", default="")


class Resume_Base_Info(BaseModel, metaclass=AllOptional):
    intendCity: Optional[str] = Field(description="意向城市", default="")
    intendPosition: Optional[str] = Field(description="意向岗位", default="")

class Resume_Edu_Info(BaseModel, metaclass=AllOptional):
    schoolName: Optional[str] = Field(description="学校名称", default="")
    major: Optional[str] = Field(description="专业", default="")

class Job_Info(BaseModel, metaclass=AllOptional):
    companyName: Optional[str] = Field(description="公司名称", default="")
    dept: Optional[str] = Field(description="部门", default="")
    title: Optional[str] = Field(description="职位", default="")
    jobStartTime: Optional[date] = Field(description="开始时间", default=date.today())
    jobEndTime: Optional[date] = Field(description="结束时间", default=date.today())
    jobDesc: Optional[str] = Field(description="工作描述", default="")
    intendPosition: Optional[str] = Field(description="意向岗位", default="")

class Project_Info(BaseModel, metaclass=AllOptional):
    companyName: Optional[str] = Field(description="公司名称", default="")
    projName: Optional[str] = Field(description="项目名称", default="")
    positionRole: Optional[str] = Field(description="项目角色", default="")
    projDesc: Optional[str] = Field(description="项目经历描述", default="")
    projStartTime: Optional[date] = Field(description="开始时间", default=date.today())
    projEndTime: Optional[date] = Field(description="结束时间", default=date.today())
