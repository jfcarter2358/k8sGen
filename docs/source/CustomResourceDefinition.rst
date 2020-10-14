CustomResourceDefinition
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

+--------------------------------------------------------+-----------------------------------------+
| Key                                                    | Type                                    |
+========================================================+=========================================+
| apiVersion                                             | apiextensions.k8s.io/v1                 |
+--------------------------------------------------------+-----------------------------------------+
| kind                                                   | CustomResourceDefinition                |
+--------------------------------------------------------+-----------------------------------------+
| metadata                                               | <COMPONENT.Metadata>                    |
+--------------------------------------------------------+-----------------------------------------+
| spec_conversion_strategy                               | <string>                                |
+--------------------------------------------------------+-----------------------------------------+
| spec_conversion_webhook_clientConfig_caBundle          | <string>                                |
+--------------------------------------------------------+-----------------------------------------+
| spec_conversion_webhook_clientConfig_service_name      | <string>                                |
+--------------------------------------------------------+-----------------------------------------+
| spec_conversion_webhook_clientConfig_service_namespace | <string>                                |
+--------------------------------------------------------+-----------------------------------------+
| spec_conversion_webhook_clientConfig_service_path      | <string>                                |
+--------------------------------------------------------+-----------------------------------------+
| spec_conversion_webhook_clientConfig_service_port      | <integer>                               |
+--------------------------------------------------------+-----------------------------------------+
| spec_conversion_webhook_clientConfig_url               | <string>                                |
+--------------------------------------------------------+-----------------------------------------+
| spec_conversion_webhook_conversionReviewVersions       | <[]string>                              |
+--------------------------------------------------------+-----------------------------------------+
| spec_group                                             | <string>                                |
+--------------------------------------------------------+-----------------------------------------+
| spec_names_categories                                  | <[]string>                              |
+--------------------------------------------------------+-----------------------------------------+
| spec_names_kind                                        | <string>                                |
+--------------------------------------------------------+-----------------------------------------+
| spec_names_listKind                                    | <string>                                |
+--------------------------------------------------------+-----------------------------------------+
| spec_names_plural                                      | <string>                                |
+--------------------------------------------------------+-----------------------------------------+
| spec_names_shortNames                                  | <[]string>                              |
+--------------------------------------------------------+-----------------------------------------+
| spec_names_singular                                    | <string>                                |
+--------------------------------------------------------+-----------------------------------------+
| spec_preserveUnknownFields                             | <boolean>                               |
+--------------------------------------------------------+-----------------------------------------+
| spec_scope                                             | <string>                                |
+--------------------------------------------------------+-----------------------------------------+
| spec_versions                                          | <[]COMPONENT.ResourceDefinitionVersion> |
+--------------------------------------------------------+-----------------------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "apiVersion": "apiextensions.k8s.io/v1",
        "kind": "CustomResourceDefinition",
        "metadata": "<COMPONENT.Metadata>",
        "spec": {
            "conversion": {
                "strategy": "<string>",
                "webhook": {
                    "clientConfig": {
                        "caBundle": "<string>",
                        "service": {
                            "name": "<string>",
                            "namespace": "<string>",
                            "path": "<string>",
                            "port": "<integer>"
                        },
                        "url": "<string>"
                    },
                    "conversionReviewVersions": "<[]string>"
                }
            },
            "group": "<string>",
            "names": {
                "categories": "<[]string>",
                "kind": "<string>",
                "listKind": "<string>",
                "plural": "<string>",
                "shortNames": "<[]string>",
                "singular": "<string>"
            },
            "preserveUnknownFields": "<boolean>",
            "scope": "<string>",
            "versions": "<[]COMPONENT.ResourceDefinitionVersion>"
        }
    }