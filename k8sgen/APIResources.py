from base import K8sObject


class DaemonSet(K8sObject):
    def __init__(self):
        super().__init__(name="DaemonSet")


class ReplicationController(K8sObject):
    def __init__(self):
        super().__init__(name="ReplicationController")


class TokenReview(K8sObject):
    def __init__(self):
        super().__init__(name="TokenReview")


class StorageClass(K8sObject):
    def __init__(self):
        super().__init__(name="StorageClass")


class CustomResourceDefinition(K8sObject):
    def __init__(self):
        super().__init__(name="CustomResourceDefinition")


class CSIDriver(K8sObject):
    def __init__(self):
        super().__init__(name="CSIDriver")


class Binding(K8sObject):
    def __init__(self):
        super().__init__(name="Binding")


class SelfSubjectRulesReview(K8sObject):
    def __init__(self):
        super().__init__(name="SelfSubjectRulesReview")


class Role(K8sObject):
    def __init__(self):
        super().__init__(name="Role")


class Deployment(K8sObject):
    def __init__(self):
        super().__init__(name="Deployment")


class ValidatingWebhookConfiguration(K8sObject):
    def __init__(self):
        super().__init__(name="ValidatingWebhookConfiguration")


class PodSecurityPolicy(K8sObject):
    def __init__(self):
        super().__init__(name="PodSecurityPolicy")


class CronJob(K8sObject):
    def __init__(self):
        super().__init__(name="CronJob")


class RuntimeClass(K8sObject):
    def __init__(self):
        super().__init__(name="RuntimeClass")


class ClusterRole(K8sObject):
    def __init__(self):
        super().__init__(name="ClusterRole")


class Service(K8sObject):
    def __init__(self):
        super().__init__(name="Service")


class IngressClass(K8sObject):
    def __init__(self):
        super().__init__(name="IngressClass")


class Ingress(K8sObject):
    def __init__(self):
        super().__init__(name="Ingress")


class PriorityClass(K8sObject):
    def __init__(self):
        super().__init__(name="PriorityClass")


class PersistentVolume(K8sObject):
    def __init__(self):
        super().__init__(name="PersistentVolume")


class Event(K8sObject):
    def __init__(self):
        super().__init__(name="Event")


class CSINode(K8sObject):
    def __init__(self):
        super().__init__(name="CSINode")


class ReplicaSet(K8sObject):
    def __init__(self):
        super().__init__(name="ReplicaSet")


class MutatingWebhookConfiguration(K8sObject):
    def __init__(self):
        super().__init__(name="MutatingWebhookConfiguration")


class ServiceAccount(K8sObject):
    def __init__(self):
        super().__init__(name="ServiceAccount")


class CertificateSigningRequest(K8sObject):
    def __init__(self):
        super().__init__(name="CertificateSigningRequest")


class SubjectAccessReview(K8sObject):
    def __init__(self):
        super().__init__(name="SubjectAccessReview")


class APIService(K8sObject):
    def __init__(self):
        super().__init__(name="APIService")


class ConfigMap(K8sObject):
    def __init__(self):
        super().__init__(name="ConfigMap")


class SelfSubjectAccessReview(K8sObject):
    def __init__(self):
        super().__init__(name="SelfSubjectAccessReview")


class Lease(K8sObject):
    def __init__(self):
        super().__init__(name="Lease")


class Job(K8sObject):
    def __init__(self):
        super().__init__(name="Job")


class PodDisruptionBudget(K8sObject):
    def __init__(self):
        super().__init__(name="PodDisruptionBudget")


class Namespace(K8sObject):
    def __init__(self):
        super().__init__(name="Namespace")


class HorizontalPodAutoscaler(K8sObject):
    def __init__(self):
        super().__init__(name="HorizontalPodAutoscaler")


class Pod(K8sObject):
    def __init__(self):
        super().__init__(name="Pod")


class PodTemplate(K8sObject):
    def __init__(self):
        super().__init__(name="PodTemplate")


class Secret(K8sObject):
    def __init__(self):
        super().__init__(name="Secret")


class LimitRange(K8sObject):
    def __init__(self):
        super().__init__(name="LimitRange")


class NetworkPolicy(K8sObject):
    def __init__(self):
        super().__init__(name="NetworkPolicy")


class ResourceQuota(K8sObject):
    def __init__(self):
        super().__init__(name="ResourceQuota")


class VolumeAttachment(K8sObject):
    def __init__(self):
        super().__init__(name="VolumeAttachment")


class PersistentVolumeClaim(K8sObject):
    def __init__(self):
        super().__init__(name="PersistentVolumeClaim")


class Node(K8sObject):
    def __init__(self):
        super().__init__(name="Node")


class ComponentStatus(K8sObject):
    def __init__(self):
        super().__init__(name="ComponentStatus")


class StatefulSet(K8sObject):
    def __init__(self):
        super().__init__(name="StatefulSet")


class RoleBinding(K8sObject):
    def __init__(self):
        super().__init__(name="RoleBinding")


class ClusterRoleBinding(K8sObject):
    def __init__(self):
        super().__init__(name="ClusterRoleBinding")


class Endpoints(K8sObject):
    def __init__(self):
        super().__init__(name="Endpoints")


class LocalSubjectAccessReview(K8sObject):
    def __init__(self):
        super().__init__(name="LocalSubjectAccessReview")


class EndpointSlice(K8sObject):
    def __init__(self):
        super().__init__(name="EndpointSlice")


class ControllerRevision(K8sObject):
    def __init__(self):
        super().__init__(name="ControllerRevision")
