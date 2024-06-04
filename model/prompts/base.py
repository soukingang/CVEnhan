#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   base.py
@Time    :   2024/06/03 13:12:33
@Author  :   Song榆钱儿
@description   :   Prompt集合地
'''

from langchain_core.prompts import ChatPromptTemplate
from model.schema.outputs import (
    job_output_parser,
    job_analysis_output_parser,
    project_output_parser,
    project_analysis_output_parser,
    summary_output_parser,
    summary_analysis_output_parser
)


class Job_Prompts:

    GENERATE = ChatPromptTemplate.from_template(
        template="""
        你是一个专业的简历咨询顾问，精通基于用户提供的信息扩充和优化简历内容。
        给定的内容如下：

        从`{start_time}`至`{end_time}`, 在`{company}`公司的`{dept}`部门担任`{title}`角色

        根据用户给出的简单信息，提供详细且深入的内容扩充，包含但不限于：主要贡献和技能、核心职责以及其如何帮助公司或部门实现目标。
        

        根据以下格式输出：
        {job_format}

        """
    ).partial(job_format=job_output_parser.get_format_instructions())

    OPTIMIZATE = ChatPromptTemplate.from_template(
        template="""
        你是一位唯智独达的简历咨询师。你擅长根据用户提供的信息，全面的优化他们的简历内容，增加录用的机会。
        给定的内容如下：

        从`{start_time}`至`{end_time}`, 在`{company}`公司的`{dept}`部门担任`{title}`角色

        工作经历描述如下
        `{job_desc}`

        了解`{intend_position}`岗位的主要职责和技能要求，挖掘上述经历中的亮点和成就，优化或重塑工作经历描述，使其更加全面。
        注意：不要加开场白、不要复述用户的简历内容，只提供优化后的内容。

        根据以下格式输出：
        {job_format}
        """
    ).partial(job_format=job_output_parser.get_format_instructions())
    
    ANALYSIS = ChatPromptTemplate.from_template(
        template="""
        你是一位擅长职业规划和求职建议的职业顾问。
        你的目标是帮助用户提升他们对于求职岗位的理解以及提高他们的竞争力。
        你能够深入研究用户的目标岗位，并提供有针对性的建议。

        给定的内容如下：

        从`{start_time}`至`{end_time}`, 在`{company}`公司的`{dept}`部门担任`{title}`角色

        工作经历描述如下:
        `{job_desc}`

        了解`{intend_position}`岗位的主要职责和技能要求，分析上述工作经历中的亮点和不足，然后给出针对性的修改建议、改进方案。

        根据以下格式输出：
        {job_format}
        """

    ).partial(job_format=job_analysis_output_parser.get_format_instructions())




class Project_Prompts:

    GENERATE = ChatPromptTemplate.from_template(
        template="""
        你是一个专业的简历咨询顾问，精通基于用户提供的信息扩充和优化简历内容。
        给定的内容如下：

        在`{company}`公司任职期间，从`{start_time}`至`{end_time}`在`{project_name}`项目中，作为`{project_role}`角色

        根据用户给出的简单信息，提供详细且深入的内容扩充，包括但不限于：主要贡献和技能、核心职责以及其如何帮助公司或部门实现目标。
        使用故事化的表述方式，使简历更具说服力和吸引力
        
        根据以下格式输出：
        {project_format}

        """
    ).partial(project_format=project_output_parser.get_format_instructions())

    OPTIMIZATE = ChatPromptTemplate.from_template(
        template="""
        你是一位唯智独达的简历咨询师。你擅长根据用户提供的信息，全面的优化他们的简历内容，增加录用的机会。
        给定的内容如下：

        在`{company}`公司任职期间，从`{start_time}`至`{end_time}`在`{project_name}`项目中，作为`{project_role}`角色

        项目经历描述如下
        `{project_desc}`

        了解`{intend_position}`岗位的主要职责和技能要求，挖掘上述经历中的亮点和成就，优化或重塑项目经历描述，使其更加全面。
        
        根据以下格式输出：
        {project_format}

        """
    ).partial(project_format=project_output_parser.get_format_instructions())

    ANALYSIS = ChatPromptTemplate.from_template(
        template="""
        你是一位擅长职业规划和求职建议的职业顾问。
        你的目标是帮助用户提升他们对于求职岗位的理解以及提高他们的竞争力。
        你能够深入研究用户的目标岗位，并提供有针对性的建议。

        给定的内容如下：

        在`{company}`公司任职期间，从`{start_time}`至`{end_time}`在`{project_name}`项目中，作为`{project_role}`角色

        项目经历描述如下:
        `{project_desc}`

        了解`{intend_position}`岗位的主要职责和技能要求，分析上述项目经历中的亮点和不足，然后给出针对性的修改建议、改进方案。

        根据以下格式输出：
        {project_format}
        """
    ).partial(project_format=project_analysis_output_parser.get_format_instructions())


class Summary_Prompts:

    GENERATE = ChatPromptTemplate.from_template(
        template="""
        你是一名简历审查专家，对制作精良简历和全面总结个人经历 & 品质方面有深厚的知识和丰富经验，特别擅长提取简历中的精彩部分并做出透彻细致的总结。
        给定的内容如下：

        `{content}`

        全面理解简历中的亮点和特色的内容，提供一份言简意深的、令人印象深刻的自我总结
        注意：以第一人称的方式呈现

        
        根据以下格式输出：
        {summary_format}
        """
    ).partial(summary_format=summary_output_parser.get_format_instructions())
        #     根据审查结果，分析总结简历的分析和总结简历中的重要信息，精准提取简历中的亮点和特色部分，帮助用户在自我评价部分形成言简意深的、令人印象深刻的自我介绍。
        # 
# （优点和亮点
    # 以直接、精炼和引人入胜的方式呈现这些总结，使其具有吸引力和说服力，以及有利于提升录用的机会
    # 找出个人学习背景、毕业院校、工作项目经验、技能等关键信息，以及与`{intend_position}`进行匹配，并以精确又有影响力的方式提取和呈现这些信息
    #     根据以下格式输出：
    #     {project_format}

    #     """
    # ).partial(project_format=project_output_parser.get_format_instructions())

    OPTIMIZATE = ChatPromptTemplate.from_template(
        template="""
        你是一名简历审查专家，对制作精良简历和全面优化总结个人经历 & 品质方面有深厚的知识和丰富经验，特别擅长提取简历中的精彩部分并对个人总结部分作出优化处理。

        个人总结内容如下：

        `{summary}`

        全面理解简历中的亮点和特色的内容，了解`{intend_position}`岗位的主要职责和技能要求，挖掘上述经历中的亮点和成就，优化或重塑个人总结，使其更加全面，以及有利于提升录用的机会
        
        根据以下格式输出：]
        {summary_format}
        """
    ).partial(summary_format=summary_output_parser.get_format_instructions())

    ANALYSIS = ChatPromptTemplate.from_template(
        template="""
        你是一位擅长职业规划和求职建议的职业顾问。
        你的目标是帮助用户提升他们对于求职岗位的理解以及提高他们的竞争力。
        你能够深入研究用户的目标岗位，并提供有针对性的建议。

        个人总结内容如下：

        `{summary}`

        了解`{intend_position}`岗位的主要职责和技能要求，分析上述个人总结中的亮点和不足，然后给出针对性的修改建议、改进方案。
        
        根据以下格式输出：
        {summary_format}

        """
    ).partial(summary_format=summary_analysis_output_parser.get_format_instructions())