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

+---------------------------------------------+-------------------------------+
| Key                                         | Type                          |
+=============================================+===============================+
| apiVersion                                  | v1                            |
+---------------------------------------------+-------------------------------+
| kind                                        | PodTemplate                   |
+---------------------------------------------+-------------------------------+
| metadata                                    | <COMPONENT.Metadata>          |
+---------------------------------------------+-------------------------------+
| template_metadata                           | <COMPONENT.Metadata>          |
+---------------------------------------------+-------------------------------+
| template_spec_activeDeadlineSeconds         | <integer>                     |
+---------------------------------------------+-------------------------------+
| template_spec_affinity_nodeAffinity         | <COMPONENT.NodeAffinity>      |
+---------------------------------------------+-------------------------------+
| template_spec_affinity_podAffinity          | <COMPONENT.PodAffinity>       |
+---------------------------------------------+-------------------------------+
| template_spec_affinity_podAntiAffinity      | <COMPONENT.PodAntiAffinity>   |
+---------------------------------------------+-------------------------------+
| template_spec_automountServiceAccountToken  | <boolean>                     |
+---------------------------------------------+-------------------------------+
| template_spec_containers                    | <[]COMPONENT.Container>       |
+---------------------------------------------+-------------------------------+
| template_spec_dnsConfig                     | <COMPONENT.DNSConfig>         |
+---------------------------------------------+-------------------------------+
| template_spec_dnsPolicy                     | <string>                      |
+---------------------------------------------+-------------------------------+
| template_spec_enableServiceLinks            | <boolean>                     |
+---------------------------------------------+-------------------------------+
| template_spec_hostAliases                   | <[]COMPONENT.HostAlias>       |
+---------------------------------------------+-------------------------------+
| template_spec_hostIPC                       | <boolean>                     |
+---------------------------------------------+-------------------------------+
| template_spec_hostNetwork                   | <boolean>                     |
+---------------------------------------------+-------------------------------+
| template_spec_hostPID                       | <boolean>                     |
+---------------------------------------------+-------------------------------+
| template_spec_hostname                      | <string>                      |
+---------------------------------------------+-------------------------------+
| template_spec_imagePullSecrets              | <[]COMPONENT.ImagePullSecret> |
+---------------------------------------------+-------------------------------+
| template_spec_initContainers                | <[]COMPONENT.Container>       |
+---------------------------------------------+-------------------------------+
| template_spec_nodeName                      | <string>                      |
+---------------------------------------------+-------------------------------+
| template_spec_nodeSelector                  | <map[string]string>           |
+---------------------------------------------+-------------------------------+
| template_spec_preemptionPolicy              | <string>                      |
+---------------------------------------------+-------------------------------+
| template_spec_priority                      | <integer>                     |
+---------------------------------------------+-------------------------------+
| template_spec_priorityClassName             | <string>                      |
+---------------------------------------------+-------------------------------+
| template_spec_readinessGates                | <[]COMPONENT.ReadinessGate>   |
+---------------------------------------------+-------------------------------+
| template_spec_restartPolicy                 | <string>                      |
+---------------------------------------------+-------------------------------+
| template_spec_runtimeClassName              | <string>                      |
+---------------------------------------------+-------------------------------+
| template_spec_schedulerName                 | <string>                      |
+---------------------------------------------+-------------------------------+
| template_spec_securityContext               | <COMPONENT.SecurityContext>   |
+---------------------------------------------+-------------------------------+
| template_spec_serviceAccount                | <string>                      |
+---------------------------------------------+-------------------------------+
| template_spec_serviceAccountName            | <string>                      |
+---------------------------------------------+-------------------------------+
| template_spec_shareProcessNamespace         | <boolean>                     |
+---------------------------------------------+-------------------------------+
| template_spec_subdomain                     | <string>                      |
+---------------------------------------------+-------------------------------+
| template_spec_terminationGracePeriodSeconds | <integer>                     |
+---------------------------------------------+-------------------------------+
| template_spec_tolerations                   | <[]COMPONENT.Tolerations>     |
+---------------------------------------------+-------------------------------+
| template_spec_volumes                       | <[]COMPONENT.Volume>          |
+---------------------------------------------+-------------------------------+


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
    }