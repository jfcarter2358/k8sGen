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

+----------------------------------------------------------------------+-----------------------------------------+
| Key                                                                  | Type                                    |
+======================================================================+=========================================+
| apiVersion                                                           | apiextensions.k8s.io/v1beta1            |
+----------------------------------------------------------------------+-----------------------------------------+
| kind                                                                 | CustomResourceDefinition                |
+----------------------------------------------------------------------+-----------------------------------------+
| metadata                                                             | <COMPONENT.Metadata>                    |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_additionalPrinterColumns                                        | <[]COMPONENT.PrinterColumn>             |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_conversion_conversionReviewVersions                             | <[]string>                              |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_conversion_strategy                                             | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_conversion_webhookClientConfig                                  | <COMPONENT.ClientConfig>                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_group                                                           | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_names_categories                                                | <[]string>                              |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_names_kind                                                      | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_names_listKind                                                  | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_names_plural                                                    | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_names_shortNames                                                | <[]string>                              |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_names_singular                                                  | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_preserveUnknownFields                                           | <boolean>                               |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_scope                                                           | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_subresources_scale_labelSelectorPath                            | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_subresources_scale_specReplicasPath                             | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_subresources_scale_statusReplicasPath                           | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_subresources_status                                             | <map[string]>                           |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_$ref                                 | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_$schema                              | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_additionalItems                      | <>                                      |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_additionalProperties                 | <>                                      |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_default                              | <>                                      |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_dependencies                         | <map[string]>                           |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_description                          | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_enum                                 | <[]>                                    |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_example                              | <>                                      |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_exclusiveMaximum                     | <boolean>                               |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_exclusiveMinimum                     | <boolean>                               |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_externalDocs_description             | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_externalDocs_url                     | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_format                               | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_id                                   | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_items                                | <>                                      |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_maxItems                             | <integer>                               |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_maxLength                            | <integer>                               |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_maxProperties                        | <integer>                               |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_maximum                              | <number>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_minItems                             | <integer>                               |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_minLength                            | <integer>                               |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_minProperties                        | <integer>                               |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_minimum                              | <number>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_multipleOf                           | <number>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_nullable                             | <boolean>                               |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_pattern                              | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_required                             | <[]string>                              |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_title                                | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_type                                 | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_uniqueItems                          | <boolean>                               |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_x-kubernetes-embedded-resource       | <boolean>                               |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_x-kubernetes-int-or-string           | <boolean>                               |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_validation_openAPIV3Schema_x-kubernetes-preserve-unknown-fields | <boolean>                               |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_version                                                         | <string>                                |
+----------------------------------------------------------------------+-----------------------------------------+
| spec_versions                                                        | <[]COMPONENT.ResourceDefinitionVersion> |
+----------------------------------------------------------------------+-----------------------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "apiVersion": "apiextensions.k8s.io/v1beta1",
        "kind": "CustomResourceDefinition",
        "metadata": "<COMPONENT.Metadata>",
        "spec": {
            "additionalPrinterColumns": "<[]COMPONENT.PrinterColumn>",
            "conversion": {
                "conversionReviewVersions": "<[]string>",
                "strategy": "<string>",
                "webhookClientConfig": "<COMPONENT.ClientConfig>"
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
            "subresources": {
                "scale": {
                    "labelSelectorPath": "<string>",
                    "specReplicasPath": "<string>",
                    "statusReplicasPath": "<string>"
                },
                "status": "<map[string]>"
            },
            "validation": {
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
                    "x-kubernetes-preserve-unknown-fields": "<boolean>"
                }
            },
            "version": "<string>",
            "versions": "<[]COMPONENT.ResourceDefinitionVersion>"
        }
    }