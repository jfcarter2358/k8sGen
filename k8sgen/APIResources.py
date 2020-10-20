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
class DaemonSet:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/DaemonSet.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['DaemonSet']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/DaemonSet.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['DaemonSet']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class ReplicationController:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ReplicationController.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['ReplicationController']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ReplicationController.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['ReplicationController']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class TokenReview:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/TokenReview.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['TokenReview']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/TokenReview.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['TokenReview']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class StorageClass:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/StorageClass.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['StorageClass']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/StorageClass.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['StorageClass']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class CustomResourceDefinition:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/CustomResourceDefinition.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['CustomResourceDefinition']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/CustomResourceDefinition.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['CustomResourceDefinition']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class CSIDriver:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/CSIDriver.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['CSIDriver']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/CSIDriver.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['CSIDriver']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class Binding:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Binding.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['Binding']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Binding.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['Binding']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class SelfSubjectRulesReview:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/SelfSubjectRulesReview.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['SelfSubjectRulesReview']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/SelfSubjectRulesReview.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['SelfSubjectRulesReview']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class Role:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Role.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['Role']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Role.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['Role']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class Deployment:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Deployment.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['Deployment']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Deployment.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['Deployment']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class ValidatingWebhookConfiguration:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ValidatingWebhookConfiguration.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['ValidatingWebhookConfiguration']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ValidatingWebhookConfiguration.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['ValidatingWebhookConfiguration']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class PodSecurityPolicy:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/PodSecurityPolicy.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['PodSecurityPolicy']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/PodSecurityPolicy.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['PodSecurityPolicy']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class CronJob:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/CronJob.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['CronJob']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/CronJob.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['CronJob']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class RuntimeClass:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/RuntimeClass.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['RuntimeClass']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/RuntimeClass.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['RuntimeClass']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class ClusterRole:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ClusterRole.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['ClusterRole']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ClusterRole.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['ClusterRole']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class Service:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Service.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['Service']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Service.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['Service']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class IngressClass:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/IngressClass.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['IngressClass']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/IngressClass.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['IngressClass']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class Ingress:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Ingress.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['Ingress']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Ingress.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['Ingress']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class PriorityClass:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/PriorityClass.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['PriorityClass']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/PriorityClass.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['PriorityClass']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class PersistentVolume:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/PersistentVolume.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['PersistentVolume']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/PersistentVolume.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['PersistentVolume']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class Event:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Event.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['Event']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Event.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['Event']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class CSINode:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/CSINode.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['CSINode']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/CSINode.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['CSINode']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class ReplicaSet:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ReplicaSet.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['ReplicaSet']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ReplicaSet.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['ReplicaSet']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class MutatingWebhookConfiguration:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/MutatingWebhookConfiguration.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['MutatingWebhookConfiguration']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/MutatingWebhookConfiguration.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['MutatingWebhookConfiguration']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class ServiceAccount:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ServiceAccount.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['ServiceAccount']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ServiceAccount.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['ServiceAccount']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class CertificateSigningRequest:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/CertificateSigningRequest.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['CertificateSigningRequest']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/CertificateSigningRequest.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['CertificateSigningRequest']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class SubjectAccessReview:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/SubjectAccessReview.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['SubjectAccessReview']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/SubjectAccessReview.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['SubjectAccessReview']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class APIService:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/APIService.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['APIService']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/APIService.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['APIService']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class ConfigMap:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ConfigMap.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['ConfigMap']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ConfigMap.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['ConfigMap']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class SelfSubjectAccessReview:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/SelfSubjectAccessReview.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['SelfSubjectAccessReview']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/SelfSubjectAccessReview.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['SelfSubjectAccessReview']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class Lease:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Lease.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['Lease']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Lease.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['Lease']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class Job:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Job.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['Job']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Job.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['Job']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class PodDisruptionBudget:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/PodDisruptionBudget.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['PodDisruptionBudget']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/PodDisruptionBudget.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['PodDisruptionBudget']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class Namespace:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Namespace.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['Namespace']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Namespace.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['Namespace']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class HorizontalPodAutoscaler:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/HorizontalPodAutoscaler.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['HorizontalPodAutoscaler']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/HorizontalPodAutoscaler.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['HorizontalPodAutoscaler']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class Pod:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Pod.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['Pod']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Pod.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['Pod']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class PodTemplate:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/PodTemplate.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['PodTemplate']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/PodTemplate.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['PodTemplate']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class Secret:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Secret.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['Secret']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Secret.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['Secret']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class LimitRange:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/LimitRange.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['LimitRange']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/LimitRange.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['LimitRange']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class NetworkPolicy:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/NetworkPolicy.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['NetworkPolicy']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/NetworkPolicy.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['NetworkPolicy']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class ResourceQuota:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ResourceQuota.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['ResourceQuota']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ResourceQuota.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['ResourceQuota']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class VolumeAttachment:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/VolumeAttachment.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['VolumeAttachment']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/VolumeAttachment.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['VolumeAttachment']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class PersistentVolumeClaim:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/PersistentVolumeClaim.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['PersistentVolumeClaim']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/PersistentVolumeClaim.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['PersistentVolumeClaim']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class Node:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Node.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['Node']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Node.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['Node']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class ComponentStatus:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ComponentStatus.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['ComponentStatus']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ComponentStatus.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['ComponentStatus']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class StatefulSet:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/StatefulSet.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['StatefulSet']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/StatefulSet.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['StatefulSet']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class RoleBinding:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/RoleBinding.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['RoleBinding']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/RoleBinding.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['RoleBinding']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class ClusterRoleBinding:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ClusterRoleBinding.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['ClusterRoleBinding']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ClusterRoleBinding.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['ClusterRoleBinding']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class Endpoints:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Endpoints.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['Endpoints']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/Endpoints.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['Endpoints']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class LocalSubjectAccessReview:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/LocalSubjectAccessReview.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['LocalSubjectAccessReview']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/LocalSubjectAccessReview.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['LocalSubjectAccessReview']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class EndpointSlice:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/EndpointSlice.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['EndpointSlice']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/EndpointSlice.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['EndpointSlice']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

class ControllerRevision:
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
                return ('Invalid key', key)
        return ret

    # get the fields that the API resource utilizes and return them
    def fields(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ControllerRevision.json')
        # data = json.loads(f.decode("utf-8"))
        data = data_file.k8sgen_data['api_resources_data']['ControllerRevision']
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        # f = pkgutil.get_data(__name__, 'data/APIResources/ControllerRevision.json')
        # data = json.loads(f.decode("utf-8"))
        # f = pkgutil.get_data(__name__, 'data/components.txt')
        # components_list = f.decode("utf-8").split('\n')
        data = data_file.k8sgen_data['api_resources_data']['ControllerRevision']
        components_list = data_file.k8sgen_data['components']
        data = utils.recurse_build(data['json'], [], self.elements)
        expanded = utils.recurse_expand(data, components_list)
        filtered = utils.clean_null(expanded)
        return filtered

    # write out the API resource class to a yaml object
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

