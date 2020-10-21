class (( APIRESOURCE )):
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
        data = copy.deepcopy(data_file.k8sgen_data['api_resources_data']['(( APIRESOURCE ))'])
        return data['json']
            
    # write out the API resource class to a json object
    def to_json(self):
        data = copy.deepcopy(data_file.k8sgen_data['api_resources_data']['(( APIRESOURCE ))'])
        components_list = copy.deepcopy(data_file.k8sgen_data['components'])
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