from base import K8sObject

"""
Kubernetes VolumeMount component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class VolumeMount(K8sObject):
    def __init__(self):
        super().__init__(name="VolumeMount")


"""
Kubernetes ManagedField component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class ManagedField(K8sObject):
    def __init__(self):
        super().__init__(name="ManagedField")


"""
Kubernetes HostAlias component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class HostAlias(K8sObject):
    def __init__(self):
        super().__init__(name="HostAlias")


"""
Kubernetes NetworkPolicyIngress component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class NetworkPolicyIngress(K8sObject):
    def __init__(self):
        super().__init__(name="NetworkPolicyIngress")


"""
Kubernetes VolumeClaimTemplate component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class VolumeClaimTemplate(K8sObject):
    def __init__(self):
        super().__init__(name="VolumeClaimTemplate")


"""
Kubernetes DownwardAPIItem component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class DownwardAPIItem(K8sObject):
    def __init__(self):
        super().__init__(name="DownwardAPIItem")


"""
Kubernetes NodePreferredAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class NodePreferredAffinity(K8sObject):
    def __init__(self):
        super().__init__(name="NodePreferredAffinity")


"""
Kubernetes Volume component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class Volume(K8sObject):
    def __init__(self):
        super().__init__(name="Volume")


"""
Kubernetes IngressTLS component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class IngressTLS(K8sObject):
    def __init__(self):
        super().__init__(name="IngressTLS")


"""
Kubernetes IngressRulePath component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class IngressRulePath(K8sObject):
    def __init__(self):
        super().__init__(name="IngressRulePath")


"""
Kubernetes AllowedFlexVolume component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class AllowedFlexVolume(K8sObject):
    def __init__(self):
        super().__init__(name="AllowedFlexVolume")


"""
Kubernetes ComponentStatusCondition component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class ComponentStatusCondition(K8sObject):
    def __init__(self):
        super().__init__(name="ComponentStatusCondition")


"""
Kubernetes NonResourceAttribute component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class NonResourceAttribute(K8sObject):
    def __init__(self):
        super().__init__(name="NonResourceAttribute")


"""
Kubernetes EnvironmentVariable component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class EnvironmentVariable(K8sObject):
    def __init__(self):
        super().__init__(name="EnvironmentVariable")


"""
Kubernetes Webhook component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class Webhook(K8sObject):
    def __init__(self):
        super().__init__(name="Webhook")


"""
Kubernetes ProjectedVolumeSource component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class ProjectedVolumeSource(K8sObject):
    def __init__(self):
        super().__init__(name="ProjectedVolumeSource")


"""
Kubernetes AllowedHostPath component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class AllowedHostPath(K8sObject):
    def __init__(self):
        super().__init__(name="AllowedHostPath")


"""
Kubernetes ImagePullSecret component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class ImagePullSecret(K8sObject):
    def __init__(self):
        super().__init__(name="ImagePullSecret")


"""
Kubernetes SubsetPort component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class SubsetPort(K8sObject):
    def __init__(self):
        super().__init__(name="SubsetPort")


"""
Kubernetes RoleRule component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class RoleRule(K8sObject):
    def __init__(self):
        super().__init__(name="RoleRule")


"""
Kubernetes ServicePort component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class ServicePort(K8sObject):
    def __init__(self):
        super().__init__(name="ServicePort")


"""
Kubernetes Selector component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class Selector(K8sObject):
    def __init__(self):
        super().__init__(name="Selector")


"""
Kubernetes Range component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class Range(K8sObject):
    def __init__(self):
        super().__init__(name="Range")


"""
Kubernetes AllowedCSIDriver component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class AllowedCSIDriver(K8sObject):
    def __init__(self):
        super().__init__(name="AllowedCSIDriver")


"""
Kubernetes PrinterColumn component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class PrinterColumn(K8sObject):
    def __init__(self):
        super().__init__(name="PrinterColumn")


"""
Kubernetes ContainerPort component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class ContainerPort(K8sObject):
    def __init__(self):
        super().__init__(name="ContainerPort")


"""
Kubernetes ConfigMapItem component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class ConfigMapItem(K8sObject):
    def __init__(self):
        super().__init__(name="ConfigMapItem")


"""
Kubernetes NodeSelectorTerm component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class NodeSelectorTerm(K8sObject):
    def __init__(self):
        super().__init__(name="NodeSelectorItem")


"""
Kubernetes DNSConfigOptions component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class DNSConfigOptions(K8sObject):
    def __init__(self):
        super().__init__(name="DNSConfigOptions")


"""
Kubernetes Metadata component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class Metadata(K8sObject):
    def __init__(self):
        super().__init__(name="Metadata")


"""
Kubernetes ClusterRule component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class ClusterRule(K8sObject):
    def __init__(self):
        super().__init__(name="ClusterRule")


"""
Kubernetes PodPreferredAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class PodPreferredAffinity(K8sObject):
    def __init__(self):
        super().__init__(name="PodPreferredAffinity")


"""
Kubernetes ResourceDefinitionVersion component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class ResourceDefinitionVersion(K8sObject):
    def __init__(self):
        super().__init__(name="ResourceDefinitionVersion")


"""
Kubernetes AllowedTopology component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class AllowedTopology(K8sObject):
    def __init__(self):
        super().__init__(name="AllowedTopology")


