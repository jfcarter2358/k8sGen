Builder
==================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

========

Usage
---------

Required files
++++++++++++++

In order to use the **K8sBuilder** class, you must first create a definition and configuration jsonc file.

An example config.jsonc file is shown below:

.. code-block:: JSON

    {
        "configmap": {
            "configmap_name": "foobar"
        }
    }

Definition files are more complex, it contains two main sections
* return
    * the APIResource that you want to generate the manifest for
* components
    * a list of Components/APIResources that you want to generate YAML for

Here is an example definition file to create a configmap from a file:

.. code-block:: JSON

    {
        "return": "configmap",
        "components": {
            "configmap" : {
                "type" : "APIResources.ConfigMap",
                "fields": {
                    "metadata": "${.metadata}",
                    "data": "${file.build/data/static/base.py}",
                }
            },
            "metadata" : {
                "type": "Components.Metadata",
                "fields": {
                    "name": "${config.configmap.configmap_name}",
                    "app": "my awesome app"
                }
            }
        }
    }


You'll notice that we create a "configmap" and "metadata" object. You can create as many as you like in the "components" section. 
In addition, as you can see in the "configmap" object, you can reference other objects via the format "${.<object name>}".

There are four main templating patterns in use in k8sgen (keep in mind, these are only acted on if htey are in a "fields" section of an object):
* ${.object_name}
    * This tells k8sgen that you want to replace this with the generated output of the object "object_name" within your definition file
* ${config.dot.notation.path}
    * This tells k8sgen that you want to replace this with the value contained in the config file located at "dot.notation.path"
* ${file.path/to/file}
    * This tells k8sgen that you want to replace this with the contents of a file located at "path/to/file"
* ${files.path/to/directory}
    * This tells k8sgen that you want to replace this with a map where the keys are the filenames and the values are the contents of those values

Each object in the definition file is made up of three main parts
* name
    * The name of the object also serves as its key in the jsonc document. This is what you will use to reference it within the document
* type
    * The k8sgen class this object is. Any APIResources can be referenced by "APIResources.<class name>" and any Components can be referenced by "Components.<class name>"
* fields
    * The fields you want to set for that object as described by the class documentation

Using the Builder class
+++++++++++++++++++++++
Once you have the requisite files created (you can also use strings/dictionaries in-memory) you can then use the K8sBuilder class.

To generate a compiled k8sgen object, run the following code:

.. code-block:: Python

    from k8sgen import K8sBuilder

    definition_path = '/path/to/defintion.jsonc'
    config_path = '/path/to/config.jsonc'

    builder = K8sBuilder()
    # if you want to pass the dictionary or string directory
    # then you will use "definition=definition_data" and "config=config_data" instead of 
    # definition_path and config_path
    out = builder.build_manifest(definition_path=definition_path, config_path=config_path)

    # if you want the yaml you can get that with
    out_yaml = out.to_yaml()