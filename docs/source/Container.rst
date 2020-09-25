Container
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

+--------------------------+-----------------------------------------+
| Key                      | Type                                    |
+==========================+=========================================+
| args                     | <[]string>                              |
+--------------------------+-----------------------------------------+
| command                  | <[]string>                              |
+--------------------------+-----------------------------------------+
| env                      | <[]COMPONENT.EnvironmentVariable>       |
+--------------------------+-----------------------------------------+
| envFrom                  | <[]COMPONENT.EnvironmentVariableSource> |
+--------------------------+-----------------------------------------+
| image                    | <string>                                |
+--------------------------+-----------------------------------------+
| imagePullPolicy          | <string>                                |
+--------------------------+-----------------------------------------+
| lifecycle_postStart      | <[]COMPONENT.LifecycleDefinition>       |
+--------------------------+-----------------------------------------+
| lifecycle_preStop        | <[]COMPONENT.LifecycleDefinition>       |
+--------------------------+-----------------------------------------+
| livenessProbe            | <COMPONENT.Probe>                       |
+--------------------------+-----------------------------------------+
| name                     | <string>                                |
+--------------------------+-----------------------------------------+
| ports                    | <[]COMPONENT.Port>                      |
+--------------------------+-----------------------------------------+
| readinessProbe           | <COMPONENT.Probe>                       |
+--------------------------+-----------------------------------------+
| resources_limits         | <map[string]string>                     |
+--------------------------+-----------------------------------------+
| resources_requests       | <map[string]string>                     |
+--------------------------+-----------------------------------------+
| securityContext          | <COMPONENT.SecurityContext>             |
+--------------------------+-----------------------------------------+
| stdin                    | <boolean>                               |
+--------------------------+-----------------------------------------+
| stdinOnce                | <boolean>                               |
+--------------------------+-----------------------------------------+
| terminationMessagePath   | <string>                                |
+--------------------------+-----------------------------------------+
| terminationMessagePolicy | <string>                                |
+--------------------------+-----------------------------------------+
| tty                      | <boolean>                               |
+--------------------------+-----------------------------------------+
| volumeDevices            | <[]COMPONENT.VolumeDevice>              |
+--------------------------+-----------------------------------------+
| volumeMounts             | <[]COMPONENT.VolumeMount>               |
+--------------------------+-----------------------------------------+
| workingDir               | <string>                                |
+--------------------------+-----------------------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "args": "<[]string>",
        "command": "<[]string>",
        "env": "<[]COMPONENT.EnvironmentVariable>",
        "envFrom": "<[]COMPONENT.EnvironmentVariableSource>",
        "image": "<string>",
        "imagePullPolicy": "<string>",
        "lifecycle": {
            "postStart": "<[]COMPONENT.LifecycleDefinition>",
            "preStop": "<[]COMPONENT.LifecycleDefinition>"
        },
        "livenessProbe": "<COMPONENT.Probe>",
        "name": "<string>",
        "ports": "<[]COMPONENT.Port>",
        "readinessProbe": "<COMPONENT.Probe>",
        "resources": {
            "limits": "<map[string]string>",
            "requests": "<map[string]string>"
        },
        "securityContext": "<COMPONENT.SecurityContext>",
        "stdin": "<boolean>",
        "stdinOnce": "<boolean>",
        "terminationMessagePath": "<string>",
        "terminationMessagePolicy": "<string>",
        "tty": "<boolean>",
        "volumeDevices": "<[]COMPONENT.VolumeDevice>",
        "volumeMounts": "<[]COMPONENT.VolumeMount>",
        "workingDir": "<string>"
    }