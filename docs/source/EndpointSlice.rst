EndpointSlice
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

+---------------------------------------------+--------------------------+
| Key                                         | Type                     |
+=============================================+==========================+
| addressType                                 | <string>                 |
+---------------------------------------------+--------------------------+
| apiVersion                                  | discovery.k8s.io/v1beta1 |
+---------------------------------------------+--------------------------+
| endpoints_addresses                         | <[]string>               |
+---------------------------------------------+--------------------------+
| endpoints_conditions_ready                  | <boolean>                |
+---------------------------------------------+--------------------------+
| endpoints_hostname                          | <string>                 |
+---------------------------------------------+--------------------------+
| endpoints_targetRef_apiVersion              | <string>                 |
+---------------------------------------------+--------------------------+
| endpoints_targetRef_fieldPath               | <string>                 |
+---------------------------------------------+--------------------------+
| endpoints_targetRef_kind                    | <string>                 |
+---------------------------------------------+--------------------------+
| endpoints_targetRef_name                    | <string>                 |
+---------------------------------------------+--------------------------+
| endpoints_targetRef_namespace               | <string>                 |
+---------------------------------------------+--------------------------+
| endpoints_targetRef_resourceVersion         | <string>                 |
+---------------------------------------------+--------------------------+
| endpoints_targetRef_uid                     | <string>                 |
+---------------------------------------------+--------------------------+
| endpoints_topology                          | <map[string]string>      |
+---------------------------------------------+--------------------------+
| kind                                        | EndpointSlice            |
+---------------------------------------------+--------------------------+
| metadata_annotations                        | <map[string]string>      |
+---------------------------------------------+--------------------------+
| metadata_clusterName                        | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_creationTimestamp                  | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_deletionGracePeriodSeconds         | <integer>                |
+---------------------------------------------+--------------------------+
| metadata_deletionTimestamp                  | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_finalizers                         | <[]string>               |
+---------------------------------------------+--------------------------+
| metadata_generateName                       | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_generation                         | <integer>                |
+---------------------------------------------+--------------------------+
| metadata_labels                             | <map[string]string>      |
+---------------------------------------------+--------------------------+
| metadata_managedFields_apiVersion           | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_managedFields_fieldsType           | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_managedFields_fieldsV1             | <map[string]>            |
+---------------------------------------------+--------------------------+
| metadata_managedFields_manager              | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_managedFields_operation            | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_managedFields_time                 | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_name                               | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_namespace                          | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_ownerReferences_apiVersion         | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_ownerReferences_blockOwnerDeletion | <boolean>                |
+---------------------------------------------+--------------------------+
| metadata_ownerReferences_controller         | <boolean>                |
+---------------------------------------------+--------------------------+
| metadata_ownerReferences_kind               | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_ownerReferences_name               | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_ownerReferences_uid                | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_resourceVersion                    | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_selfLink                           | <string>                 |
+---------------------------------------------+--------------------------+
| metadata_uid                                | <string>                 |
+---------------------------------------------+--------------------------+
| ports_appProtocol                           | <string>                 |
+---------------------------------------------+--------------------------+
| ports_name                                  | <string>                 |
+---------------------------------------------+--------------------------+
| ports_port                                  | <integer>                |
+---------------------------------------------+--------------------------+
| ports_protocol                              | <string>                 |
+---------------------------------------------+--------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "addressType": "<string>",
        "apiVersion": "discovery.k8s.io/v1beta1",
        "endpoints": [
            {
                "addresses": "<[]string>",
                "conditions": {
                    "ready": "<boolean>"
                },
                "hostname": "<string>",
                "targetRef": {
                    "apiVersion": "<string>",
                    "fieldPath": "<string>",
                    "kind": "<string>",
                    "name": "<string>",
                    "namespace": "<string>",
                    "resourceVersion": "<string>",
                    "uid": "<string>"
                },
                "topology": "<map[string]string>"
            }
        ],
        "kind": "EndpointSlice",
        "metadata": {
            "annotations": "<map[string]string>",
            "clusterName": "<string>",
            "creationTimestamp": "<string>",
            "deletionGracePeriodSeconds": "<integer>",
            "deletionTimestamp": "<string>",
            "finalizers": "<[]string>",
            "generateName": "<string>",
            "generation": "<integer>",
            "labels": "<map[string]string>",
            "managedFields": [
                {
                    "apiVersion": "<string>",
                    "fieldsType": "<string>",
                    "fieldsV1": "<map[string]>",
                    "manager": "<string>",
                    "operation": "<string>",
                    "time": "<string>"
                }
            ],
            "name": "<string>",
            "namespace": "<string>",
            "ownerReferences": [
                {
                    "apiVersion": "<string>",
                    "blockOwnerDeletion": "<boolean>",
                    "controller": "<boolean>",
                    "kind": "<string>",
                    "name": "<string>",
                    "uid": "<string>"
                }
            ],
            "resourceVersion": "<string>",
            "selfLink": "<string>",
            "uid": "<string>"
        },
        "ports": [
            {
                "appProtocol": "<string>",
                "name": "<string>",
                "port": "<integer>",
                "protocol": "<string>"
            }
        ]
    }