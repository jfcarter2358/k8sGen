Pod
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

+------------------------------------+-------------------------------+
| Key                                | Type                          |
+====================================+===============================+
| apiVersion                         | v1                            |
+------------------------------------+-------------------------------+
| kind                               | Pod                           |
+------------------------------------+-------------------------------+
| metadata                           | <COMPONENT.Metadata>          |
+------------------------------------+-------------------------------+
| spec_activeDeadlineSeconds         | <integer>                     |
+------------------------------------+-------------------------------+
| spec_affinity_nodeAffinity         | <COMPONENT.NodeAffinity>      |
+------------------------------------+-------------------------------+
| spec_affinity_podAffinity          | <COMPONENT.PodAffinity>       |
+------------------------------------+-------------------------------+
| spec_affinity_podAntiAffinity      | <COMPONENT.PodAntiAffinity>   |
+------------------------------------+-------------------------------+
| spec_automountServiceAccountToken  | <boolean>                     |
+------------------------------------+-------------------------------+
| spec_containers                    | <[]COMPONENT.Container>       |
+------------------------------------+-------------------------------+
| spec_dnsConfig                     | <COMPONENT.DNSConfig>         |
+------------------------------------+-------------------------------+
| spec_dnsPolicy                     | <string>                      |
+------------------------------------+-------------------------------+
| spec_enableServiceLinks            | <boolean>                     |
+------------------------------------+-------------------------------+
| spec_hostAliases                   | <[]COMPONENT.HostAlias>       |
+------------------------------------+-------------------------------+
| spec_hostIPC                       | <boolean>                     |
+------------------------------------+-------------------------------+
| spec_hostNetwork                   | <boolean>                     |
+------------------------------------+-------------------------------+
| spec_hostPID                       | <boolean>                     |
+------------------------------------+-------------------------------+
| spec_hostname                      | <string>                      |
+------------------------------------+-------------------------------+
| spec_imagePullSecrets              | <[]COMPONENT.ImagePullSecret> |
+------------------------------------+-------------------------------+
| spec_initContainers                | <[]COMPONENT.Container>       |
+------------------------------------+-------------------------------+
| spec_nodeName                      | <string>                      |
+------------------------------------+-------------------------------+
| spec_nodeSelector                  | <map[string]string>           |
+------------------------------------+-------------------------------+
| spec_preemptionPolicy              | <string>                      |
+------------------------------------+-------------------------------+
| spec_priority                      | <integer>                     |
+------------------------------------+-------------------------------+
| spec_priorityClassName             | <string>                      |
+------------------------------------+-------------------------------+
| spec_readinessGates                | <[]COMPONENT.ReadinessGate>   |
+------------------------------------+-------------------------------+
| spec_restartPolicy                 | <string>                      |
+------------------------------------+-------------------------------+
| spec_runtimeClassName              | <string>                      |
+------------------------------------+-------------------------------+
| spec_schedulerName                 | <string>                      |
+------------------------------------+-------------------------------+
| spec_securityContext               | <COMPONENT.SecurityContext>   |
+------------------------------------+-------------------------------+
| spec_serviceAccount                | <string>                      |
+------------------------------------+-------------------------------+
| spec_serviceAccountName            | <string>                      |
+------------------------------------+-------------------------------+
| spec_shareProcessNamespace         | <boolean>                     |
+------------------------------------+-------------------------------+
| spec_subdomain                     | <string>                      |
+------------------------------------+-------------------------------+
| spec_terminationGracePeriodSeconds | <integer>                     |
+------------------------------------+-------------------------------+
| spec_tolerations                   | <[]COMPONENT.Tolerations>     |
+------------------------------------+-------------------------------+
| spec_volumes                       | <[]COMPONENT.Volume>          |
+------------------------------------+-------------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "apiVersion": "v1",
        "kind": "Pod",
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
            "hostAliases": "<[]COMPONENT.HostAlias>",
            "hostIPC": "<boolean>",
            "hostNetwork": "<boolean>",
            "hostPID": "<boolean>",
            "hostname": "<string>",
            "imagePullSecrets": "<[]COMPONENT.ImagePullSecret>",
            "initContainers": "<[]COMPONENT.Container>",
            "nodeName": "<string>",
            "nodeSelector": "<map[string]string>",
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
            "volumes": "<[]COMPONENT.Volume>"
        }
    }