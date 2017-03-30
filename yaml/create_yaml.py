import yaml

my_list = range(2)

my_list.append({})

my_list[-1]['key_1'] = 'first_item'
my_list[-1]['key_2'] = 'sec_item'

with open('data.yml', 'w') as f:
    f.write(yaml.dump(my_list))
