import json

my_list = range(5)

my_list.append('yolo')
my_list.append({})

my_list[-1]['key_1'] = 'item 1'
my_list[-1]['key_2'] = 'item 2'

with open('dump.json', 'w') as f:
    json.dump(my_list, f)
