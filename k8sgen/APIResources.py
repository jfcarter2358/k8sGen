import json
import yaml
from k8sgen import utils
from k8sgen import data_file
import copy

def str_presenter(dumper, data):
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

def represent_none(self, _):
    return self.represent_scalar('tag:yaml.org,2002:null', '')

yaml.add_representer(str, str_presenter)
yaml.add_representer(type(None), represent_none)
class APIResource:
    def __init__(self, api_name):
        self.api_name = api_name
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
        data = copy.deepcopy(data_file.k8sgen_data['api_resources_data'][self.api_name])
        return data['json']

    # write out the API resource class to a json object
    def to_json(self):
        data = copy.deepcopy(data_file.k8sgen_data['api_resources_data'][self.api_name])
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

class DaemonSet(APIResource):
    def __init__(self):
        super().__init__(api_name="DaemonSet")


class ReplicationController(APIResource):
    def __init__(self):
        super().__init__(api_name="ReplicationController")


class TokenReview(APIResource):
    def __init__(self):
        super().__init__(api_name="TokenReview")


class StorageClass(APIResource):
    def __init__(self):
        super().__init__(api_name="StorageClass")


class CustomResourceDefinition(APIResource):
    def __init__(self):
        super().__init__(api_name="CustomResourceDefinition")


class CSIDriver(APIResource):
    def __init__(self):
        super().__init__(api_name="CSIDriver")

class Binding(APIResource):
    def __init__(self):
        super().__init__(api_name="Binding")


class SelfSubjectRulesReview(APIResource):
    def __init__(self):
        super().__init__(api_name="SelfSubjectRulesReview")


class Role(APIResource):
    def __init__(self):
        super().__init__(api_name="Role")


class Deployment(APIResource):
    def __init__(self):
        super().__init__(api_name="Deployment")


class ValidatingWebhookConfiguration(APIResource):
    def __init__(self):
        super().__init__(api_name="ValidatingWebhookConfiguration")


class PodSecurityPolicy(APIResource):
    def __init__(self):
        super().__init__(api_name="PodSecurityPolicy")

class CronJob(APIResource):
    def __init__(self):
        super().__init__(api_name="CronJob")


class RuntimeClass(APIResource):
    def __init__(self):
        super().__init__(api_name="RuntimeClass")


class ClusterRole(APIResource):
    def __init__(self):
        super().__init__(api_name="ClusterRole")


class Service(APIResource):
    def __init__(self):
        super().__init__(api_name="Service")


class IngressClass(APIResource):
    def __init__(self):
        super().__init__(api_name="IngressClass")


class Ingress(APIResource):
    def __init__(self):
        super().__init__(api_name="Ingress")


class PriorityClass(APIResource):
    def __init__(self):
        super().__init__(api_name="PriorityClass")


class PersistentVolume(APIResource):
    def __init__(self):
        super().__init__(api_name="PersistentVolume")


class Event(APIResource):
    def __init__(self):
        super().__init__(api_name="Event")


class CSINode(APIResource):
    def __init__(self):
        super().__init__(api_name="CSINode")


class ReplicaSet(APIResource):
    def __init__(self):
        super().__init__(api_name="ReplicaSet")


class MutatingWebhookConfiguration(APIResource):
    def __init__(self):
        super().__init__(api_name="MutatingWebhookConfiguration")


class ServiceAccount(APIResource):
    def __init__(self):
        super().__init__(api_name="ServiceAccount")


class CertificateSigningRequest(APIResource):
    def __init__(self):
        super().__init__(api_name="CertificateSigningRequest")


class SubjectAccessReview(APIResource):
    def __init__(self):
        super().__init__(api_name="SubjectAccessReview")


class APIService(APIResource):
    def __init__(self):
        super().__init__(api_name="APIService")


class ConfigMap(APIResource):
    def __init__(self):
        super().__init__(api_name="ConfigMap")


class SelfSubjectAccessReview(APIResource):
    def __init__(self):
        super().__init__(api_name="SelfSubjectAccessReview")


class Lease(APIResource):
    def __init__(self):
        super().__init__(api_name="Lease")


class Job(APIResource):
    def __init__(self):
        super().__init__(api_name="Job")


class PodDisruptionBudget(APIResource):
    def __init__(self):
        super().__init__(api_name="PodDisruptionBudget")


class Namespace(APIResource):
    def __init__(self):
        super().__init__(api_name="Namespace")


class HorizontalPodAutoscaler(APIResource):
    def __init__(self):
        super().__init__(api_name="HorizontalPodAutoscaler")


class Pod(APIResource):
    def __init__(self):
        super().__init__(api_name="Pod")


class PodTemplate(APIResource):
    def __init__(self):
        super().__init__(api_name="PodTemplate")


class Secret(APIResource):
    def __init__(self):
        super().__init__(api_name="Secret")


class LimitRange(APIResource):
    def __init__(self):
        super().__init__(api_name="LimitRange")


class NetworkPolicy(APIResource):
    def __init__(self):
        super().__init__(api_name="NetworkPolicy")


class ResourceQuota(APIResource):
    def __init__(self):
        super().__init__(api_name="ResourceQuota")


class VolumeAttachment(APIResource):
    def __init__(self):
        super().__init__(api_name="VolumeAttachment")


class PersistentVolumeClaim(APIResource):
    def __init__(self):
        super().__init__(api_name="PersistentVolumeClaim")


class Node(APIResource):
    def __init__(self):
        super().__init__(api_name="Node")


class ComponentStatus(APIResource):
    def __init__(self):
        super().__init__(api_name="ComponentStatus")


class StatefulSet(APIResource):
    def __init__(self):
        super().__init__(api_name="StatefulSet")


class RoleBinding(APIResource):
    def __init__(self):
        super().__init__(api_name="RoleBinding")


class ClusterRoleBinding(APIResource):
    def __init__(self):
        super().__init__(api_name="ClusterRoleBinding")


class Endpoints(APIResource):
    def __init__(self):
        super().__init__(api_name="Endpoints")


class LocalSubjectAccessReview(APIResource):
    def __init__(self):
        super().__init__(api_name="LocalSubjectAccessReview")


class EndpointSlice(APIResource):
    def __init__(self):
        super().__init__(api_name="EndpointSlice")


class ControllerRevision(APIResource):
    def __init__(self):
        super().__init__(api_name="ControllerRevision")
