ReplicationController
==================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

========

Functions
---------

set
+++

Set any specific field to a value

**Args**

* \*\*kwargs

    * Arbitrary list of keys as variables in formation of YAML path separated by underscores with their assocaited values. For example, to set the value at

    .. code-block:: JSON

        {
            "spec": {
                "template": {
                    "spec": ""
                }
            }
        }

    use

    .. code-block:: Python

        obj.set(spec_template_spec="foobar")

    * You can also specify an incomplete path and k8sGen will attempt to find a unique location whose ending path matches what you have specified. For the case of the above structure, running

    .. code-block:: Python

        obj.set(template_spec="foobar")

    will set the same location because the only path that ends in 'template/spec' is 'spec/template/spec'

**Returns**

List of return values for each variable set

Possible return values include:

* True : value was set successfully
* (False, 'invalid key name') : the key you are trying to set does not exist for this object
* (False, 'abniguous key name') : the key you are trying to set does not refer to a unique location

get
+++

Get the values that have been set for specific fields

**Args** 

* \*args
    * Arbitrary list of keys as variables in formation of YAML path separated by underscores

**Returns**

List of return values for each variable set

Possible return values include:

* {Value} : The key's value
* (False, 'invalid key name') : the key you are trying to set does not exist for this object

Key Names and Types
-------------------

