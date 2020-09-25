import yaml
import json
import os
import shutil
import subprocess
import sys

def build_resources():
    p = subprocess.Popen('kubectl api-resources', shell=True, stdout=subprocess.PIPE)
    output = p.communicate()[0].decode()

    resources = []
    resource_lines = output.split('\n')
    for rl in resource_lines[1:]:
        r = rl.split(' ')[-1]
        if len(r) > 0:
            resources.append(r)

    resources = list(set(resources))
    resources.sort()

    with open('build/data/resources.txt', 'w') as f:
        f.write('\n'.join(resources))

    for r in resources:
        os.system('kubectl explain {0} --recursive > build/data/resources/{0}.txt'.format(r))

def build_components(components):
    for k in components['build']:
        key_list = components['build'][k].split('.')

        data = parse(key_list[0])

        component_data = get_from_key_list(data['json'], key_list[1:])

        if type(component_data) == list:
            component_data = component_data[0]
        
        with open('k8sgen/data/Components/{}.json'.format(k), 'w') as f:
            json.dump(component_data, f, indent=4)

def format_components(components):
    for c in components['build']:
        print(c)
        with open('k8sgen/data/Components/{}.json'.format(c)) as f:
            data = json.load(f)
        key_list = components['build'][c].split('.')[1:]

        for k in components['ignore']['Components']:
            delete_from_key_list(data, k.split('.'))

        for k in components['replace']:
            r = k[:k.find('.')]
            key = k[k.find('.') + 1:]
            if c == r:
                if get_from_key_list(data, key.split('.')) != None:
                    data = set_from_key_list(data, key.split('.'), components['replace'][k]) 

        with open('k8sgen/data/Components/{}.json'.format(c), 'w') as f:
            json.dump(data, f, indent=4)

def parse(resource):
    with open('build/data/resources/{}.txt'.format(resource)) as f:
        lines = f.read().split('\n')

    fields_index = -1
    kind = ""
    version = ""
    description = ""
    is_description = False

    index = 0
    for l in lines:
        index += 1
        if l.startswith('FIELDS:'):
            is_description = False
            fields_index = index
            break
        if is_description:
            description += ' ' + l.strip()
        if l.startswith('KIND:'):
            kind = l[l.rfind(' ') + 1:]
        if l.startswith('VERSION:'):
            version = l[l.rfind(' ') + 1:]
        if l.startswith('DESCRIPTION:'):
            is_description = True

    fields = '\n'.join(lines[fields_index:])
    fields = fields.replace('\t<', ' <')
    fields = fields.replace(' <', ': <')

    fields = fields.split('\n')

    for i in range(0, len(fields)):
        indent = len(fields[i]) - len(fields[i].replace(' - ', '   ').lstrip())
        parts = fields[i].strip().split(': ')
        if len(parts) > 1:
            if parts[1] == '<[]Object>':
                child_indent = len(fields[i+1]) - len(fields[i+1].replace(' - ', '   ').lstrip())
                if child_indent > indent:
                    fields[i+1] = fields[i+1][:indent+1] + '-' + fields[i+1][indent+2:]

    fields = '\n'.join(fields)
    
    fields = fields.replace('<map[string]Object>', '')
    fields = fields.replace('<Object>', '')
    fields = fields.replace('<[]Object>', '')

    # with open('build/debug.txt', 'w') as f:
    #     f.write(fields)

    fields_data = yaml.safe_load(fields)     

    kind = kind.strip()
    version = version.strip()
    description = description.strip()
    if fields_data == None:
        fields_data = {}

    fields_data['apiVersion'] = version
    fields_data['kind'] = kind

    data = {
        "description": description,
        "json": fields_data
    }

    return data

def format_resource(resource, components):
    data = parse(resource) 

    for k in components['replace']:
        r = k[:k.find('.')]
        key = k[k.find('.') + 1:]
        if resource == r:
            if get_from_key_list(data['json'], key.split('.')) != None:
                data['json'] = set_from_key_list(data['json'], key.split('.'), components['replace'][k])   

    for k in components['ignore'][resource]:
        delete_from_key_list(data['json'], k.split('.'))

    with open('k8sgen/data/APIResources/{}.json'.format(resource), 'w') as f:
        json.dump(data, f, indent=4)

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

def delete_from_key_list(data, keys):
    # if the key doesn't exist then return None
    if not keys[0] in data.keys():
        return False
    if len(keys) > 1:
        # if we aren't at the last key then go a level deeper
        if type(data[keys[0]]) == list:
            return [delete_from_key_list(data[keys[0]][0], keys[1:])]
        else:
            return delete_from_key_list(data[keys[0]], keys[1:])
    else:
        # return the value we want
        del data[keys[0]]
        return True

def set_from_key_list(data, keys, value):
    if type(data) != dict and type(data) != list:
        return data
    # if the key doesn't exist then return None
    if not keys[0] in data.keys():
        if len(keys) == 1:
            data[keys[0]] = value
            return data
        else:
            return None
        return None
    if len(keys) > 1:
        # if we aren't at the last key then go a level deeper
        if type(data[keys[0]]) == list:
            ret = [set_from_key_list(data[keys[0]][0], keys[1:], value)]
        else:
            ret = set_from_key_list(data[keys[0]], keys[1:], value)
        if ret == None:
            return None
        else:
            data[keys[0]] = ret
    else:
        # return the value we want
        data[keys[0]] = value
    return data

with open('build/data/resources.txt') as f:
    resources = f.read().split('\n')

with open('build/data/components.json') as f:
    components = json.load(f)

if os.path.exists('data'):
    shutil.rmtree('data')
os.mkdir('k8sgen/data')
os.mkdir('k8sgen/data/APIResources')
os.mkdir('k8sgen/data/Components')

if sys.argv[1] == 'y':
    if os.path.exists('build/data/resources'):
        shutil.rmtree('build/data/resources')
    os.mkdir('build/data/resources')

    print('getting resources...')
    build_resources()

print('building components...')
build_components(components)

print('fomatting components...')
format_components(components)

print('formatting resources...')
for r in resources:
    format_resource(r, components)

print('done!')