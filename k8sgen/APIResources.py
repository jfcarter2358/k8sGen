from k8sgen import base
from k8sgen.base import K8sObject

'''
Kubernetes DaemonSet component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class DaemonSet(K8sObject):
    def __init__(self):
        super().__init__(name="DaemonSet")

'''
Kubernetes ReplicationController component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ReplicationController(K8sObject):
    def __init__(self):
        super().__init__(name="ReplicationController")

'''
Kubernetes TokenReview component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class TokenReview(K8sObject):
    def __init__(self):
        super().__init__(name="TokenReview")

'''
Kubernetes StorageClass component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class StorageClass(K8sObject):
    def __init__(self):
        super().__init__(name="StorageClass")

'''
Kubernetes CustomResourceDefinition component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class CustomResourceDefinition(K8sObject):
    def __init__(self):
        super().__init__(name="CustomResourceDefinition")

'''
Kubernetes CSIDriver component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class CSIDriver(K8sObject):
    def __init__(self):
        super().__init__(name="CSIDriver")

'''
Kubernetes Binding component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Binding(K8sObject):
    def __init__(self):
        super().__init__(name="Binding")

'''
Kubernetes SelfSubjectRulesReview component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class SelfSubjectRulesReview(K8sObject):
    def __init__(self):
        super().__init__(name="SelfSubjectRulesReview")

'''
Kubernetes Role component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Role(K8sObject):
    def __init__(self):
        super().__init__(name="Role")

'''
Kubernetes Deployment component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Deployment(K8sObject):
    def __init__(self):
        super().__init__(name="Deployment")

'''
Kubernetes ValidatingWebhookConfiguration component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ValidatingWebhookConfiguration(K8sObject):
    def __init__(self):
        super().__init__(name="ValidatingWebhookConfiguration")

'''
Kubernetes PodSecurityPolicy component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class PodSecurityPolicy(K8sObject):
    def __init__(self):
        super().__init__(name="PodSecurityPolicy")

'''
Kubernetes CronJob component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class CronJob(K8sObject):
    def __init__(self):
        super().__init__(name="CronJob")

'''
Kubernetes RuntimeClass component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class RuntimeClass(K8sObject):
    def __init__(self):
        super().__init__(name="RuntimeClass")

'''
Kubernetes ClusterRole component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ClusterRole(K8sObject):
    def __init__(self):
        super().__init__(name="ClusterRole")

'''
Kubernetes Service component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Service(K8sObject):
    def __init__(self):
        super().__init__(name="Service")

'''
Kubernetes IngressClass component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class IngressClass(K8sObject):
    def __init__(self):
        super().__init__(name="IngressClass")

'''
Kubernetes Ingress component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Ingress(K8sObject):
    def __init__(self):
        super().__init__(name="Ingress")

'''
Kubernetes PriorityClass component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class PriorityClass(K8sObject):
    def __init__(self):
        super().__init__(name="PriorityClass")

'''
Kubernetes PersistentVolume component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class PersistentVolume(K8sObject):
    def __init__(self):
        super().__init__(name="PersistentVolume")

'''
Kubernetes Event component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Event(K8sObject):
    def __init__(self):
        super().__init__(name="Event")

'''
Kubernetes CSINode component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class CSINode(K8sObject):
    def __init__(self):
        super().__init__(name="CSINode")

'''
Kubernetes ReplicaSet component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ReplicaSet(K8sObject):
    def __init__(self):
        super().__init__(name="ReplicaSet")

'''
Kubernetes MutatingWebhookConfiguration component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class MutatingWebhookConfiguration(K8sObject):
    def __init__(self):
        super().__init__(name="MutatingWebhookConfiguration")

'''
Kubernetes ServiceAccount component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ServiceAccount(K8sObject):
    def __init__(self):
        super().__init__(name="ServiceAccount")

'''
Kubernetes CertificateSigningRequest component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class CertificateSigningRequest(K8sObject):
    def __init__(self):
        super().__init__(name="CertificateSigningRequest")

