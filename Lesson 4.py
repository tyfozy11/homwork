# Lesson 4
first_number = 55
sekond_number = 3

try:
    division = first_number / sekond_number
    print(division)
except:
    division = None
    print(division)
print(division)

new_set = set()
set1 = {2, 25, "fkd", (3), 45,'fefef' 'dedw' }
print(new_set)
print(set1)




list_city = input().split()
print(list_city)

unigue= set(list_city)
print(unigue)

print(len(unigue))


my_dict = {
    'neme': 'Serhii',
    55: [],
}
dict2 = dict()
dict3 = dict(city='odesa')
dict4 = {}

print(my_dict['neme'])
my_string = ' jfwfwufhwiufb urhu2fhwjfneryvn rfb2uf3nfo3u u4h3u'
unigue2 = set(my_string)
my_dict8 = dict.fromkeys(unigue2, 0)
for leters in my_dict8.values():
    print(leters)