NetworkPolicyIngress
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

+--------------------------------------------------+---------------------+
| Key                                              | Type                |
+==================================================+=====================+
| from_ipBlock_cidr                                | <string>            |
+--------------------------------------------------+---------------------+
| from_ipBlock_except                              | <[]string>          |
+--------------------------------------------------+---------------------+
| from_namespaceSelector_matchExpressions_key      | <string>            |
+--------------------------------------------------+---------------------+
| from_namespaceSelector_matchExpressions_operator | <string>            |
+--------------------------------------------------+---------------------+
| from_namespaceSelector_matchExpressions_values   | <[]string>          |
+--------------------------------------------------+---------------------+
| from_namespaceSelector_matchLabels               | <map[string]string> |
+--------------------------------------------------+---------------------+
| from_podSelector_matchExpressions_key            | <string>            |
+--------------------------------------------------+---------------------+
| from_podSelector_matchExpressions_operator       | <string>            |
+--------------------------------------------------+---------------------+
| from_podSelector_matchExpressions_values         | <[]string>          |
+--------------------------------------------------+---------------------+
| from_podSelector_matchLabels                     | <map[string]string> |
+--------------------------------------------------+---------------------+
| ports_port                                       | <string>            |
+--------------------------------------------------+---------------------+
| ports_protocol                                   | <string>            |
+--------------------------------------------------+---------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "from": [
            {
                "ipBlock": {
                    "cidr": "<string>",
                    "except": "<[]string>"
                },
                "namespaceSelector": {
                    "matchExpressions": [
                        {
                            "key": "<string>",
                            "operator": "<string>",
                            "values": "<[]string>"
                        }
                    ],
                    "matchLabels": "<map[string]string>"
                },
                "podSelector": {
                    "matchExpressions": [
                        {
                            "key": "<string>",
                            "operator": "<string>",
                            "values": "<[]string>"
                        }
                    ],
                    "matchLabels": "<map[string]string>"
                }
            }
        ],
        "ports": [
            {
                "port": "<string>",
                "protocol": "<string>"
            }
        ]
    }