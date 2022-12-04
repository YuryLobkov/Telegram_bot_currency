import requests
from bs4 import BeautifulSoup


def get_kzt_rate_str():
    res = requests.get('https://www.mig.kz/')
    soup = BeautifulSoup(res.text, 'html.parser')
    print('https://www.mig.kz/', res)
    raw_string_value = soup.select('.informer > *')[2].getText().strip()
    kzt_rate_value = raw_string_value[:raw_string_value.index('\n')]
    return kzt_rate_value


def get_kzt_value():
    return float(get_kzt_rate_str())


print(get_kzt_rate_str())
print(get_kzt_value())