"""
Kubernetes SecurityContext component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class SecurityContext(K8sObject):
    def __init__(self):
        super().__init__(name="SecurityContext")


"""
Kubernetes LifecycleDefinition component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class LifecycleDefinition(K8sObject):
    def __init__(self):
        super().__init__(name="LifecycleDefinition")


"""
Kubernetes OwnerReference component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class OwnerReference(K8sObject):
    def __init__(self):
        super().__init__(name="OwnerReference")


"""
Kubernetes SecretItem component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class SecretItem(K8sObject):
    def __init__(self):
        super().__init__(name="SecretItem")


"""
Kubernetes PodAntiAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class PodAntiAffinity(K8sObject):
    def __init__(self):
        super().__init__(name="PodAntiAffinity")


"""
Kubernetes Container component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class Container(K8sObject):
    def __init__(self):
        super().__init__(name="Container")


"""
Kubernetes Address component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class Address(K8sObject):
    def __init__(self):
        super().__init__(name="Address")


"""
Kubernetes IngressRule component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class IngressRule(K8sObject):
    def __init__(self):
        super().__init__(name="IngressRule")


"""
Kubernetes ScopeSelector component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class ScopeSelector(K8sObject):
    def __init__(self):
        super().__init__(name="ScopeSelector")


"""
Kubernetes UserGroup component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class UserGroup(K8sObject):
    def __init__(self):
        super().__init__(name="UserGroup")


"""
Kubernetes PodRequiredAntiAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class PodRequiredAntiAffinity(K8sObject):
    def __init__(self):
        super().__init__(name="PodRequiredAntiAffinity")


"""
Kubernetes EnvironmentVariableSource component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class EnvironmentVariableSource(K8sObject):
    def __init__(self):
        super().__init__(name="EnvironmentVariableSource")


"""
Kubernetes Limit component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class Limit(K8sObject):
    def __init__(self):
        super().__init__(name="Limit")


"""
Kubernetes NodeAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class NodeAffinity(K8sObject):
    def __init__(self):
        super().__init__(name="NodeAffinity")


"""
Kubernetes NetworkPolicyEgress component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class NetworkPolicyEgress(K8sObject):
    def __init__(self):
        super().__init__(name="NetworkPolicyEgress")


"""
Kubernetes Subset component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class Subset(K8sObject):
    def __init__(self):
        super().__init__(name="Subset")


"""
Kubernetes DNSConfig component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class DNSConfig(K8sObject):
    def __init__(self):
        super().__init__(name="DNSConfig")


"""
Kubernetes PodAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class PodAffinity(K8sObject):
    def __init__(self):
        super().__init__(name="PodAffinity")


"""
Kubernetes MatchExpression component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class MatchExpression(K8sObject):
    def __init__(self):
        super().__init__(name="MatchExpression")


"""
Kubernetes Probe component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class Probe(K8sObject):
    def __init__(self):
        super().__init__(name="Probe")


"""
Kubernetes ServiceAccountSecret component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class ServiceAccountSecret(K8sObject):
    def __init__(self):
        super().__init__(name="ServiceAccountSecret")


"""
Kubernetes ReadinessGate component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class ReadinessGate(K8sObject):
    def __init__(self):
        super().__init__(name="ReadinessGate")


"""
Kubernetes Toleration component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class Toleration(K8sObject):
    def __init__(self):
        super().__init__(name="Toleration")


"""
Kubernetes NodeRequiredAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class NodeRequiredAffinity(K8sObject):
    def __init__(self):
        super().__init__(name="NodeRequiredAffinity")


"""
Kubernetes MatchLabelExpression component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class MatchLabelExpression(K8sObject):
    def __init__(self):
        super().__init__(name="MatchLabelExpression")


"""
Kubernetes Sysctl component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class Sysctl(K8sObject):
    def __init__(self):
        super().__init__(name="Sysctl")


"""
Kubernetes HTTPHeader component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class HTTPHeader(K8sObject):
    def __init__(self):
        super().__init__(name="HTTPHeader")


"""
Kubernetes ResourceAttribute component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class ResourceAttribute(K8sObject):
    def __init__(self):
        super().__init__(name="ResourceAttribute")


"""
Kubernetes ClientConfig component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class ClientConfig(K8sObject):
    def __init__(self):
        super().__init__(name="ClientConfig")


"""
Kubernetes VolumeDevice component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class VolumeDevice(K8sObject):
    def __init__(self):
        super().__init__(name="VolumeDevice")


"""
Kubernetes PodPreferredAntiAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class PodPreferredAntiAffinity(K8sObject):
    def __init__(self):
        super().__init__(name="PodPreferredAntiAffinity")


"""
Kubernetes PodRequiredAffinity component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class PodRequiredAffinity(K8sObject):
    def __init__(self):
        super().__init__(name="PodRequiredAffinity")


"""
Kubernetes Taint component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class Taint(K8sObject):
    def __init__(self):
        super().__init__(name="Taint")


"""
Kubernetes ContainerSpec component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class ContainerSpec(K8sObject):
    def __init__(self):
        super().__init__(name="ContainerSpec")


"""
Kubernetes ClusterRoleBindingSubject component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class ClusterRoleBindingSubject(K8sObject):
    def __init__(self):
        super().__init__(name="ClusterRoleBindingSubject")


"""
Kubernetes CSINodeDriver component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
"""
class CSINodeDriver(K8sObject):
    def __init__(self):
        super().__init__(name="CSINodeDriver")
