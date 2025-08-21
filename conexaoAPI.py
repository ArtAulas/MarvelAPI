from dotenv import load_dotenv
import os
from datetime import datetime
import hashlib
import requests

load_dotenv()

PUBLIC_KEY= os.getenv("PUBLIC_KEY")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
BASE_ENDPOINT='https://gateway.marvel.com'
TIMESTAMP=datetime.now().timestamp()
HASH= hashlib.md5(f"{TIMESTAMP}{PRIVATE_KEY}{PUBLIC_KEY}".encode()).hexdigest()
AUTH_PARAMS=f'?apikey={PUBLIC_KEY}&ts={TIMESTAMP}&hash={HASH}&limit=100'

def get_image(urlImagem,nomeImagem='img'):
    try:
        data = requests.get(urlImagem).content
        f = open(nomeImagem+'.jpg','wb')
        f.write(data)
        f.close()
    except:
        pass

def get_character_by_name(nome):
    url=f'{BASE_ENDPOINT}:443/v1/public/characters{AUTH_PARAMS}&nameStartsWith={nome}'
    r=requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        print('Erro na requisição:', r.status_code)