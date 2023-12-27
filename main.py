import requests
from api_responses import _200, _400
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
from os import environ as env
from fastapi import FastAPI
import json

def genrerate_token():
    url = 'https://api.petfinder.com/v2/oauth2/token'
    obj = {
        'grant_type': 'client_credentials',
        'client_id': env['client_id'],
        'client_secret': env['client_secret']
    }
    x = requests.post(url, json = obj)
    t = json.loads(x.text)
    return t["access_token"]

def get_req(page):
    url = "https://api.petfinder.com/v2/animals"
    obj = {'page': page}
    b = "Bearer "
    d = genrerate_token()
    v={'Authorization': b + d}
    if page == 1:
        x = requests.get(url, headers=v)
    else :
        x = requests.get(url, params=obj, headers=v)
    return json.loads(x.text)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"hello":"world"}


@app.get("/animals/{page}")
def read_item(page: int, q: Union[str, None] = None):
    return get_req(page)