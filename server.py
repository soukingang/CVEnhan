#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   server.py
@Time    :   2024/06/04 14:35:59
@Author  :   Song榆钱儿
@description   :   主启动文件
'''

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
from services.job.invoker import job
from services.project.invoker import project
from services.summary.invoker import summary

app = FastAPI()
@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

app.include_router(job, prefix="/job")
app.include_router(project, prefix="/project")
app.include_router(summary, prefix="/summary")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)

