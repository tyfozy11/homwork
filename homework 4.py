# task 1.
# написати програму, яка просить в користувача ввести через пробіл міста, в яких він був за минулі 10 років
# потім окремо запросити у користувача міста, куди він хоче поїхати внаступні 10 років
# вивести на екран повідомлення з текстом про те, що користувачу, мабуть, дуже сподобалося в містах, які він повторив в
# двох циклах вводу, а саме... (сформувати строку, використовуючи join)
# якщо повтору не було - вивести повідомлення, що користувач відкритий до чогось нового
# врахувати випадки, що користувач нічого не вводить не потрібно, в даному випадку вам явно зазначено,
# що ці перевірки не потрібні.
# не потрібно перевіряти введення цифр
# ми виходим із того, що користувач введе щось на зразок "Київ Тернопіль париЖ акапулько-80"
# В той же час врахуйте, що користувач може вводити дані в різних регістрах

# використати сети!!!

# print( "Вітаю,введіть через пробіл міста, в яких, Ви, був за минулі 10 років, будь ласка.")
# date_input = input("").title().split()
# date_input = set(date_input)
# print(date_input )
# print( "Дякую, а тепер введіть міста, куди, Ви, хотіли б  поїхати внаступні 10 років ")
# date_input2 =  input("").title().split()
# date_input2 = set(date_input2)
# print(date_input2)
# if len( date_input & date_input2) >= 1:
#     print(','.join(date_input & date_input2), 'мабуть, дуже сподобалося в містах')
# else :
#     print(' відкритий до чогось нового')


#дано код Морзе, що зберігається в словнику
# є стрічка, в якій слова розділені 2 пробілами, а букви в слові - одним пробілом
# написати програму по декодуванню даної (чи подібної) стрічки
# ПІДКАЗКА - при потребі можна створити симетричний словник, де ключами буде код Морзе, а значеннями - символи латиниці
# """
# MORSE_CODE_DICT = {
# 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
# 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
# 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
# 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
# '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
# '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
# }
# string_to_decode1 = '.. .-.. .. -.- . .--. -.-- - .... --- -. ...-- .-.-.- .---- ----- '
# string_to_decode2 = '.. -.- -. --- .-- --..-- -.-- --- ..- -.-. .- -. -.. --- .. - '

MORSE_CODE_DICT = {
'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
'6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
'?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}
print(MORSE_CODE_DICT.items())
string_to_decode1 = '.. .-.. .. -.- . .--. -.-- - .... --- -. ...-- .-.-.- .---- ----- '
string_to_decode2 = '.. -.- -. --- .-- --..-- -.-- --- ..- -.-. .- -. -.. --- .. - '
print(string_to_decode1.split())
print('----->', string_to_decode1)