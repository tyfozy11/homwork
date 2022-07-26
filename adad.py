def information_input(age1):
    age1=input('Вводити тут---->')
    while True:
        if age1.isdigit() and int(age1)<=max_age:
            str_age1 = age1
            num_age = int(age1)
            break
        print(error_input)
        return
res_1=information_input()