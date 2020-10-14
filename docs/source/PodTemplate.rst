PodTemplate
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

+-----------------------------------------------------------------------------------------+-------------------------------+
| Key                                                                                     | Type                          |
+=========================================================================================+===============================+
| apiVersion                                                                              | v1                            |
+-----------------------------------------------------------------------------------------+-------------------------------+
| kind                                                                                    | PodTemplate                   |
+-----------------------------------------------------------------------------------------+-------------------------------+
| metadata                                                                                | <COMPONENT.Metadata>          |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_metadata                                                                       | <COMPONENT.Metadata>          |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_activeDeadlineSeconds                                                     | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_affinity_nodeAffinity                                                     | <COMPONENT.NodeAffinity>      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_affinity_podAffinity                                                      | <COMPONENT.PodAffinity>       |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_affinity_podAntiAffinity                                                  | <COMPONENT.PodAntiAffinity>   |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_automountServiceAccountToken                                              | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_containers                                                                | <[]COMPONENT.Container>       |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_dnsConfig                                                                 | <COMPONENT.DNSConfig>         |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_dnsPolicy                                                                 | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_enableServiceLinks                                                        | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_args                                                  | <[]string>                    |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_command                                               | <[]string>                    |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_env_name                                              | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_env_value                                             | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_env_valueFrom_configMapKeyRef_key                     | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_env_valueFrom_configMapKeyRef_name                    | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_env_valueFrom_configMapKeyRef_optional                | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_env_valueFrom_fieldRef_apiVersion                     | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_env_valueFrom_fieldRef_fieldPath                      | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_env_valueFrom_resourceFieldRef_containerName          | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_env_valueFrom_resourceFieldRef_divisor                | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_env_valueFrom_resourceFieldRef_resource               | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_env_valueFrom_secretKeyRef_key                        | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_env_valueFrom_secretKeyRef_name                       | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_env_valueFrom_secretKeyRef_optional                   | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_envFrom_configMapRef_name                             | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_envFrom_configMapRef_optional                         | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_envFrom_prefix                                        | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_envFrom_secretRef_name                                | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_envFrom_secretRef_optional                            | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_image                                                 | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_imagePullPolicy                                       | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_postStart_exec_command                      | <[]string>                    |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_postStart_httpGet_host                      | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_postStart_httpGet_httpHeaders_name          | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_postStart_httpGet_httpHeaders_value         | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_postStart_httpGet_path                      | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_postStart_httpGet_port                      | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_postStart_httpGet_scheme                    | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_postStart_tcpSocket_host                    | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_postStart_tcpSocket_port                    | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_preStop_exec_command                        | <[]string>                    |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_preStop_httpGet_host                        | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_preStop_httpGet_httpHeaders_name            | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_preStop_httpGet_httpHeaders_value           | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_preStop_httpGet_path                        | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_preStop_httpGet_port                        | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_preStop_httpGet_scheme                      | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_preStop_tcpSocket_host                      | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_lifecycle_preStop_tcpSocket_port                      | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_livenessProbe_exec_command                            | <[]string>                    |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_livenessProbe_failureThreshold                        | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_livenessProbe_httpGet_host                            | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_livenessProbe_httpGet_httpHeaders_name                | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_livenessProbe_httpGet_httpHeaders_value               | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_livenessProbe_httpGet_path                            | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_livenessProbe_httpGet_port                            | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_livenessProbe_httpGet_scheme                          | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_livenessProbe_initialDelaySeconds                     | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_livenessProbe_periodSeconds                           | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_livenessProbe_successThreshold                        | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_livenessProbe_tcpSocket_host                          | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_livenessProbe_tcpSocket_port                          | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_livenessProbe_timeoutSeconds                          | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_name                                                  | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_ports_containerPort                                   | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_ports_hostIP                                          | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_ports_hostPort                                        | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_ports_name                                            | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_ports_protocol                                        | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_readinessProbe_exec_command                           | <[]string>                    |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_readinessProbe_failureThreshold                       | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_readinessProbe_httpGet_host                           | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_readinessProbe_httpGet_httpHeaders_name               | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_readinessProbe_httpGet_httpHeaders_value              | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_readinessProbe_httpGet_path                           | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_readinessProbe_httpGet_port                           | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_readinessProbe_httpGet_scheme                         | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_readinessProbe_initialDelaySeconds                    | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_readinessProbe_periodSeconds                          | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_readinessProbe_successThreshold                       | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_readinessProbe_tcpSocket_host                         | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_readinessProbe_tcpSocket_port                         | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_readinessProbe_timeoutSeconds                         | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_resources_limits                                      | <map[string]string>           |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_resources_requests                                    | <map[string]string>           |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_securityContext_allowPrivilegeEscalation              | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_securityContext_capabilities_add                      | <[]string>                    |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_securityContext_capabilities_drop                     | <[]string>                    |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_securityContext_privileged                            | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_securityContext_procMount                             | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_securityContext_readOnlyRootFilesystem                | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_securityContext_runAsGroup                            | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_securityContext_runAsNonRoot                          | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_securityContext_runAsUser                             | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_securityContext_seLinuxOptions_level                  | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_securityContext_seLinuxOptions_role                   | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_securityContext_seLinuxOptions_type                   | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_securityContext_seLinuxOptions_user                   | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_securityContext_windowsOptions_gmsaCredentialSpec     | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_securityContext_windowsOptions_gmsaCredentialSpecName | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_securityContext_windowsOptions_runAsUserName          | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_startupProbe_exec_command                             | <[]string>                    |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_startupProbe_failureThreshold                         | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_startupProbe_httpGet_host                             | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_startupProbe_httpGet_httpHeaders_name                 | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_startupProbe_httpGet_httpHeaders_value                | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_startupProbe_httpGet_path                             | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_startupProbe_httpGet_port                             | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_startupProbe_httpGet_scheme                           | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_startupProbe_initialDelaySeconds                      | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_startupProbe_periodSeconds                            | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_startupProbe_successThreshold                         | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_startupProbe_tcpSocket_host                           | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_startupProbe_tcpSocket_port                           | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_startupProbe_timeoutSeconds                           | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_stdin                                                 | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_stdinOnce                                             | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_targetContainerName                                   | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_terminationMessagePath                                | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_terminationMessagePolicy                              | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_tty                                                   | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_volumeDevices_devicePath                              | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_volumeDevices_name                                    | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_volumeMounts_mountPath                                | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_volumeMounts_mountPropagation                         | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_volumeMounts_name                                     | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_volumeMounts_readOnly                                 | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_volumeMounts_subPath                                  | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_volumeMounts_subPathExpr                              | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_ephemeralContainers_workingDir                                            | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_hostAliases                                                               | <[]COMPONENT.HostAlias>       |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_hostIPC                                                                   | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_hostNetwork                                                               | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_hostPID                                                                   | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_hostname                                                                  | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_imagePullSecrets                                                          | <[]COMPONENT.ImagePullSecret> |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_initContainers                                                            | <[]COMPONENT.Container>       |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_nodeName                                                                  | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_nodeSelector                                                              | <map[string]string>           |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_overhead                                                                  | <map[string]string>           |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_preemptionPolicy                                                          | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_priority                                                                  | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_priorityClassName                                                         | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_readinessGates                                                            | <[]COMPONENT.ReadinessGate>   |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_restartPolicy                                                             | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_runtimeClassName                                                          | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_schedulerName                                                             | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_securityContext                                                           | <COMPONENT.SecurityContext>   |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_serviceAccount                                                            | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_serviceAccountName                                                        | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_shareProcessNamespace                                                     | <boolean>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_subdomain                                                                 | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_terminationGracePeriodSeconds                                             | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_tolerations                                                               | <[]COMPONENT.Tolerations>     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_topologySpreadConstraints_labelSelector_matchExpressions_key              | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_topologySpreadConstraints_labelSelector_matchExpressions_operator         | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_topologySpreadConstraints_labelSelector_matchExpressions_values           | <[]string>                    |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_topologySpreadConstraints_labelSelector_matchLabels                       | <map[string]string>           |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_topologySpreadConstraints_maxSkew                                         | <integer>                     |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_topologySpreadConstraints_topologyKey                                     | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_topologySpreadConstraints_whenUnsatisfiable                               | <string>                      |
+-----------------------------------------------------------------------------------------+-------------------------------+
| template_spec_volumes                                                                   | <[]COMPONENT.Volume>          |
+-----------------------------------------------------------------------------------------+-------------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "apiVersion": "v1",
        "kind": "PodTemplate",
        "metadata": "<COMPONENT.Metadata>",
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