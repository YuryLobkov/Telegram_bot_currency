import requests
from bs4 import BeautifulSoup
import pprint
import time

res = requests.get('https://dolarhoy.com/')
soup = BeautifulSoup(res.text, 'html.parser')
print('dolarhoy.com', res)
vals = soup.select('.val')
titles = soup.select('.title')


def scrap_dolar_hoy(title, val):
    dh = []
    for idx in range(1, 6):
        compra = val[idx * 2].getText()
        venta = val[idx * 2 + 1].getText()
        name = title[idx].getText()
        dh.append({name: {'compra': compra, 'venta': venta}})
        time.sleep(0.1)
    return dh


#pprint.pprint(scrap_dolar_hoy(titles, vals))


def get_course_dollar_hoy():
    return scrap_dolar_hoy(titles, vals)


def get_blue_dollar():
    table = scrap_dolar_hoy(titles, vals)
    course_string = table[0].get('Dólar blue')
    blue = '\n'.join(f'{key}: {value}' for key, value in course_string.items())
    return 'Dólar blue\n' + blue


def get_blue_dollar_value():
    return float(scrap_dolar_hoy(titles, vals)[0]['Dólar blue']['compra'][1:])


# print(get_blue_dollar_value())
