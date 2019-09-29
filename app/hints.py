from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
import uvicorn, aiohttp, asyncio
from io import BytesIO



import fastai.basics as fai
import fastai.text as ftxt
import os 
from pathlib import Path



import fastai.basics as fai
import fastai.text as ftxt


export_file_url = 'https://drive.google.com/uc?export=download&id=1SuzaqnqxMTNGiXFdHoJGAO-rf8ZXlP07'
export_file_name = 'export_lm.pkl'

path = Path(__file__).parent 


async def download_file(url, dest):
    if dest.exists(): return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(dest, 'wb') as f:
                f.write(data)

download_file(export_file_url, path / export_file_name)


learn = ftxt.load_learner(path, file = export_file_name)



def generatequote():    
    quotes = []
    while quotes==[]:
        idea = learn.predict("xxbos", n_words=20, temperature=0.75)
        ideas = idea.split("xxbos")
        if ideas[1][-1] == "”":
            quotes.append(ideas[1])
            
    message = quotes[0][:]
    message = '“'+message[3:].capitalize()
    message = message.replace(' . ','.')
    message = message.replace(' ,',',')
    message = message.replace("do n't", "don't")
    message = message.replace("ca n't", "can't")
    message = message.replace("we 're", "we're")
    message = message.replace(" ’s", "’s")
    message = message.replace(" 've", "'ve")
    
    return message

