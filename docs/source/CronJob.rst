CronJob
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

+-----------------------------------------------+---------------------------+
| Key                                           | Type                      |
+===============================================+===========================+
| apiVersion                                    | batch/v1beta1             |
+-----------------------------------------------+---------------------------+
| kind                                          | CronJob                   |
+-----------------------------------------------+---------------------------+
| metadata                                      | <COMPONENT.Metadata>      |
+-----------------------------------------------+---------------------------+
| spec_concurrencyPolicy                        | <string>                  |
+-----------------------------------------------+---------------------------+
| spec_failedJobsHistoryLimit                   | <integer>                 |
+-----------------------------------------------+---------------------------+
| spec_jobTemplate_metadata                     | <COMPONENT.Metadata>      |
+-----------------------------------------------+---------------------------+
| spec_jobTemplate_spec_activeDeadlineSeconds   | <integer>                 |
+-----------------------------------------------+---------------------------+
| spec_jobTemplate_spec_backoffLimit            | <integer>                 |
+-----------------------------------------------+---------------------------+
| spec_jobTemplate_spec_completions             | <integer>                 |
+-----------------------------------------------+---------------------------+
| spec_jobTemplate_spec_manualSelector          | <boolean>                 |
+-----------------------------------------------+---------------------------+
| spec_jobTemplate_spec_parallelism             | <integer>                 |
+-----------------------------------------------+---------------------------+
| spec_jobTemplate_spec_selector                | <COMPONENT.Selector>      |
+-----------------------------------------------+---------------------------+
| spec_jobTemplate_spec_template_metadata       | <COMPONENT.Metadata>      |
+-----------------------------------------------+---------------------------+
| spec_jobTemplate_spec_template_spec           | <COMPONENT.ContainerSpec> |
+-----------------------------------------------+---------------------------+
| spec_jobTemplate_spec_ttlSecondsAfterFinished | <integer>                 |
+-----------------------------------------------+---------------------------+
| spec_schedule                                 | <string>                  |
+-----------------------------------------------+---------------------------+
| spec_startingDeadlineSeconds                  | <integer>                 |
+-----------------------------------------------+---------------------------+
| spec_successfulJobsHistoryLimit               | <integer>                 |
+-----------------------------------------------+---------------------------+
| spec_suspend                                  | <boolean>                 |
+-----------------------------------------------+---------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "apiVersion": "batch/v1beta1",
        "kind": "CronJob",
        "metadata": "<COMPONENT.Metadata>",
        "spec": {
            "concurrencyPolicy": "<string>",
            "failedJobsHistoryLimit": "<integer>",
            "jobTemplate": {
                "metadata": "<COMPONENT.Metadata>",
                "spec": {
                    "activeDeadlineSeconds": "<integer>",
                    "backoffLimit": "<integer>",
                    "completions": "<integer>",
                    "manualSelector": "<boolean>",
                    "parallelism": "<integer>",
                    "selector": "<COMPONENT.Selector>",
                    "template": {
                        "metadata": "<COMPONENT.Metadata>",
                        "spec": "<COMPONENT.ContainerSpec>"
                    },
                    "ttlSecondsAfterFinished": "<integer>"
                }
            },
            "schedule": "<string>",
            "startingDeadlineSeconds": "<integer>",
            "successfulJobsHistoryLimit": "<integer>",
            "suspend": "<boolean>"
        }
    }