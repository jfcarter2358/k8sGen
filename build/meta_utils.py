def get_from_key_list(data, keys):
    if type(data) != dict and type(data) != list:
        return data
    if type(data) == list:
        data = data[0]
    # if the key doesn't exist then return None
    if not keys[0] in data.keys():
        return None
    if len(keys) > 1:
        # if we aren't at the last key then go a level deeper
        return get_from_key_list(data[keys[0]], keys[1:])
    else:
        # return the value we want
        return data[keys[0]]
        
def clean_null(d):
   clean = {}
   for k, v in d.items():
        if isinstance(v, dict):
            nested = clean_null(v)
            if len(nested.keys()) > 0:
                clean[k] = nested
        elif v is not None:
            clean[k] = v
   return clean

def clean_unset(data):
    if type(data) == dict:
        for k in data:
            if type(data[k]) == dict:
                data[k] = clean_unset(data[k])
            elif type(data[k]) == list:
                data[k] = clean_unset(data[k])
            elif type(data[k]) == str:
                if data[k].startswith('<') and data[k].endswith('>'):
                    data[k] = None
    else:
        for k in range(0, len(data)):
            if type(data[k]) == dict:
                data[k] = clean_unset(data[k])
            elif type(data[k]) == list:
                data[k] = clean_unset(data[k])
            elif type(data[k]) == str:
                if data[k].startswith('<') and data[k].endswith('>'):
                    data[k] = None
    return data

def recurse_expand(data, components_list, indent=0):
    # print(' ' * indent + str(data))
    if type(data) == dict:
        for k in data:
            if type(data[k]).__name__ in components_list:
                data[k] = data[k].to_json()
            else:
                if type(data[k]) == dict:
                    data[k] = recurse_expand(data[k], components_list, indent = indent+2)
                elif type(data[k]) == list:
                    data[k] = recurse_expand(data[k], components_list, indent = indent+2)
                elif type(data[k]) == str:
                    if data[k].startswith('<') and data[k].endswith('>'):
                        data[k] = None
    else:
        for k in range(0, len(data)):
            if type(data[k]).__name__ in components_list:
                data[k] = data[k].to_json()
            else:
                if type(data[k]) == dict:
                    data[k] = recurse_expand(data[k], components_list, indent = indent+2)
                elif type(data[k]) == list:
                    data[k] = recurse_expand(data[k], components_list, indent = indent+2)
                elif type(data[k]) == str:
                    if data[k].startswith('<') and data[k].endswith('>'):
                        data[k] = None
    return data

def recurse_build(data, key_list, elements, indent=0):
    # print(' ' * indent + str(data))
    if type(data) == dict:
        for k in data:
            key = '.'.join(key_list + [k])
            if key in elements.keys():
                data[k] = elements[key]
            else:
                if type(data[k]) == dict:
                    data[k] = recurse_build(data[k], key_list + [k], elements, indent = indent+2)
                elif type(data[k]) == list:
                    data[k] = recurse_build(data[k], key_list + [k], elements, indent = indent+2)
    else:
        for k in range(0, len(data)):
            key = '.'.join(key_list)
            if key in elements.keys():
                data[k] = elements[key]
            else:
                if type(data[k]) == dict:
                    data[k] = recurse_build(data[k], key_list, elements, components_list, apiresources_list, indent = indent+2)
                elif type(data[k]) == list:
                    data[k] = recurse_build(data[k], key_list, elements, components_list, apiresources_list, indent = indent+2)
    return data

def get_key_dict(data):
    temp = list(get_paths(data))
    ret = {'_'.join(a):get_from_key_list(data, a) for i, a in enumerate(temp) if a not in temp[:i]}
    return ret

def get_paths(d, current = []):
    for a, b in d.items():
        yield current+[a]
        if isinstance(b, dict):
            yield from get_paths(b, current+[a])
        elif isinstance(b, list):
            for i in b:
                yield from get_paths(i, current+[a])