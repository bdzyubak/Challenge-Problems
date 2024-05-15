import json

from collections import OrderedDict
from operator import itemgetter


def sort_by_price_ascending(json_string):
    items_dict = json.loads(json_string)
    items_sorted_price = sorted(items_dict, key=lambda x: (x['price'], x['name']))
    json_out = json.dumps(items_sorted_price)
    return json_out

print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))
