Ingress
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

+--------------------------------+---------------------------+
| Key                            | Type                      |
+================================+===========================+
| apiVersion                     | extensions/v1beta1        |
+--------------------------------+---------------------------+
| kind                           | Ingress                   |
+--------------------------------+---------------------------+
| metadata                       | <COMPONENT.Metadata>      |
+--------------------------------+---------------------------+
| spec_backend_resource_apiGroup | <string>                  |
+--------------------------------+---------------------------+
| spec_backend_resource_kind     | <string>                  |
+--------------------------------+---------------------------+
| spec_backend_resource_name     | <string>                  |
+--------------------------------+---------------------------+
| spec_backend_serviceName       | <string>                  |
+--------------------------------+---------------------------+
| spec_backend_servicePort       | <string>                  |
+--------------------------------+---------------------------+
| spec_ingressClassName          | <string>                  |
+--------------------------------+---------------------------+
| spec_rules                     | <[]COMPONENT.IngressRule> |
+--------------------------------+---------------------------+
| spec_tls                       | <[]COMPONENT.IngressTLS>  |
+--------------------------------+---------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "apiVersion": "extensions/v1beta1",
        "kind": "Ingress",
        "metadata": "<COMPONENT.Metadata>",
        "spec": {
            "backend": {
                "resource": {
                    "apiGroup": "<string>",
                    "kind": "<string>",
                    "name": "<string>"
                },
                "serviceName": "<string>",
                "servicePort": "<string>"
            },
            "ingressClassName": "<string>",
            "rules": "<[]COMPONENT.IngressRule>",
            "tls": "<[]COMPONENT.IngressTLS>"
        }
    }