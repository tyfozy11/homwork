import requests
import pprint

url_nbu = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
result = requests.request('GET', url_nbu)

# with open('example.html', 'wt') as file:
#     file.write(result.text)
pprint.pprint(result.text)
print(type(result.text))