'''
Kubernetes SubjectAccessReview component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class SubjectAccessReview(K8sObject):
    def __init__(self):
        super().__init__(name="SubjectAccessReview")

'''
Kubernetes APIService component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class APIService(K8sObject):
    def __init__(self):
        super().__init__(name="APIService")

'''
Kubernetes ConfigMap component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ConfigMap(K8sObject):
    def __init__(self):
        super().__init__(name="ConfigMap")

'''
Kubernetes SelfSubjectAccessReview component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class SelfSubjectAccessReview(K8sObject):
    def __init__(self):
        super().__init__(name="SelfSubjectAccessReview")

'''
Kubernetes Lease component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Lease(K8sObject):
    def __init__(self):
        super().__init__(name="Lease")

'''
Kubernetes Job component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Job(K8sObject):
    def __init__(self):
        super().__init__(name="Job")

'''
Kubernetes PodDisruptionBudget component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class PodDisruptionBudget(K8sObject):
    def __init__(self):
        super().__init__(name="PodDisruptionBudget")

'''
Kubernetes Namespace component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Namespace(K8sObject):
    def __init__(self):
        super().__init__(name="Namespace")

'''
Kubernetes HorizontalPodAutoscaler component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class HorizontalPodAutoscaler(K8sObject):
    def __init__(self):
        super().__init__(name="HorizontalPodAutoscaler")

'''
Kubernetes Pod component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Pod(K8sObject):
    def __init__(self):
        super().__init__(name="Pod")

'''
Kubernetes PodTemplate component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class PodTemplate(K8sObject):
    def __init__(self):
        super().__init__(name="PodTemplate")

'''
Kubernetes Secret component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Secret(K8sObject):
    def __init__(self):
        super().__init__(name="Secret")

'''
Kubernetes LimitRange component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class LimitRange(K8sObject):
    def __init__(self):
        super().__init__(name="LimitRange")

'''
Kubernetes NetworkPolicy component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class NetworkPolicy(K8sObject):
    def __init__(self):
        super().__init__(name="NetworkPolicy")

'''
Kubernetes ResourceQuota component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ResourceQuota(K8sObject):
    def __init__(self):
        super().__init__(name="ResourceQuota")

'''
Kubernetes VolumeAttachment component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class VolumeAttachment(K8sObject):
    def __init__(self):
        super().__init__(name="VolumeAttachment")

'''
Kubernetes PersistentVolumeClaim component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class PersistentVolumeClaim(K8sObject):
    def __init__(self):
        super().__init__(name="PersistentVolumeClaim")

'''
Kubernetes Node component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Node(K8sObject):
    def __init__(self):
        super().__init__(name="Node")

'''
Kubernetes ComponentStatus component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ComponentStatus(K8sObject):
    def __init__(self):
        super().__init__(name="ComponentStatus")

'''
Kubernetes StatefulSet component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class StatefulSet(K8sObject):
    def __init__(self):
        super().__init__(name="StatefulSet")

'''
Kubernetes RoleBinding component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class RoleBinding(K8sObject):
    def __init__(self):
        super().__init__(name="RoleBinding")

'''
Kubernetes ClusterRoleBinding component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ClusterRoleBinding(K8sObject):
    def __init__(self):
        super().__init__(name="ClusterRoleBinding")

'''
Kubernetes Endpoints component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class Endpoints(K8sObject):
    def __init__(self):
        super().__init__(name="Endpoints")

'''
Kubernetes LocalSubjectAccessReview component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class LocalSubjectAccessReview(K8sObject):
    def __init__(self):
        super().__init__(name="LocalSubjectAccessReview")

'''
Kubernetes EndpointSlice component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class EndpointSlice(K8sObject):
    def __init__(self):
        super().__init__(name="EndpointSlice")

'''
Kubernetes ControllerRevision component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class ControllerRevision(K8sObject):
    def __init__(self):
        super().__init__(name="ControllerRevision")

