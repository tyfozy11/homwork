import requests
import datetime

url_nbu = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
result = requests.request('GET', url_nbu)


with open('example.txt', 'a', encoding='utf-8') as file:
    file.write(str(datetime.datetime.now()) + '\n\n')
    position = 1
    for currency in result.json():
        file.write(f'{position}. {currency["txt"]} - {currency["rate"]}' + '\n')
        position += 1


try:
    result = requests.request('GET', url)
except Exception as e:
    print(e)
else:
    if 300 > result.status_code >= 200:
        if content := result.headers.get('Content-Type'):
            if content == 'image/png':
                with open('logo.png', 'wb') as file:
                    file.write(result.content)