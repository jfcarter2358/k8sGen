import json
import yaml
from k8sgen import utils
from k8sgen import data_file
import pkgutil

def str_presenter(dumper, data):
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

def represent_none(self, _):
    return self.represent_scalar('tag:yaml.org,2002:null', '')

yaml.add_representer(str, str_presenter)
yaml.add_representer(type(None), represent_none)
'''
Kubernetes VolumeMount component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class VolumeMount:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/VolumeMount.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['VolumeMount']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/VolumeMount.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['VolumeMount']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes ManagedField component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ManagedField:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ManagedField.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['ManagedField']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ManagedField.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['ManagedField']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes HostAlias component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class HostAlias:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/HostAlias.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['HostAlias']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/HostAlias.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['HostAlias']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes NetworkPolicyIngress component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class NetworkPolicyIngress:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/NetworkPolicyIngress.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['NetworkPolicyIngress']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/NetworkPolicyIngress.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['NetworkPolicyIngress']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes VolumeClaimTemplate component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class VolumeClaimTemplate:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/VolumeClaimTemplate.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['VolumeClaimTemplate']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/VolumeClaimTemplate.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['VolumeClaimTemplate']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes DownwardAPIItem component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class DownwardAPIItem:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/DownwardAPIItem.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['DownwardAPIItem']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/DownwardAPIItem.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['DownwardAPIItem']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes NodePreferredAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class NodePreferredAffinity:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/NodePreferredAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['NodePreferredAffinity']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/NodePreferredAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['NodePreferredAffinity']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes Volume component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Volume:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Volume.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['Volume']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Volume.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['Volume']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes IngressTLS component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class IngressTLS:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/IngressTLS.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['IngressTLS']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/IngressTLS.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['IngressTLS']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes IngressRulePath component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class IngressRulePath:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/IngressRulePath.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['IngressRulePath']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/IngressRulePath.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['IngressRulePath']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes AllowedFlexVolume component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class AllowedFlexVolume:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/AllowedFlexVolume.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['AllowedFlexVolume']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/AllowedFlexVolume.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['AllowedFlexVolume']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes ComponentStatusCondition component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ComponentStatusCondition:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ComponentStatusCondition.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['ComponentStatusCondition']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ComponentStatusCondition.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['ComponentStatusCondition']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes NonResourceAttribute component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class NonResourceAttribute:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/NonResourceAttribute.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['NonResourceAttribute']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/NonResourceAttribute.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['NonResourceAttribute']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes EnvironmentVariable component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class EnvironmentVariable:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/EnvironmentVariable.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['EnvironmentVariable']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/EnvironmentVariable.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['EnvironmentVariable']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes Webhook component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Webhook:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Webhook.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['Webhook']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Webhook.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['Webhook']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes ProjectedVolumeSource component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ProjectedVolumeSource:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ProjectedVolumeSource.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['ProjectedVolumeSource']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ProjectedVolumeSource.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['ProjectedVolumeSource']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes AllowedHostPath component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class AllowedHostPath:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/AllowedHostPath.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['AllowedHostPath']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/AllowedHostPath.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['AllowedHostPath']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes ImagePullSecret component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ImagePullSecret:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ImagePullSecret.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['ImagePullSecret']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ImagePullSecret.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['ImagePullSecret']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes SubsetPort component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class SubsetPort:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/SubsetPort.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['SubsetPort']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/SubsetPort.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['SubsetPort']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes RoleRule component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class RoleRule:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/RoleRule.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['RoleRule']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/RoleRule.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['RoleRule']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes ServicePort component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ServicePort:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ServicePort.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['ServicePort']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ServicePort.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['ServicePort']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes Selector component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Selector:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Selector.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['Selector']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Selector.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['Selector']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes Range component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Range:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Range.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['Range']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Range.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['Range']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes AllowedCSIDriver component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class AllowedCSIDriver:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/AllowedCSIDriver.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['AllowedCSIDriver']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/AllowedCSIDriver.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['AllowedCSIDriver']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes PrinterColumn component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class PrinterColumn:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/PrinterColumn.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['PrinterColumn']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/PrinterColumn.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['PrinterColumn']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes ContainerPort component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ContainerPort:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ContainerPort.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['ContainerPort']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ContainerPort.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['ContainerPort']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes ConfigMapItem component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ConfigMapItem:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ConfigMapItem.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['ConfigMapItem']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ConfigMapItem.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['ConfigMapItem']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes NodeSelectorTerm component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class NodeSelectorTerm:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/NodeSelectorTerm.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['NodeSelectorTerm']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/NodeSelectorTerm.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['NodeSelectorTerm']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes DNSConfigOptions component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class DNSConfigOptions:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/DNSConfigOptions.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['DNSConfigOptions']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/DNSConfigOptions.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['DNSConfigOptions']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes Metadata component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Metadata:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Metadata.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['Metadata']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Metadata.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['Metadata']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes ClusterRule component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ClusterRule:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ClusterRule.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['ClusterRule']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ClusterRule.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['ClusterRule']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes PodPreferredAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class PodPreferredAffinity:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/PodPreferredAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['PodPreferredAffinity']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/PodPreferredAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['PodPreferredAffinity']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes ResourceDefinitionVersion component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ResourceDefinitionVersion:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ResourceDefinitionVersion.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['ResourceDefinitionVersion']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ResourceDefinitionVersion.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['ResourceDefinitionVersion']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes AllowedTopology component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class AllowedTopology:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/AllowedTopology.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['AllowedTopology']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/AllowedTopology.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['AllowedTopology']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes SecurityContext component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class SecurityContext:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/SecurityContext.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['SecurityContext']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/SecurityContext.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['SecurityContext']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes LifecycleDefinition component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class LifecycleDefinition:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/LifecycleDefinition.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['LifecycleDefinition']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/LifecycleDefinition.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['LifecycleDefinition']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes OwnerReference component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class OwnerReference:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/OwnerReference.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['OwnerReference']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/OwnerReference.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['OwnerReference']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes SecretItem component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class SecretItem:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/SecretItem.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['SecretItem']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/SecretItem.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['SecretItem']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes PodAntiAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class PodAntiAffinity:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/PodAntiAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['PodAntiAffinity']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/PodAntiAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['PodAntiAffinity']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes Container component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Container:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Container.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['Container']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Container.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['Container']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes Address component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Address:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Address.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['Address']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Address.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['Address']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes IngressRule component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class IngressRule:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/IngressRule.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['IngressRule']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/IngressRule.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['IngressRule']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes ScopeSelector component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ScopeSelector:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ScopeSelector.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['ScopeSelector']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ScopeSelector.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['ScopeSelector']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes UserGroup component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class UserGroup:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/UserGroup.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['UserGroup']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/UserGroup.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['UserGroup']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes PodRequiredAntiAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class PodRequiredAntiAffinity:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/PodRequiredAntiAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['PodRequiredAntiAffinity']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/PodRequiredAntiAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['PodRequiredAntiAffinity']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes EnvironmentVariableSource component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class EnvironmentVariableSource:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/EnvironmentVariableSource.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['EnvironmentVariableSource']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/EnvironmentVariableSource.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['EnvironmentVariableSource']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes Limit component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Limit:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Limit.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['Limit']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Limit.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['Limit']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes NodeAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class NodeAffinity:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/NodeAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['NodeAffinity']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/NodeAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['NodeAffinity']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes NetworkPolicyEgress component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class NetworkPolicyEgress:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/NetworkPolicyEgress.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['NetworkPolicyEgress']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/NetworkPolicyEgress.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['NetworkPolicyEgress']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes Subset component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Subset:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Subset.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['Subset']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Subset.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['Subset']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes DNSConfig component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class DNSConfig:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/DNSConfig.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['DNSConfig']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/DNSConfig.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['DNSConfig']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes PodAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class PodAffinity:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/PodAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['PodAffinity']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/PodAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['PodAffinity']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes MatchExpression component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class MatchExpression:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/MatchExpression.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['MatchExpression']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/MatchExpression.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['MatchExpression']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes Probe component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Probe:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Probe.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['Probe']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Probe.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['Probe']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes ServiceAccountSecret component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ServiceAccountSecret:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ServiceAccountSecret.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['ServiceAccountSecret']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ServiceAccountSecret.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['ServiceAccountSecret']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes ReadinessGate component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ReadinessGate:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ReadinessGate.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['ReadinessGate']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ReadinessGate.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['ReadinessGate']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes Toleration component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Toleration:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Toleration.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['Toleration']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Toleration.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['Toleration']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes NodeRequiredAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class NodeRequiredAffinity:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/NodeRequiredAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['NodeRequiredAffinity']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/NodeRequiredAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['NodeRequiredAffinity']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes MatchLabelExpression component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class MatchLabelExpression:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/MatchLabelExpression.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['MatchLabelExpression']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/MatchLabelExpression.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['MatchLabelExpression']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes Sysctl component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Sysctl:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Sysctl.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['Sysctl']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Sysctl.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['Sysctl']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes HTTPHeader component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class HTTPHeader:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/HTTPHeader.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['HTTPHeader']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/HTTPHeader.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['HTTPHeader']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes ResourceAttribute component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ResourceAttribute:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ResourceAttribute.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['ResourceAttribute']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ResourceAttribute.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['ResourceAttribute']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes ClientConfig component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ClientConfig:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ClientConfig.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['ClientConfig']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ClientConfig.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['ClientConfig']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes VolumeDevice component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class VolumeDevice:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/VolumeDevice.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['VolumeDevice']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/VolumeDevice.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['VolumeDevice']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes PodPreferredAntiAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class PodPreferredAntiAffinity:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/PodPreferredAntiAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['PodPreferredAntiAffinity']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/PodPreferredAntiAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['PodPreferredAntiAffinity']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes PodRequiredAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class PodRequiredAffinity:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/PodRequiredAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['PodRequiredAffinity']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/PodRequiredAffinity.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['PodRequiredAffinity']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes Taint component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Taint:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Taint.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['Taint']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/Taint.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['Taint']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes ContainerSpec component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ContainerSpec:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ContainerSpec.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['ContainerSpec']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ContainerSpec.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['ContainerSpec']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes ClusterRoleBindingSubject component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ClusterRoleBindingSubject:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ClusterRoleBindingSubject.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['ClusterRoleBindingSubject']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/ClusterRoleBindingSubject.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['ClusterRoleBindingSubject']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

'''
Kubernetes CSINodeDriver component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class CSINodeDriver:
    def __init__(self, **kwargs):
        self.elements = {}

    # set any specific field to a value
    def set(self, **kwargs):
        ret = []
        key_strings = utils.get_key_string(self.fields())
        for key, value in kwargs.items():
            ky = key.replace('_', '.')
            if ky.startswith('.'):
                ky = ky[1:]
                if ky in key_strings:
                    self.elements[ky] = value
                    ret.append(True)
                else:
                    ret.append((False, 'invalid key name'))
            else:
                matches = []
                for k in key_strings:
                    if k.endswith(ky):
                        matches.append(k)
                if len(matches) == 1:
                    self.elements[matches[0]] = value
                    ret.append(True)
                elif len(matches) == 0:
                    ret.append((False, 'invalid key name'))
                else:
                    ret.append((False, 'ambiguous key name'))
        return ret

    # get the values that have been set for specific fields
    def get(self, *args):
        ret = {}
        for key in args:
            ky = key.replace('_', '.')
            if ky in self.elements.keys():
                ret[key] = self.elements[ky]
            else:
                return ('Invalid key name', key)
        return ret

    # get the fields that the component utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/Components/CSINodeDriver.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['components_data']['CSINodeDriver']
        return data
            
    # write out the component class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/Components/CSINodeDriver.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['components_data']['CSINodeDriver']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data, [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the component class to a yaml object
    def to_yaml(self):
        data = self.to_json()
        return yaml.dump(data)

    def to_string(self):
        variables = utils.clean_null(utils.clean_unset({k.replace('.', '_'):v for (k, v) in self.elements.items()}))
        str_rep = ''
        for v in variables:
            str_rep += '{}={}, '.format(v, variables[v])
        class_name = type(self).__name__
        return '{}({})'.format(class_name, str_rep[:-2])
        
    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

