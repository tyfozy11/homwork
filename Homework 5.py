# завантажити використовуючи requests структуру даних з
#
# https://dummyjson.com/todos
#
# та вивести на екран не виконані значення todo з тих даних, які до вас прийшли
# pip install requests
import requests
from pprint import pprint
url = ' https://dummyjson.com/todos'
todo_non = requests.get(url)

todo_ready = todo_non.json()
#pprint(todo_ready['todos'])
for i in range (len (todo_ready['todos'])):
    if todo_ready['todos'][i]['completed'] == False:
       pprint(todo_ready['todos'][i]['todo'])