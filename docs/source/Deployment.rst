Deployment
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

+--------------------------------------------+---------------------------+
| Key                                        | Type                      |
+============================================+===========================+
| apiVersion                                 | apps/v1                   |
+--------------------------------------------+---------------------------+
| kind                                       | Deployment                |
+--------------------------------------------+---------------------------+
| metadata                                   | <COMPONENT.Metadata>      |
+--------------------------------------------+---------------------------+
| spec_minReadySeconds                       | <integer>                 |
+--------------------------------------------+---------------------------+
| spec_paused                                | <boolean>                 |
+--------------------------------------------+---------------------------+
| spec_progressDeadlineSeconds               | <integer>                 |
+--------------------------------------------+---------------------------+
| spec_replicas                              | <integer>                 |
+--------------------------------------------+---------------------------+
| spec_revisionHistoryLimit                  | <integer>                 |
+--------------------------------------------+---------------------------+
| spec_selector                              | <COMPONENT.Selector>      |
+--------------------------------------------+---------------------------+
| spec_strategy_rollingUpdate_maxSurge       | <string>                  |
+--------------------------------------------+---------------------------+
| spec_strategy_rollingUpdate_maxUnavailable | <string>                  |
+--------------------------------------------+---------------------------+
| spec_strategy_type                         | <string>                  |
+--------------------------------------------+---------------------------+
| spec_template_metadata                     | <COMPONENT.Metadata>      |
+--------------------------------------------+---------------------------+
| spec_template_spec                         | <COMPONENT.ContainerSpec> |
+--------------------------------------------+---------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": "<COMPONENT.Metadata>",
        "spec": {
            "minReadySeconds": "<integer>",
            "paused": "<boolean>",
            "progressDeadlineSeconds": "<integer>",
            "replicas": "<integer>",
            "revisionHistoryLimit": "<integer>",
            "selector": "<COMPONENT.Selector>",
            "strategy": {
                "rollingUpdate": {
                    "maxSurge": "<string>",
                    "maxUnavailable": "<string>"
                },
                "type": "<string>"
            },
            "template": {
                "metadata": "<COMPONENT.Metadata>",
                "spec": "<COMPONENT.ContainerSpec>"
            }
        }
    }