+----------------------------------------------------------------------------------------------+-------------------------------+
| Key                                                                                          | Type                          |
+==============================================================================================+===============================+
| apiVersion                                                                                   | v1                            |
+----------------------------------------------------------------------------------------------+-------------------------------+
| kind                                                                                         | ReplicationController         |
+----------------------------------------------------------------------------------------------+-------------------------------+
| metadata                                                                                     | <COMPONENT.Metadata>          |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_minReadySeconds                                                                         | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_replicas                                                                                | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_selector                                                                                | <map[string]string>           |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_metadata                                                                       | <COMPONENT.Metadata>          |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_activeDeadlineSeconds                                                     | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_affinity_nodeAffinity                                                     | <COMPONENT.NodeAffinity>      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_affinity_podAffinity                                                      | <COMPONENT.PodAffinity>       |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_affinity_podAntiAffinity                                                  | <COMPONENT.PodAntiAffinity>   |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_automountServiceAccountToken                                              | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_containers                                                                | <[]COMPONENT.Container>       |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_dnsConfig                                                                 | <COMPONENT.DNSConfig>         |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_dnsPolicy                                                                 | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_enableServiceLinks                                                        | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_args                                                  | <[]string>                    |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_command                                               | <[]string>                    |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_env_name                                              | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_env_value                                             | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_env_valueFrom_configMapKeyRef_key                     | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_env_valueFrom_configMapKeyRef_name                    | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_env_valueFrom_configMapKeyRef_optional                | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_env_valueFrom_fieldRef_apiVersion                     | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_env_valueFrom_fieldRef_fieldPath                      | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_env_valueFrom_resourceFieldRef_containerName          | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_env_valueFrom_resourceFieldRef_divisor                | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_env_valueFrom_resourceFieldRef_resource               | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_env_valueFrom_secretKeyRef_key                        | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_env_valueFrom_secretKeyRef_name                       | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_env_valueFrom_secretKeyRef_optional                   | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_envFrom_configMapRef_name                             | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_envFrom_configMapRef_optional                         | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_envFrom_prefix                                        | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_envFrom_secretRef_name                                | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_envFrom_secretRef_optional                            | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_image                                                 | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_imagePullPolicy                                       | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_postStart_exec_command                      | <[]string>                    |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_postStart_httpGet_host                      | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_postStart_httpGet_httpHeaders_name          | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_postStart_httpGet_httpHeaders_value         | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_postStart_httpGet_path                      | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_postStart_httpGet_port                      | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_postStart_httpGet_scheme                    | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_postStart_tcpSocket_host                    | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_postStart_tcpSocket_port                    | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_preStop_exec_command                        | <[]string>                    |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_preStop_httpGet_host                        | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_preStop_httpGet_httpHeaders_name            | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_preStop_httpGet_httpHeaders_value           | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_preStop_httpGet_path                        | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_preStop_httpGet_port                        | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_preStop_httpGet_scheme                      | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_preStop_tcpSocket_host                      | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_lifecycle_preStop_tcpSocket_port                      | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_livenessProbe_exec_command                            | <[]string>                    |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_livenessProbe_failureThreshold                        | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_livenessProbe_httpGet_host                            | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_livenessProbe_httpGet_httpHeaders_name                | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_livenessProbe_httpGet_httpHeaders_value               | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_livenessProbe_httpGet_path                            | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_livenessProbe_httpGet_port                            | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_livenessProbe_httpGet_scheme                          | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_livenessProbe_initialDelaySeconds                     | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_livenessProbe_periodSeconds                           | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_livenessProbe_successThreshold                        | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_livenessProbe_tcpSocket_host                          | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_livenessProbe_tcpSocket_port                          | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_livenessProbe_timeoutSeconds                          | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_name                                                  | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_ports_containerPort                                   | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_ports_hostIP                                          | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_ports_hostPort                                        | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_ports_name                                            | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_ports_protocol                                        | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_readinessProbe_exec_command                           | <[]string>                    |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_readinessProbe_failureThreshold                       | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_readinessProbe_httpGet_host                           | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_readinessProbe_httpGet_httpHeaders_name               | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_readinessProbe_httpGet_httpHeaders_value              | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_readinessProbe_httpGet_path                           | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_readinessProbe_httpGet_port                           | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_readinessProbe_httpGet_scheme                         | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_readinessProbe_initialDelaySeconds                    | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_readinessProbe_periodSeconds                          | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_readinessProbe_successThreshold                       | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_readinessProbe_tcpSocket_host                         | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_readinessProbe_tcpSocket_port                         | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_readinessProbe_timeoutSeconds                         | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_resources_limits                                      | <map[string]string>           |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_resources_requests                                    | <map[string]string>           |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_securityContext_allowPrivilegeEscalation              | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_securityContext_capabilities_add                      | <[]string>                    |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_securityContext_capabilities_drop                     | <[]string>                    |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_securityContext_privileged                            | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_securityContext_procMount                             | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_securityContext_readOnlyRootFilesystem                | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_securityContext_runAsGroup                            | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_securityContext_runAsNonRoot                          | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_securityContext_runAsUser                             | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_securityContext_seLinuxOptions_level                  | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_securityContext_seLinuxOptions_role                   | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_securityContext_seLinuxOptions_type                   | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_securityContext_seLinuxOptions_user                   | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_securityContext_windowsOptions_gmsaCredentialSpec     | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_securityContext_windowsOptions_gmsaCredentialSpecName | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_securityContext_windowsOptions_runAsUserName          | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_startupProbe_exec_command                             | <[]string>                    |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_startupProbe_failureThreshold                         | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_startupProbe_httpGet_host                             | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_startupProbe_httpGet_httpHeaders_name                 | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_startupProbe_httpGet_httpHeaders_value                | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_startupProbe_httpGet_path                             | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_startupProbe_httpGet_port                             | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_startupProbe_httpGet_scheme                           | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_startupProbe_initialDelaySeconds                      | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_startupProbe_periodSeconds                            | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_startupProbe_successThreshold                         | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_startupProbe_tcpSocket_host                           | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_startupProbe_tcpSocket_port                           | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_startupProbe_timeoutSeconds                           | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_stdin                                                 | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_stdinOnce                                             | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_targetContainerName                                   | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_terminationMessagePath                                | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_terminationMessagePolicy                              | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_tty                                                   | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_volumeDevices_devicePath                              | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_volumeDevices_name                                    | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_volumeMounts_mountPath                                | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_volumeMounts_mountPropagation                         | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_volumeMounts_name                                     | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_volumeMounts_readOnly                                 | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_volumeMounts_subPath                                  | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_volumeMounts_subPathExpr                              | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_ephemeralContainers_workingDir                                            | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_hostAliases                                                               | <[]COMPONENT.HostAlias>       |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_hostIPC                                                                   | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_hostNetwork                                                               | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_hostPID                                                                   | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_hostname                                                                  | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_imagePullSecrets                                                          | <[]COMPONENT.ImagePullSecret> |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_initContainers                                                            | <[]COMPONENT.Container>       |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_nodeName                                                                  | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_nodeSelector                                                              | <map[string]string>           |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_overhead                                                                  | <map[string]string>           |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_preemptionPolicy                                                          | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_priority                                                                  | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_priorityClassName                                                         | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_readinessGates                                                            | <[]COMPONENT.ReadinessGate>   |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_restartPolicy                                                             | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_runtimeClassName                                                          | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_schedulerName                                                             | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_securityContext                                                           | <COMPONENT.SecurityContext>   |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_serviceAccount                                                            | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_serviceAccountName                                                        | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_shareProcessNamespace                                                     | <boolean>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_subdomain                                                                 | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_terminationGracePeriodSeconds                                             | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_tolerations                                                               | <[]COMPONENT.Tolerations>     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_topologySpreadConstraints_labelSelector_matchExpressions_key              | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_topologySpreadConstraints_labelSelector_matchExpressions_operator         | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_topologySpreadConstraints_labelSelector_matchExpressions_values           | <[]string>                    |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_topologySpreadConstraints_labelSelector_matchLabels                       | <map[string]string>           |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_topologySpreadConstraints_maxSkew                                         | <integer>                     |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_topologySpreadConstraints_topologyKey                                     | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_topologySpreadConstraints_whenUnsatisfiable                               | <string>                      |
+----------------------------------------------------------------------------------------------+-------------------------------+
| spec_template_spec_volumes                                                                   | <[]COMPONENT.Volume>          |
+----------------------------------------------------------------------------------------------+-------------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "apiVersion": "v1",
        "kind": "ReplicationController",
        "metadata": "<COMPONENT.Metadata>",
        "spec": {
            "minReadySeconds": "<integer>",
            "replicas": "<integer>",
            "selector": "<map[string]string>",
            "template": {
                "metadata": "<COMPONENT.Metadata>",
                "spec": {
                    "activeDeadlineSeconds": "<integer>",
                    "affinity": {
                        "nodeAffinity": "<COMPONENT.NodeAffinity>",
                        "podAffinity": "<COMPONENT.PodAffinity>",
                        "podAntiAffinity": "<COMPONENT.PodAntiAffinity>"
                    },
                    "automountServiceAccountToken": "<boolean>",
                    "containers": "<[]COMPONENT.Container>",
                    "dnsConfig": "<COMPONENT.DNSConfig>",
                    "dnsPolicy": "<string>",
                    "enableServiceLinks": "<boolean>",
                    "ephemeralContainers": [
                        {
                            "args": "<[]string>",
                            "command": "<[]string>",
                            "env": [
                                {
                                    "name": "<string>",
                                    "value": "<string>",
                                    "valueFrom": {
                                        "configMapKeyRef": {
                                            "key": "<string>",
                                            "name": "<string>",
                                            "optional": "<boolean>"
                                        },
                                        "fieldRef": {
                                            "apiVersion": "<string>",
                                            "fieldPath": "<string>"
                                        },
                                        "resourceFieldRef": {
                                            "containerName": "<string>",
                                            "divisor": "<string>",
                                            "resource": "<string>"
                                        },
                                        "secretKeyRef": {
                                            "key": "<string>",
                                            "name": "<string>",
                                            "optional": "<boolean>"
                                        }
                                    }
                                }
                            ],
                            "envFrom": [
                                {
                                    "configMapRef": {
                                        "name": "<string>",
                                        "optional": "<boolean>"
                                    },
                                    "prefix": "<string>",
                                    "secretRef": {
                                        "name": "<string>",
                                        "optional": "<boolean>"
                                    }
                                }
                            ],
                            "image": "<string>",
                            "imagePullPolicy": "<string>",
                            "lifecycle": {
                                "postStart": {
                                    "exec": {
                                        "command": "<[]string>"
                                    },
                                    "httpGet": {
                                        "host": "<string>",
                                        "httpHeaders": [
                                            {
                                                "name": "<string>",
                                                "value": "<string>"
                                            }
                                        ],
                                        "path": "<string>",
                                        "port": "<string>",
                                        "scheme": "<string>"
                                    },
                                    "tcpSocket": {
                                        "host": "<string>",
                                        "port": "<string>"
                                    }
                                },
                                "preStop": {
                                    "exec": {
                                        "command": "<[]string>"
                                    },
                                    "httpGet": {
                                        "host": "<string>",
                                        "httpHeaders": [
                                            {
                                                "name": "<string>",
                                                "value": "<string>"
                                            }
                                        ],
                                        "path": "<string>",
                                        "port": "<string>",
                                        "scheme": "<string>"
                                    },
                                    "tcpSocket": {
                                        "host": "<string>",
                                        "port": "<string>"
                                    }
                                }
                            },
                            "livenessProbe": {
                                "exec": {
                                    "command": "<[]string>"
                                },
                                "failureThreshold": "<integer>",
                                "httpGet": {
                                    "host": "<string>",
                                    "httpHeaders": [
                                        {
                                            "name": "<string>",
                                            "value": "<string>"
                                        }
                                    ],
                                    "path": "<string>",
                                    "port": "<string>",
                                    "scheme": "<string>"
                                },
                                "initialDelaySeconds": "<integer>",
                                "periodSeconds": "<integer>",
                                "successThreshold": "<integer>",
                                "tcpSocket": {
                                    "host": "<string>",
                                    "port": "<string>"
                                },
                                "timeoutSeconds": "<integer>"
                            },
                            "name": "<string>",
                            "ports": [
                                {
                                    "containerPort": "<integer>",
                                    "hostIP": "<string>",
                                    "hostPort": "<integer>",
                                    "name": "<string>",
                                    "protocol": "<string>"
                                }
                            ],
                            "readinessProbe": {
                                "exec": {
                                    "command": "<[]string>"
                                },
                                "failureThreshold": "<integer>",
                                "httpGet": {
                                    "host": "<string>",
                                    "httpHeaders": [
                                        {
                                            "name": "<string>",
                                            "value": "<string>"
                                        }
                                    ],
                                    "path": "<string>",
                                    "port": "<string>",
                                    "scheme": "<string>"
                                },
                                "initialDelaySeconds": "<integer>",
                                "periodSeconds": "<integer>",
                                "successThreshold": "<integer>",
                                "tcpSocket": {
                                    "host": "<string>",
                                    "port": "<string>"
                                },
                                "timeoutSeconds": "<integer>"
                            },
                            "resources": {
                                "limits": "<map[string]string>",
                                "requests": "<map[string]string>"
                            },
                            "securityContext": {
                                "allowPrivilegeEscalation": "<boolean>",
                                "capabilities": {
                                    "add": "<[]string>",
                                    "drop": "<[]string>"
                                },
                                "privileged": "<boolean>",
                                "procMount": "<string>",
                                "readOnlyRootFilesystem": "<boolean>",
                                "runAsGroup": "<integer>",
                                "runAsNonRoot": "<boolean>",
                                "runAsUser": "<integer>",
                                "seLinuxOptions": {
                                    "level": "<string>",
                                    "role": "<string>",
                                    "type": "<string>",
                                    "user": "<string>"
                                },
                                "windowsOptions": {
                                    "gmsaCredentialSpec": "<string>",
                                    "gmsaCredentialSpecName": "<string>",
                                    "runAsUserName": "<string>"
                                }
                            },
                            "startupProbe": {
                                "exec": {
                                    "command": "<[]string>"
                                },
                                "failureThreshold": "<integer>",
                                "httpGet": {
                                    "host": "<string>",
                                    "httpHeaders": [
                                        {
                                            "name": "<string>",
                                            "value": "<string>"
                                        }
                                    ],
                                    "path": "<string>",
                                    "port": "<string>",
                                    "scheme": "<string>"
                                },
                                "initialDelaySeconds": "<integer>",
                                "periodSeconds": "<integer>",
                                "successThreshold": "<integer>",
                                "tcpSocket": {
                                    "host": "<string>",
                                    "port": "<string>"
                                },
                                "timeoutSeconds": "<integer>"
                            },
                            "stdin": "<boolean>",
                            "stdinOnce": "<boolean>",
                            "targetContainerName": "<string>",
                            "terminationMessagePath": "<string>",
                            "terminationMessagePolicy": "<string>",
                            "tty": "<boolean>",
                            "volumeDevices": [
                                {
                                    "devicePath": "<string>",
                                    "name": "<string>"
                                }
                            ],
                            "volumeMounts": [
                                {
                                    "mountPath": "<string>",
                                    "mountPropagation": "<string>",
                                    "name": "<string>",
                                    "readOnly": "<boolean>",
                                    "subPath": "<string>",
                                    "subPathExpr": "<string>"
                                }
                            ],
                            "workingDir": "<string>"
                        }
                    ],
                    "hostAliases": "<[]COMPONENT.HostAlias>",
                    "hostIPC": "<boolean>",
                    "hostNetwork": "<boolean>",
                    "hostPID": "<boolean>",
                    "hostname": "<string>",
                    "imagePullSecrets": "<[]COMPONENT.ImagePullSecret>",
                    "initContainers": "<[]COMPONENT.Container>",
                    "nodeName": "<string>",
                    "nodeSelector": "<map[string]string>",
                    "overhead": "<map[string]string>",
                    "preemptionPolicy": "<string>",
                    "priority": "<integer>",
                    "priorityClassName": "<string>",
                    "readinessGates": "<[]COMPONENT.ReadinessGate>",
                    "restartPolicy": "<string>",
                    "runtimeClassName": "<string>",
                    "schedulerName": "<string>",
                    "securityContext": "<COMPONENT.SecurityContext>",
                    "serviceAccount": "<string>",
                    "serviceAccountName": "<string>",
                    "shareProcessNamespace": "<boolean>",
                    "subdomain": "<string>",
                    "terminationGracePeriodSeconds": "<integer>",
                    "tolerations": "<[]COMPONENT.Tolerations>",
                    "topologySpreadConstraints": [
                        {
                            "labelSelector": {
                                "matchExpressions": [
                                    {
                                        "key": "<string>",
                                        "operator": "<string>",
                                        "values": "<[]string>"
                                    }
                                ],
                                "matchLabels": "<map[string]string>"
                            },
                            "maxSkew": "<integer>",
                            "topologyKey": "<string>",
                            "whenUnsatisfiable": "<string>"
                        }
                    ],
                    "volumes": "<[]COMPONENT.Volume>"
                }
            }
        }
    }