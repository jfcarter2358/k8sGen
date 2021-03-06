LocalSubjectAccessReview
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

+-------------------------------------+--------------------------+
| Key                                 | Type                     |
+=====================================+==========================+
| apiVersion                          | authorization.k8s.io/v1  |
+-------------------------------------+--------------------------+
| kind                                | LocalSubjectAccessReview |
+-------------------------------------+--------------------------+
| metadata                            | <COMPONENT.Metadata>     |
+-------------------------------------+--------------------------+
| spec_extra                          | <map[string][]string>    |
+-------------------------------------+--------------------------+
| spec_groups                         | <[]string>               |
+-------------------------------------+--------------------------+
| spec_nonResourceAttributes_path     | <string>                 |
+-------------------------------------+--------------------------+
| spec_nonResourceAttributes_verb     | <string>                 |
+-------------------------------------+--------------------------+
| spec_resourceAttributes_group       | <string>                 |
+-------------------------------------+--------------------------+
| spec_resourceAttributes_name        | <string>                 |
+-------------------------------------+--------------------------+
| spec_resourceAttributes_namespace   | <string>                 |
+-------------------------------------+--------------------------+
| spec_resourceAttributes_resource    | <string>                 |
+-------------------------------------+--------------------------+
| spec_resourceAttributes_subresource | <string>                 |
+-------------------------------------+--------------------------+
| spec_resourceAttributes_verb        | <string>                 |
+-------------------------------------+--------------------------+
| spec_resourceAttributes_version     | <string>                 |
+-------------------------------------+--------------------------+
| spec_uid                            | <string>                 |
+-------------------------------------+--------------------------+
| spec_user                           | <string>                 |
+-------------------------------------+--------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "apiVersion": "authorization.k8s.io/v1",
        "kind": "LocalSubjectAccessReview",
        "metadata": "<COMPONENT.Metadata>",
        "spec": {
            "extra": "<map[string][]string>",
            "groups": "<[]string>",
            "nonResourceAttributes": {
                "path": "<string>",
                "verb": "<string>"
            },
            "resourceAttributes": {
                "group": "<string>",
                "name": "<string>",
                "namespace": "<string>",
                "resource": "<string>",
                "subresource": "<string>",
                "verb": "<string>",
                "version": "<string>"
            },
            "uid": "<string>",
            "user": "<string>"
        }
    }