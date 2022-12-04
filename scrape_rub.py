import requests
from bs4 import BeautifulSoup


def get_rub_rate_str():
    res = requests.get('https://www.sravni.ru/bank/sberbank-rossii/valjuty/')
    soup = BeautifulSoup(res.text, 'html.parser')
    print('sravni.ru', res)
    return soup.select('td:nth-child(2) > span:nth-child(1)')[0].getText()


def get_rub_value():
    return (float(get_rub_rate_str()[:5].replace(',','.')))


#print(get_rub_rate_str())
# print(get_rub_value())