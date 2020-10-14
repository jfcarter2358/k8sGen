ContainerSpec
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

+---------------------------------------------------------------------------+-------------------------------+
| Key                                                                       | Type                          |
+===========================================================================+===============================+
| activeDeadlineSeconds                                                     | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| affinity_nodeAffinity                                                     | <COMPONENT.NodeAffinity>      |
+---------------------------------------------------------------------------+-------------------------------+
| affinity_podAffinity                                                      | <COMPONENT.PodAffinity>       |
+---------------------------------------------------------------------------+-------------------------------+
| affinity_podAntiAffinity                                                  | <COMPONENT.PodAntiAffinity>   |
+---------------------------------------------------------------------------+-------------------------------+
| automountServiceAccountToken                                              | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| containers                                                                | <[]COMPONENT.Container>       |
+---------------------------------------------------------------------------+-------------------------------+
| dnsConfig                                                                 | <COMPONENT.DNSConfig>         |
+---------------------------------------------------------------------------+-------------------------------+
| dnsPolicy                                                                 | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| enableServiceLinks                                                        | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_args                                                  | <[]string>                    |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_command                                               | <[]string>                    |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_env_name                                              | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_env_value                                             | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_env_valueFrom_configMapKeyRef_key                     | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_env_valueFrom_configMapKeyRef_name                    | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_env_valueFrom_configMapKeyRef_optional                | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_env_valueFrom_fieldRef_apiVersion                     | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_env_valueFrom_fieldRef_fieldPath                      | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_env_valueFrom_resourceFieldRef_containerName          | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_env_valueFrom_resourceFieldRef_divisor                | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_env_valueFrom_resourceFieldRef_resource               | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_env_valueFrom_secretKeyRef_key                        | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_env_valueFrom_secretKeyRef_name                       | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_env_valueFrom_secretKeyRef_optional                   | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_envFrom_configMapRef_name                             | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_envFrom_configMapRef_optional                         | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_envFrom_prefix                                        | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_envFrom_secretRef_name                                | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_envFrom_secretRef_optional                            | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_image                                                 | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_imagePullPolicy                                       | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_postStart_exec_command                      | <[]string>                    |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_postStart_httpGet_host                      | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_postStart_httpGet_httpHeaders_name          | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_postStart_httpGet_httpHeaders_value         | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_postStart_httpGet_path                      | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_postStart_httpGet_port                      | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_postStart_httpGet_scheme                    | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_postStart_tcpSocket_host                    | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_postStart_tcpSocket_port                    | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_preStop_exec_command                        | <[]string>                    |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_preStop_httpGet_host                        | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_preStop_httpGet_httpHeaders_name            | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_preStop_httpGet_httpHeaders_value           | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_preStop_httpGet_path                        | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_preStop_httpGet_port                        | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_preStop_httpGet_scheme                      | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_preStop_tcpSocket_host                      | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_lifecycle_preStop_tcpSocket_port                      | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_livenessProbe_exec_command                            | <[]string>                    |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_livenessProbe_failureThreshold                        | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_livenessProbe_httpGet_host                            | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_livenessProbe_httpGet_httpHeaders_name                | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_livenessProbe_httpGet_httpHeaders_value               | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_livenessProbe_httpGet_path                            | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_livenessProbe_httpGet_port                            | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_livenessProbe_httpGet_scheme                          | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_livenessProbe_initialDelaySeconds                     | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_livenessProbe_periodSeconds                           | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_livenessProbe_successThreshold                        | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_livenessProbe_tcpSocket_host                          | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_livenessProbe_tcpSocket_port                          | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_livenessProbe_timeoutSeconds                          | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_name                                                  | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_ports_containerPort                                   | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_ports_hostIP                                          | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_ports_hostPort                                        | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_ports_name                                            | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_ports_protocol                                        | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_readinessProbe_exec_command                           | <[]string>                    |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_readinessProbe_failureThreshold                       | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_readinessProbe_httpGet_host                           | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_readinessProbe_httpGet_httpHeaders_name               | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_readinessProbe_httpGet_httpHeaders_value              | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_readinessProbe_httpGet_path                           | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_readinessProbe_httpGet_port                           | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_readinessProbe_httpGet_scheme                         | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_readinessProbe_initialDelaySeconds                    | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_readinessProbe_periodSeconds                          | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_readinessProbe_successThreshold                       | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_readinessProbe_tcpSocket_host                         | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_readinessProbe_tcpSocket_port                         | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_readinessProbe_timeoutSeconds                         | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_resources_limits                                      | <map[string]string>           |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_resources_requests                                    | <map[string]string>           |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_securityContext_allowPrivilegeEscalation              | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_securityContext_capabilities_add                      | <[]string>                    |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_securityContext_capabilities_drop                     | <[]string>                    |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_securityContext_privileged                            | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_securityContext_procMount                             | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_securityContext_readOnlyRootFilesystem                | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_securityContext_runAsGroup                            | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_securityContext_runAsNonRoot                          | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_securityContext_runAsUser                             | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_securityContext_seLinuxOptions_level                  | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_securityContext_seLinuxOptions_role                   | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_securityContext_seLinuxOptions_type                   | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_securityContext_seLinuxOptions_user                   | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_securityContext_windowsOptions_gmsaCredentialSpec     | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_securityContext_windowsOptions_gmsaCredentialSpecName | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_securityContext_windowsOptions_runAsUserName          | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_startupProbe_exec_command                             | <[]string>                    |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_startupProbe_failureThreshold                         | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_startupProbe_httpGet_host                             | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_startupProbe_httpGet_httpHeaders_name                 | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_startupProbe_httpGet_httpHeaders_value                | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_startupProbe_httpGet_path                             | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_startupProbe_httpGet_port                             | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_startupProbe_httpGet_scheme                           | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_startupProbe_initialDelaySeconds                      | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_startupProbe_periodSeconds                            | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_startupProbe_successThreshold                         | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_startupProbe_tcpSocket_host                           | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_startupProbe_tcpSocket_port                           | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_startupProbe_timeoutSeconds                           | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_stdin                                                 | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_stdinOnce                                             | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_targetContainerName                                   | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_terminationMessagePath                                | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_terminationMessagePolicy                              | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_tty                                                   | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_volumeDevices_devicePath                              | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_volumeDevices_name                                    | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_volumeMounts_mountPath                                | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_volumeMounts_mountPropagation                         | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_volumeMounts_name                                     | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_volumeMounts_readOnly                                 | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_volumeMounts_subPath                                  | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_volumeMounts_subPathExpr                              | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| ephemeralContainers_workingDir                                            | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| hostAliases                                                               | <[]COMPONENT.HostAlias>       |
+---------------------------------------------------------------------------+-------------------------------+
| hostIPC                                                                   | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| hostNetwork                                                               | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| hostPID                                                                   | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| hostname                                                                  | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| imagePullSecrets                                                          | <[]COMPONENT.ImagePullSecret> |
+---------------------------------------------------------------------------+-------------------------------+
| initContainers                                                            | <[]COMPONENT.Container>       |
+---------------------------------------------------------------------------+-------------------------------+
| nodeName                                                                  | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| nodeSelector                                                              | <map[string]string>           |
+---------------------------------------------------------------------------+-------------------------------+
| overhead                                                                  | <map[string]string>           |
+---------------------------------------------------------------------------+-------------------------------+
| preemptionPolicy                                                          | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| priority                                                                  | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| priorityClassName                                                         | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| readinessGates                                                            | <[]COMPONENT.ReadinessGate>   |
+---------------------------------------------------------------------------+-------------------------------+
| restartPolicy                                                             | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| runtimeClassName                                                          | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| schedulerName                                                             | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| securityContext                                                           | <COMPONENT.SecurityContext>   |
+---------------------------------------------------------------------------+-------------------------------+
| serviceAccount                                                            | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| serviceAccountName                                                        | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| shareProcessNamespace                                                     | <boolean>                     |
+---------------------------------------------------------------------------+-------------------------------+
| subdomain                                                                 | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| terminationGracePeriodSeconds                                             | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| tolerations                                                               | <[]COMPONENT.Tolerations>     |
+---------------------------------------------------------------------------+-------------------------------+
| topologySpreadConstraints_labelSelector_matchExpressions_key              | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| topologySpreadConstraints_labelSelector_matchExpressions_operator         | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| topologySpreadConstraints_labelSelector_matchExpressions_values           | <[]string>                    |
+---------------------------------------------------------------------------+-------------------------------+
| topologySpreadConstraints_labelSelector_matchLabels                       | <map[string]string>           |
+---------------------------------------------------------------------------+-------------------------------+
| topologySpreadConstraints_maxSkew                                         | <integer>                     |
+---------------------------------------------------------------------------+-------------------------------+
| topologySpreadConstraints_topologyKey                                     | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| topologySpreadConstraints_whenUnsatisfiable                               | <string>                      |
+---------------------------------------------------------------------------+-------------------------------+
| volumes                                                                   | <[]COMPONENT.Volume>          |
+---------------------------------------------------------------------------+-------------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
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