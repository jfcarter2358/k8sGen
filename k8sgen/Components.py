import json
import yaml
from k8sgen import utils
import pkgutil

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
        f = pkgutil.get_data(__name__, 'data/Components/VolumeMount.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/VolumeMount.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/ManagedField.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/ManagedField.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/HostAlias.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/HostAlias.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/NetworkPolicyIngress.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/NetworkPolicyIngress.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/VolumeClaimTemplate.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/VolumeClaimTemplate.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/DownwardAPIItem.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/DownwardAPIItem.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/NodePreferredAffinity.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/NodePreferredAffinity.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/Volume.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/Volume.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/IngressTLS.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/IngressTLS.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/IngressRulePath.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/IngressRulePath.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/AllowedFlexVolume.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/AllowedFlexVolume.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/ComponentStatusCondition.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/ComponentStatusCondition.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/NonResourceAttribute.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/NonResourceAttribute.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/EnvironmentVariable.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/EnvironmentVariable.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/Webhook.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/Webhook.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/ProjectedVolumeSource.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/ProjectedVolumeSource.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/AllowedHostPath.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/AllowedHostPath.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/ImagePullSecret.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/ImagePullSecret.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/RoleRule.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/RoleRule.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/ServicePort.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/ServicePort.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/Selector.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/Selector.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/Range.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/Range.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/AllowedCSIDriver.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/AllowedCSIDriver.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/PrinterColumn.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/PrinterColumn.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/ConfigMapItem.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/ConfigMapItem.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/NodeSelectorTerm.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/NodeSelectorTerm.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/DNSConfigOptions.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/DNSConfigOptions.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/Metadata.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/Metadata.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/ClusterRule.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/ClusterRule.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/PodPreferredAffinity.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/PodPreferredAffinity.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/ResourceDefinitionVersion.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/ResourceDefinitionVersion.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/AllowedTopology.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/AllowedTopology.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/SecurityContext.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/SecurityContext.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/LifecycleDefinition.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/LifecycleDefinition.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/OwnerReference.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/OwnerReference.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/SecretItem.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/SecretItem.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/PodAntiAffinity.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/PodAntiAffinity.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/Container.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/Container.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/Address.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/Address.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/IngressRule.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/IngressRule.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/ScopeSelector.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/ScopeSelector.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/UserGroup.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/UserGroup.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/PodRequiredAntiAffinity.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/PodRequiredAntiAffinity.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/EnvironmentVariableSource.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/EnvironmentVariableSource.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/Limit.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/Limit.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/NodeAffinity.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/NodeAffinity.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/NetworkPolicyEgress.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/NetworkPolicyEgress.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/Subset.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/Subset.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/DNSConfig.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/DNSConfig.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/PodAffinity.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/PodAffinity.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/MatchExpression.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/MatchExpression.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/Probe.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/Probe.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
Kubernetes Port component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Port:
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
        f = pkgutil.get_data(__name__, 'data/Components/Port.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/Port.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/ServiceAccountSecret.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/ServiceAccountSecret.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/ReadinessGate.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/ReadinessGate.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/Toleration.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/Toleration.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/NodeRequiredAffinity.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/NodeRequiredAffinity.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/MatchLabelExpression.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/MatchLabelExpression.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/Sysctl.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/Sysctl.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/HTTPHeader.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/HTTPHeader.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/ResourceAttribute.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/ResourceAttribute.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/ClientConfig.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/ClientConfig.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/VolumeDevice.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/VolumeDevice.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/PodPreferredAntiAffinity.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/PodPreferredAntiAffinity.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/PodRequiredAffinity.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/PodRequiredAffinity.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/Taint.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/Taint.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/ContainerSpec.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/ContainerSpec.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/ClusterRoleBindingSubject.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/ClusterRoleBindingSubject.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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
        f = pkgutil.get_data(__name__, 'data/Components/CSINodeDriver.json')
        data = json.loads(f.decode("utf-8"))
        return data
            
    # write out the component class to a json object
    def to_json(self):
        f = pkgutil.get_data(__name__, 'data/Components/CSINodeDriver.json')
        data = json.loads(f.decode("utf-8"))
        f = pkgutil.get_data(__name__, 'data/components.txt')
        components_list = f.decode("utf-8").split('\n')
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

