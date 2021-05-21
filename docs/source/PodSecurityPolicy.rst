PodSecurityPolicy
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

+--------------------------------------------+---------------------------------+
| Key                                        | Type                            |
+============================================+=================================+
| apiVersion                                 | policy/v1beta1                  |
+--------------------------------------------+---------------------------------+
| kind                                       | PodSecurityPolicy               |
+--------------------------------------------+---------------------------------+
| metadata                                   | <COMPONENT.Metadata>            |
+--------------------------------------------+---------------------------------+
| spec_allowPrivilegeEscalation              | <boolean>                       |
+--------------------------------------------+---------------------------------+
| spec_allowedCSIDrivers                     | <[]COMPONENT.AllowedCSIDriver>  |
+--------------------------------------------+---------------------------------+
| spec_allowedCapabilities                   | <[]string>                      |
+--------------------------------------------+---------------------------------+
| spec_allowedFlexVolumes                    | <[]COMPONENT.AllowedFlexVolume> |
+--------------------------------------------+---------------------------------+
| spec_allowedHostPaths                      | <[]COMPONENT.AllowedHostPath>   |
+--------------------------------------------+---------------------------------+
| spec_allowedProcMountTypes                 | <[]string>                      |
+--------------------------------------------+---------------------------------+
| spec_allowedUnsafeSysctls                  | <[]string>                      |
+--------------------------------------------+---------------------------------+
| spec_defaultAddCapabilities                | <[]string>                      |
+--------------------------------------------+---------------------------------+
| spec_defaultAllowPrivilegeEscalation       | <boolean>                       |
+--------------------------------------------+---------------------------------+
| spec_forbiddenSysctls                      | <[]string>                      |
+--------------------------------------------+---------------------------------+
| spec_fsGroup                               | <integer>                       |
+--------------------------------------------+---------------------------------+
| spec_hostIPC                               | <boolean>                       |
+--------------------------------------------+---------------------------------+
| spec_hostNetwork                           | <boolean>                       |
+--------------------------------------------+---------------------------------+
| spec_hostPID                               | <boolean>                       |
+--------------------------------------------+---------------------------------+
| spec_hostPorts                             | <[]COMPONENT.Range>             |
+--------------------------------------------+---------------------------------+
| spec_privileged                            | <boolean>                       |
+--------------------------------------------+---------------------------------+
| spec_readOnlyRootFilesystem                | <boolean>                       |
+--------------------------------------------+---------------------------------+
| spec_requiredDropCapabilities              | <[]string>                      |
+--------------------------------------------+---------------------------------+
| spec_runAsGroup                            | <integer>                       |
+--------------------------------------------+---------------------------------+
| spec_runAsUser                             | <integer>                       |
+--------------------------------------------+---------------------------------+
| spec_runtimeClass_allowedRuntimeClassNames | <[]string>                      |
+--------------------------------------------+---------------------------------+
| spec_runtimeClass_defaultRuntimeClassName  | <string>                        |
+--------------------------------------------+---------------------------------+
| spec_seLinux_rule                          | <string>                        |
+--------------------------------------------+---------------------------------+
| spec_seLinux_seLinuxOptions_level          | <string>                        |
+--------------------------------------------+---------------------------------+
| spec_seLinux_seLinuxOptions_role           | <string>                        |
+--------------------------------------------+---------------------------------+
| spec_seLinux_seLinuxOptions_type           | <string>                        |
+--------------------------------------------+---------------------------------+
| spec_seLinux_seLinuxOptions_user           | <string>                        |
+--------------------------------------------+---------------------------------+
| spec_supplementalGroups                    | <COMPONENT.UserGroup>           |
+--------------------------------------------+---------------------------------+
| spec_volumes                               | <[]COMPONENT.Volume>            |
+--------------------------------------------+---------------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "apiVersion": "policy/v1beta1",
        "kind": "PodSecurityPolicy",
        "metadata": "<COMPONENT.Metadata>",
        "spec": {
            "allowPrivilegeEscalation": "<boolean>",
            "allowedCSIDrivers": "<[]COMPONENT.AllowedCSIDriver>",
            "allowedCapabilities": "<[]string>",
            "allowedFlexVolumes": "<[]COMPONENT.AllowedFlexVolume>",
            "allowedHostPaths": "<[]COMPONENT.AllowedHostPath>",
            "allowedProcMountTypes": "<[]string>",
            "allowedUnsafeSysctls": "<[]string>",
            "defaultAddCapabilities": "<[]string>",
            "defaultAllowPrivilegeEscalation": "<boolean>",
            "forbiddenSysctls": "<[]string>",
            "fsGroup": "<integer>",
            "hostIPC": "<boolean>",
            "hostNetwork": "<boolean>",
            "hostPID": "<boolean>",
            "hostPorts": "<[]COMPONENT.Range>",
            "privileged": "<boolean>",
            "readOnlyRootFilesystem": "<boolean>",
            "requiredDropCapabilities": "<[]string>",
            "runAsGroup": "<integer>",
            "runAsUser": "<integer>",
            "runtimeClass": {
                "allowedRuntimeClassNames": "<[]string>",
                "defaultRuntimeClassName": "<string>"
            },
            "seLinux": {
                "rule": "<string>",
                "seLinuxOptions": {
                    "level": "<string>",
                    "role": "<string>",
                    "type": "<string>",
                    "user": "<string>"
                }
            },
            "supplementalGroups": "<COMPONENT.UserGroup>",
            "volumes": "<[]COMPONENT.Volume>"
        }
    }