# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:49:56 2024

@author: mcing
launching outr firt application
"""

#import  fastapi
from fastapi import FastAPI # importing only the stuff that we neeed
app =FastAPI()
@app.get("/")
def home():
    return "hello world"


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
