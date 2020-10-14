ResourceDefinitionVersion
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

+-------------------------------------------------------------+-----------------------------+
| Key                                                         | Type                        |
+=============================================================+=============================+
| additionalPrinterColumns                                    | <[]COMPONENT.PrinterColumn> |
+-------------------------------------------------------------+-----------------------------+
| name                                                        | <string>                    |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_$ref                                 | <string>                    |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_$schema                              | <string>                    |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_additionalItems                      | <>                          |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_additionalProperties                 | <>                          |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_default                              | <>                          |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_dependencies                         | <map[string]>               |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_description                          | <string>                    |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_enum                                 | <[]>                        |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_example                              | <>                          |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_exclusiveMaximum                     | <boolean>                   |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_exclusiveMinimum                     | <boolean>                   |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_externalDocs_description             | <string>                    |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_externalDocs_url                     | <string>                    |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_format                               | <string>                    |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_id                                   | <string>                    |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_items                                | <>                          |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_maxItems                             | <integer>                   |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_maxLength                            | <integer>                   |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_maxProperties                        | <integer>                   |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_maximum                              | <number>                    |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_minItems                             | <integer>                   |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_minLength                            | <integer>                   |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_minProperties                        | <integer>                   |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_minimum                              | <number>                    |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_multipleOf                           | <number>                    |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_nullable                             | <boolean>                   |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_pattern                              | <string>                    |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_required                             | <[]string>                  |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_title                                | <string>                    |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_type                                 | <string>                    |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_uniqueItems                          | <boolean>                   |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_x-kubernetes-embedded-resource       | <boolean>                   |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_x-kubernetes-int-or-string           | <boolean>                   |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_x-kubernetes-list-map-keys           | <[]string>                  |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_x-kubernetes-list-type               | <string>                    |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_x-kubernetes-map-type                | <string>                    |
+-------------------------------------------------------------+-----------------------------+
| schema_openAPIV3Schema_x-kubernetes-preserve-unknown-fields | <boolean>                   |
+-------------------------------------------------------------+-----------------------------+
| served                                                      | <boolean>                   |
+-------------------------------------------------------------+-----------------------------+
| storage                                                     | <boolean>                   |
+-------------------------------------------------------------+-----------------------------+
| subresources_scale_labelSelectorPath                        | <string>                    |
+-------------------------------------------------------------+-----------------------------+
| subresources_scale_specReplicasPath                         | <string>                    |
+-------------------------------------------------------------+-----------------------------+
| subresources_scale_statusReplicasPath                       | <string>                    |
+-------------------------------------------------------------+-----------------------------+
| subresources_status                                         | <map[string]>               |
+-------------------------------------------------------------+-----------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "additionalPrinterColumns": "<[]COMPONENT.PrinterColumn>",
        "name": "<string>",
        "schema": {
            "openAPIV3Schema": {
                "$ref": "<string>",
                "$schema": "<string>",
                "additionalItems": "<>",
                "additionalProperties": "<>",
                "allOf": null,
                "anyOf": null,
                "default": "<>",
                "definitions": null,
                "dependencies": "<map[string]>",
                "description": "<string>",
                "enum": "<[]>",
                "example": "<>",
                "exclusiveMaximum": "<boolean>",
                "exclusiveMinimum": "<boolean>",
                "externalDocs": {
                    "description": "<string>",
                    "url": "<string>"
                },
                "format": "<string>",
                "id": "<string>",
                "items": "<>",
                "maxItems": "<integer>",
                "maxLength": "<integer>",
                "maxProperties": "<integer>",
                "maximum": "<number>",
                "minItems": "<integer>",
                "minLength": "<integer>",
                "minProperties": "<integer>",
                "minimum": "<number>",
                "multipleOf": "<number>",
                "not": null,
                "nullable": "<boolean>",
                "oneOf": null,
                "pattern": "<string>",
                "patternProperties": null,
                "properties": null,
                "required": "<[]string>",
                "title": "<string>",
                "type": "<string>",
                "uniqueItems": "<boolean>",
                "x-kubernetes-embedded-resource": "<boolean>",
                "x-kubernetes-int-or-string": "<boolean>",
                "x-kubernetes-list-map-keys": "<[]string>",
                "x-kubernetes-list-type": "<string>",
                "x-kubernetes-map-type": "<string>",
                "x-kubernetes-preserve-unknown-fields": "<boolean>"
            }
        },
        "served": "<boolean>",
        "storage": "<boolean>",
        "subresources": {
            "scale": {
                "labelSelectorPath": "<string>",
                "specReplicasPath": "<string>",
                "statusReplicasPath": "<string>"
            },
            "status": "<map[string]>"
        }
    }