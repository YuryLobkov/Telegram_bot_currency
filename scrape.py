import requests
from bs4 import BeautifulSoup
import pprint
import time


res = requests.get('https://dolarhoy.com/')
soup = BeautifulSoup(res.text, 'html.parser')
print(res)
val = soup.select('.val')
title = soup.select('.title')


def scrap_dolar_hoy(title, val):
    dh = []
    for idx in range(1, 6):
        compra = val[idx*2].getText()
        venta = val[idx*2+1].getText()
        name = title[idx].getText()
        dh.append({name : {'compra' : compra, 'venta': venta} })
        time.sleep(0.1)
    return(dh)

pprint.pprint(scrap_dolar_hoy(title, val))

