EnvironmentVariable
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

+------------------------------------------+-----------+
| Key                                      | Type      |
+==========================================+===========+
| name                                     | <string>  |
+------------------------------------------+-----------+
| value                                    | <string>  |
+------------------------------------------+-----------+
| valueFrom_configMapKeyRef_key            | <string>  |
+------------------------------------------+-----------+
| valueFrom_configMapKeyRef_name           | <string>  |
+------------------------------------------+-----------+
| valueFrom_configMapKeyRef_optional       | <boolean> |
+------------------------------------------+-----------+
| valueFrom_fieldRef_apiVersion            | <string>  |
+------------------------------------------+-----------+
| valueFrom_fieldRef_fieldPath             | <string>  |
+------------------------------------------+-----------+
| valueFrom_resourceFieldRef_containerName | <string>  |
+------------------------------------------+-----------+
| valueFrom_resourceFieldRef_divisor       | <string>  |
+------------------------------------------+-----------+
| valueFrom_resourceFieldRef_resource      | <string>  |
+------------------------------------------+-----------+
| valueFrom_secretKeyRef_key               | <string>  |
+------------------------------------------+-----------+
| valueFrom_secretKeyRef_name              | <string>  |
+------------------------------------------+-----------+
| valueFrom_secretKeyRef_optional          | <boolean> |
+------------------------------------------+-----------+


JSON fields
-----------

.. code-block:: JSON

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