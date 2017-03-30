from pprint import pprint as pp
import json

with open('dump.json', 'r') as f:
    my_data = json.load(f)

pp(my_data)
