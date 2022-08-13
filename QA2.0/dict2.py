import pandas as pd
import json
from fastapi import FastAPI

app = FastAPI()

i = 1
while i < 10:
    print(i)
    i = i + 1

@app.get('/')
async def test():
    return
