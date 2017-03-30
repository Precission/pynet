from pprint import pprint as pp
import yaml

with open('data.yml', 'r') as f:
    my_data = yaml.load(f)

pp(my_data)
