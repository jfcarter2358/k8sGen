import os
import json
import utils
import shutil

# load the templates

with open('build/data/templates/APIResources.template.py') as f:
    apiresource_template = f.read()
with open('build/data/templates/apiresource_doc.template.rst') as f:
    apiresource_doc_template = f.read()
with open('build/data/templates/apiresource_doc.template.main.rst') as f:
    apiresource_doc_main_template = f.read()
with open('build/data/templates/Components.template.py') as f:
    component_template = f.read()
with open('build/data/templates/component_doc.template.rst') as f:
    component_doc_template = f.read()
with open('build/data/templates/component_doc.template.main.rst') as f:
    component_doc_main_template = f.read()

k8sgen_data = {
    'api_resources_data': {},
    'api_resources': [],
    'components_data': {},
    'components': []
}

# build APIResources.py

out = 'from k8sgen import base\nfrom k8sgen.base import K8sObject\n\n'
fs = os.listdir('k8sgen/data/APIResources')

names = [f[:-5] for f in fs]
rst = [n + '.rst' for n in names]
with open('k8sgen/data/apiresources.txt', 'w') as f:
    f.write('\n'.join(names))
k8sgen_data['api_resources'] = names

for fi in fs:
    out += apiresource_template.replace('(( APIRESOURCE ))', fi[:-5]) + '\n\n'
    with open('k8sgen/data/APIResources/' + fi) as f:
        data = json.load(f)
    k8sgen_data['api_resources_data'][fi[:-5]] = data
    key_strings = utils.get_key_dict(data['json'])
    rows = {k:v for (k, v) in key_strings.items() if type(v) == str}
    row_keys = [k for (k, v) in rows.items()]
    row_vals = [v for (k, v) in rows.items()]

    max_key = len(max(row_keys, key=len))
    max_val = len(max(row_vals, key=len))

    row_string  = '+-' + ('-' * max_key) + '-+-' + ('-' * max_val) + '-+\n'
    row_string += '| ' + 'Key' + (' ' * (max_key - 3)) + ' | ' + 'Type' + (' ' * (max_val - 4)) + ' |\n'
    row_string += '+=' + ('=' * max_key) + '=+=' + ('=' * max_val) + '=+\n'
    for (k, v) in rows.items():
        row_string += '| ' + k + (' ' * (max_key - len(k))) + ' | ' + v + (' ' * (max_val - len(v))) + ' |\n'
        row_string += '+-' + ('-' * max_key) + '-+-' + ('-' * max_val) + '-+\n'
    
    data_strings = json.dumps(data['json'], indent=4).split('\n')
    data_strings = ['    ' + d for d in data_strings]
    data_string = '\n'.join(data_strings)

    with open('docs/source/{}.rst'.format(fi[:-5]), 'w') as f:
        f.write(apiresource_doc_template.replace('(( APIRESOURCE ))', fi[:-5]).replace('(( ROWS ))', row_string).replace('(( JSON ))', data_string))
    with open('docs/source/APIResources.rst', 'w') as f:
        f.write(apiresource_doc_main_template.replace('(( APIRESOURCE_LIST ))', '\n   '.join(sorted(rst))))

with open('k8sgen/APIResources.py', 'w') as f:
    f.write(out)

# build Components.py

out = 'from k8sgen import base\nfrom k8sgen.base import K8sObject\n\n'
fs = os.listdir('k8sgen/data/Components')

names = [f[:-5] for f in fs]
rst = [n + '.rst' for n in names]
with open('k8sgen/data/components.txt', 'w') as f:
    f.write('\n'.join(names))
k8sgen_data['components'] = names

for fi in fs:
    out += component_template.replace('(( COMPONENT ))', fi[:-5]) + '\n\n'
    with open('k8sgen/data/Components/' + fi) as f:
        data = json.load(f)
    k8sgen_data['components_data'][fi[:-5]] = data
    if data != None:
        key_strings = utils.get_key_dict(data)
        rows = {k:v for (k, v) in key_strings.items() if type(v) == str}
        row_keys = [k for (k, v) in rows.items()]
        row_vals = [v for (k, v) in rows.items()]

        max_key = len(max(row_keys, key=len))
        max_val = len(max(row_vals, key=len))

        row_string  = '+-' + ('-' * max_key) + '-+-' + ('-' * max_val) + '-+\n'
        row_string += '| ' + 'Key' + (' ' * (max_key - 3)) + ' | ' + 'Type' + (' ' * (max_val - 4)) + ' |\n'
        row_string += '+=' + ('=' * max_key) + '=+=' + ('=' * max_val) + '=+\n'
        for (k, v) in rows.items():
            row_string += '| ' + k + (' ' * (max_key - len(k))) + ' | ' + v + (' ' * (max_val - len(v))) + ' |\n'
            row_string += '+-' + ('-' * max_key) + '-+-' + ('-' * max_val) + '-+\n'
        
        data_strings = json.dumps(data, indent=4).split('\n')
        data_strings = ['    ' + d for d in data_strings]
        data_string = '\n'.join(data_strings)

        with open('docs/source/{}.rst'.format(fi[:-5]), 'w') as f:
            f.write(component_doc_template.replace('(( COMPONENT ))', fi[:-5]).replace('(( ROWS ))', row_string).replace('(( JSON ))', data_string))
        with open('docs/source/Components.rst', 'w') as f:
            f.write(component_doc_main_template.replace('(( COMPONENT_LIST ))', '\n   '.join(sorted(rst))))

with open('k8sgen/Components.py', 'w') as f:
    f.write(out)

with open('k8sgen/data_file.py', 'w') as f:
    f.write('k8sgen_data = {}'.format(json.dumps(k8sgen_data, indent=4).replace(': null', ': None')))

static_files = os.listdir('build/data/static')
for sf in static_files:
    shutil.copy('build/data/static/{}'.format(sf), 'k8sgen/{}'.format(sf))