# завантажити використовуючи requests структуру даних з
#
# https://dummyjson.com/todos
#
# та вивести на екран не виконані значення todo з тих даних, які до вас прийшли
# pip install requests
import requests
from pprint import pprint
url = ' https://dummyjson.com/todos'
todo_examination= requests.get(url)

todo_not_done = todo_examination.json()
#pprint(todo_ready['todos'])
for i in range(len(todo_not_done['todos'])):
    if not todo_not_done['todos'][i]['completed']:
       pprint(todo_not_done['todos'][i]['todo'])