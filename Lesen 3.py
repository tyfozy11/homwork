# lesson 3
my_str = 'abc abc abv sdc'

result = my_str.split("ab")
print(my_str)
print(result)
print(type(result))
my_list = [1, 2, "df", True, [23, 44, 52]]
print(my_list)
my_list.append(my_str)
print(my_list)
my_list.remove(2)
print(my_list)
print("df" in my_list)
my_list[2]="2323"
print(my_list)

# loop
a = 0
b = 10
while a < b:
    print(f'a is {a} b is {b}')
    a+=1 # a = a + 1
a = 0
b = 10

#while True:
 #   print(f'a is {a} b is {b}')
 #   a+=1 # a = a + 1
 #   if a % 2 == 0:
 #       continue
 #   if a >= b:
 #       break

#lst = [1, 22, 2, 'T', 44, 52]
#idx = 0
#while idx < len(lst):
 #   print(lst[idx])

 #   idx += 1

#while True:
#    user_input = input("Enter the number")
 #   if user_input.isdigit():
#       print("Done")
#    else:
#        print('It\' s not number')

#lst = [1, 22, 2, 'T', 44, 52]
#for i in lst:
 #   print('--->', i)

#lst2 =[ [2, 3, 4,[5,6, 7,],[8, 9, 10] ]
#for value in lst2:
 #   print('-->', value)

  #  for sub_val in value:
  #      print('--->', sub_val)

#counter = 5
#lst = []
#while counter> 0:
  #  user_input = input('Enter smth:')
    #lst.append( user_input)
#counter -= 1
#print(lst)

import time

while True:
    print('Hello')
    time.sleep(12)
