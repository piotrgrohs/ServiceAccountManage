import hcl2

def load_tf(file):
    with open(file, 'r') as file:
        return hcl2.load(file)

def get_difference(dict_a, dict_b):
    _list = []
    for app in dict_a["data"]: 
        for attribute in dict_a["data"][app]:
            attribute_a = dict_a["data"][app][attribute]
            attribute_b = dict_b["data"][app][attribute]
            compare = set(attribute_b) - set(attribute_a)
            compare_swap = set(attribute_a) - set(attribute_b)
            if len(compare) > 0 or len(compare_swap) > 0:
                _list.append({ 'app': app,
                        'element_a': dict_a["data"][app],
                        'element_b': dict_b["data"][app],
                        'key': attribute,
                        'value': compare if len(compare) > 0 else compare_swap
                        })
    return _list

dict_before_file = 'data.tfvars'
dict_now_file = 'data2.tfvars'
dict_before = load_tf(dict_before_file)
dict_now = load_tf(dict_now_file)

difference = get_difference(dict_before, dict_now)
pass
