Event
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

+--------------------------------+----------------------+
| Key                            | Type                 |
+================================+======================+
| action                         | <string>             |
+--------------------------------+----------------------+
| apiVersion                     | v1                   |
+--------------------------------+----------------------+
| count                          | <integer>            |
+--------------------------------+----------------------+
| eventTime                      | <string>             |
+--------------------------------+----------------------+
| firstTimestamp                 | <string>             |
+--------------------------------+----------------------+
| involvedObject_apiVersion      | <string>             |
+--------------------------------+----------------------+
| involvedObject_fieldPath       | <string>             |
+--------------------------------+----------------------+
| involvedObject_kind            | <string>             |
+--------------------------------+----------------------+
| involvedObject_name            | <string>             |
+--------------------------------+----------------------+
| involvedObject_namespace       | <string>             |
+--------------------------------+----------------------+
| involvedObject_resourceVersion | <string>             |
+--------------------------------+----------------------+
| involvedObject_uid             | <string>             |
+--------------------------------+----------------------+
| kind                           | Event                |
+--------------------------------+----------------------+
| lastTimestamp                  | <string>             |
+--------------------------------+----------------------+
| message                        | <string>             |
+--------------------------------+----------------------+
| metadata                       | <COMPONENT.Metadata> |
+--------------------------------+----------------------+
| reason                         | <string>             |
+--------------------------------+----------------------+
| related_apiVersion             | <string>             |
+--------------------------------+----------------------+
| related_fieldPath              | <string>             |
+--------------------------------+----------------------+
| related_kind                   | <string>             |
+--------------------------------+----------------------+
| related_name                   | <string>             |
+--------------------------------+----------------------+
| related_namespace              | <string>             |
+--------------------------------+----------------------+
| related_resourceVersion        | <string>             |
+--------------------------------+----------------------+
| related_uid                    | <string>             |
+--------------------------------+----------------------+
| reportingComponent             | <string>             |
+--------------------------------+----------------------+
| reportingInstance              | <string>             |
+--------------------------------+----------------------+
| series_count                   | <integer>            |
+--------------------------------+----------------------+
| series_lastObservedTime        | <string>             |
+--------------------------------+----------------------+
| series_state                   | <string>             |
+--------------------------------+----------------------+
| source_component               | <string>             |
+--------------------------------+----------------------+
| source_host                    | <string>             |
+--------------------------------+----------------------+
| type                           | <string>             |
+--------------------------------+----------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "action": "<string>",
        "apiVersion": "v1",
        "count": "<integer>",
        "eventTime": "<string>",
        "firstTimestamp": "<string>",
        "involvedObject": {
            "apiVersion": "<string>",
            "fieldPath": "<string>",
            "kind": "<string>",
            "name": "<string>",
            "namespace": "<string>",
            "resourceVersion": "<string>",
            "uid": "<string>"
        },
        "kind": "Event",
        "lastTimestamp": "<string>",
        "message": "<string>",
        "metadata": "<COMPONENT.Metadata>",
        "reason": "<string>",
        "related": {
            "apiVersion": "<string>",
            "fieldPath": "<string>",
            "kind": "<string>",
            "name": "<string>",
            "namespace": "<string>",
            "resourceVersion": "<string>",
            "uid": "<string>"
        },
        "reportingComponent": "<string>",
        "reportingInstance": "<string>",
        "series": {
            "count": "<integer>",
            "lastObservedTime": "<string>",
            "state": "<string>"
        },
        "source": {
            "component": "<string>",
            "host": "<string>"
        },
        "type": "<string>"
    }