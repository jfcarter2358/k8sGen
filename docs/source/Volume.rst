Volume
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

+---------------------------------+--------------------------------------+
| Key                             | Type                                 |
+=================================+======================================+
| awsElasticBlockStore_fsType     | <string>                             |
+---------------------------------+--------------------------------------+
| awsElasticBlockStore_partition  | <integer>                            |
+---------------------------------+--------------------------------------+
| awsElasticBlockStore_readOnly   | <boolean>                            |
+---------------------------------+--------------------------------------+
| awsElasticBlockStore_volumeID   | <string>                             |
+---------------------------------+--------------------------------------+
| azureDisk_cachingMode           | <string>                             |
+---------------------------------+--------------------------------------+
| azureDisk_diskName              | <string>                             |
+---------------------------------+--------------------------------------+
| azureDisk_diskURI               | <string>                             |
+---------------------------------+--------------------------------------+
| azureDisk_fsType                | <string>                             |
+---------------------------------+--------------------------------------+
| azureDisk_kind                  | <string>                             |
+---------------------------------+--------------------------------------+
| azureDisk_readOnly              | <boolean>                            |
+---------------------------------+--------------------------------------+
| azureFile_readOnly              | <boolean>                            |
+---------------------------------+--------------------------------------+
| azureFile_secretName            | <string>                             |
+---------------------------------+--------------------------------------+
| azureFile_shareName             | <string>                             |
+---------------------------------+--------------------------------------+
| cephfs_monitors                 | <[]string>                           |
+---------------------------------+--------------------------------------+
| cephfs_path                     | <string>                             |
+---------------------------------+--------------------------------------+
| cephfs_readOnly                 | <boolean>                            |
+---------------------------------+--------------------------------------+
| cephfs_secretFile               | <string>                             |
+---------------------------------+--------------------------------------+
| cephfs_secretRef_name           | <string>                             |
+---------------------------------+--------------------------------------+
| cephfs_user                     | <string>                             |
+---------------------------------+--------------------------------------+
| cinder_fsType                   | <string>                             |
+---------------------------------+--------------------------------------+
| cinder_readOnly                 | <boolean>                            |
+---------------------------------+--------------------------------------+
| cinder_secretRef_name           | <string>                             |
+---------------------------------+--------------------------------------+
| cinder_volumeID                 | <string>                             |
+---------------------------------+--------------------------------------+
| configMap_defaultMode           | <integer>                            |
+---------------------------------+--------------------------------------+
| configMap_items                 | <[]COMPONENT.ConfigMapItem>          |
+---------------------------------+--------------------------------------+
| configMap_name                  | <string>                             |
+---------------------------------+--------------------------------------+
| configMap_optional              | <boolean>                            |
+---------------------------------+--------------------------------------+
| csi_driver                      | <string>                             |
+---------------------------------+--------------------------------------+
| csi_fsType                      | <string>                             |
+---------------------------------+--------------------------------------+
| csi_nodePublishSecretRef_name   | <string>                             |
+---------------------------------+--------------------------------------+
| csi_readOnly                    | <boolean>                            |
+---------------------------------+--------------------------------------+
| csi_volumeAttributes            | <map[string]string>                  |
+---------------------------------+--------------------------------------+
| downwardAPI_defaultMode         | <integer>                            |
+---------------------------------+--------------------------------------+
| downwardAPI_items               | <[]COMPONENT.DownwardAPIItem>        |
+---------------------------------+--------------------------------------+
| emptyDir_medium                 | <string>                             |
+---------------------------------+--------------------------------------+
| emptyDir_sizeLimit              | <string>                             |
+---------------------------------+--------------------------------------+
| fc_fsType                       | <string>                             |
+---------------------------------+--------------------------------------+
| fc_lun                          | <integer>                            |
+---------------------------------+--------------------------------------+
| fc_readOnly                     | <boolean>                            |
+---------------------------------+--------------------------------------+
| fc_targetWWNs                   | <[]string>                           |
+---------------------------------+--------------------------------------+
| fc_wwids                        | <[]string>                           |
+---------------------------------+--------------------------------------+
| flexVolume_driver               | <string>                             |
+---------------------------------+--------------------------------------+
| flexVolume_fsType               | <string>                             |
+---------------------------------+--------------------------------------+
| flexVolume_options              | <map[string]string>                  |
+---------------------------------+--------------------------------------+
| flexVolume_readOnly             | <boolean>                            |
+---------------------------------+--------------------------------------+
| flexVolume_secretRef_name       | <string>                             |
+---------------------------------+--------------------------------------+
| flocker_datasetName             | <string>                             |
+---------------------------------+--------------------------------------+
| flocker_datasetUUID             | <string>                             |
+---------------------------------+--------------------------------------+
| gcePersistentDisk_fsType        | <string>                             |
+---------------------------------+--------------------------------------+
| gcePersistentDisk_partition     | <integer>                            |
+---------------------------------+--------------------------------------+
| gcePersistentDisk_pdName        | <string>                             |
+---------------------------------+--------------------------------------+
| gcePersistentDisk_readOnly      | <boolean>                            |
+---------------------------------+--------------------------------------+
| gitRepo_directory               | <string>                             |
+---------------------------------+--------------------------------------+
| gitRepo_repository              | <string>                             |
+---------------------------------+--------------------------------------+
| gitRepo_revision                | <string>                             |
+---------------------------------+--------------------------------------+
| glusterfs_endpoints             | <string>                             |
+---------------------------------+--------------------------------------+
| glusterfs_path                  | <string>                             |
+---------------------------------+--------------------------------------+
| glusterfs_readOnly              | <boolean>                            |
+---------------------------------+--------------------------------------+
| hostPath_path                   | <string>                             |
+---------------------------------+--------------------------------------+
| hostPath_type                   | <string>                             |
+---------------------------------+--------------------------------------+
| iscsi_chapAuthDiscovery         | <boolean>                            |
+---------------------------------+--------------------------------------+
| iscsi_chapAuthSession           | <boolean>                            |
+---------------------------------+--------------------------------------+
| iscsi_fsType                    | <string>                             |
+---------------------------------+--------------------------------------+
| iscsi_initiatorName             | <string>                             |
+---------------------------------+--------------------------------------+
| iscsi_iqn                       | <string>                             |
+---------------------------------+--------------------------------------+
| iscsi_iscsiInterface            | <string>                             |
+---------------------------------+--------------------------------------+
| iscsi_lun                       | <integer>                            |
+---------------------------------+--------------------------------------+
| iscsi_portals                   | <[]string>                           |
+---------------------------------+--------------------------------------+
| iscsi_readOnly                  | <boolean>                            |
+---------------------------------+--------------------------------------+
| iscsi_secretRef_name            | <string>                             |
+---------------------------------+--------------------------------------+
| iscsi_targetPortal              | <string>                             |
+---------------------------------+--------------------------------------+
| name                            | <string>                             |
+---------------------------------+--------------------------------------+
| nfs_path                        | <string>                             |
+---------------------------------+--------------------------------------+
| nfs_readOnly                    | <boolean>                            |
+---------------------------------+--------------------------------------+
| nfs_server                      | <string>                             |
+---------------------------------+--------------------------------------+
| persistentVolumeClaim_claimName | <string>                             |
+---------------------------------+--------------------------------------+
| persistentVolumeClaim_readOnly  | <boolean>                            |
+---------------------------------+--------------------------------------+
| photonPersistentDisk_fsType     | <string>                             |
+---------------------------------+--------------------------------------+
| photonPersistentDisk_pdID       | <string>                             |
+---------------------------------+--------------------------------------+
| portworxVolume_fsType           | <string>                             |
+---------------------------------+--------------------------------------+
| portworxVolume_readOnly         | <boolean>                            |
+---------------------------------+--------------------------------------+
| portworxVolume_volumeID         | <string>                             |
+---------------------------------+--------------------------------------+
| projected_defaultMode           | <integer>                            |
+---------------------------------+--------------------------------------+
| projected_sources               | <[]COMPONENT.ProjectedVolumeSources> |
+---------------------------------+--------------------------------------+
| quobyte_group                   | <string>                             |
+---------------------------------+--------------------------------------+
| quobyte_readOnly                | <boolean>                            |
+---------------------------------+--------------------------------------+
| quobyte_registry                | <string>                             |
+---------------------------------+--------------------------------------+
| quobyte_tenant                  | <string>                             |
+---------------------------------+--------------------------------------+
| quobyte_user                    | <string>                             |
+---------------------------------+--------------------------------------+
| quobyte_volume                  | <string>                             |
+---------------------------------+--------------------------------------+
| rbd_fsType                      | <string>                             |
+---------------------------------+--------------------------------------+
| rbd_image                       | <string>                             |
+---------------------------------+--------------------------------------+
| rbd_keyring                     | <string>                             |
+---------------------------------+--------------------------------------+
| rbd_monitors                    | <[]string>                           |
+---------------------------------+--------------------------------------+
| rbd_pool                        | <string>                             |
+---------------------------------+--------------------------------------+
| rbd_readOnly                    | <boolean>                            |
+---------------------------------+--------------------------------------+
| rbd_secretRef_name              | <string>                             |
+---------------------------------+--------------------------------------+
| rbd_user                        | <string>                             |
+---------------------------------+--------------------------------------+
| scaleIO_fsType                  | <string>                             |
+---------------------------------+--------------------------------------+
| scaleIO_gateway                 | <string>                             |
+---------------------------------+--------------------------------------+
| scaleIO_protectionDomain        | <string>                             |
+---------------------------------+--------------------------------------+
| scaleIO_readOnly                | <boolean>                            |
+---------------------------------+--------------------------------------+
| scaleIO_secretRef_name          | <string>                             |
+---------------------------------+--------------------------------------+
| scaleIO_sslEnabled              | <boolean>                            |
+---------------------------------+--------------------------------------+
| scaleIO_storageMode             | <string>                             |
+---------------------------------+--------------------------------------+
| scaleIO_storagePool             | <string>                             |
+---------------------------------+--------------------------------------+
| scaleIO_system                  | <string>                             |
+---------------------------------+--------------------------------------+
| scaleIO_volumeName              | <string>                             |
+---------------------------------+--------------------------------------+
| secret_defaultMode              | <integer>                            |
+---------------------------------+--------------------------------------+
| secret_items                    | <[]COMPONENT.SecretItem>             |
+---------------------------------+--------------------------------------+
| secret_optional                 | <boolean>                            |
+---------------------------------+--------------------------------------+
| secret_secretName               | <string>                             |
+---------------------------------+--------------------------------------+
| storageos_fsType                | <string>                             |
+---------------------------------+--------------------------------------+
| storageos_readOnly              | <boolean>                            |
+---------------------------------+--------------------------------------+
| storageos_secretRef_name        | <string>                             |
+---------------------------------+--------------------------------------+
| storageos_volumeName            | <string>                             |
+---------------------------------+--------------------------------------+
| storageos_volumeNamespace       | <string>                             |
+---------------------------------+--------------------------------------+
| vsphereVolume_fsType            | <string>                             |
+---------------------------------+--------------------------------------+
| vsphereVolume_storagePolicyID   | <string>                             |
+---------------------------------+--------------------------------------+
| vsphereVolume_storagePolicyName | <string>                             |
+---------------------------------+--------------------------------------+
| vsphereVolume_volumePath        | <string>                             |
+---------------------------------+--------------------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "awsElasticBlockStore": {
            "fsType": "<string>",
            "partition": "<integer>",
            "readOnly": "<boolean>",
            "volumeID": "<string>"
        },
        "azureDisk": {
            "cachingMode": "<string>",
            "diskName": "<string>",
            "diskURI": "<string>",
            "fsType": "<string>",
            "kind": "<string>",
            "readOnly": "<boolean>"
        },
        "azureFile": {
            "readOnly": "<boolean>",
            "secretName": "<string>",
            "shareName": "<string>"
        },
        "cephfs": {
            "monitors": "<[]string>",
            "path": "<string>",
            "readOnly": "<boolean>",
            "secretFile": "<string>",
            "secretRef": {
                "name": "<string>"
            },
            "user": "<string>"
        },
        "cinder": {
            "fsType": "<string>",
            "readOnly": "<boolean>",
            "secretRef": {
                "name": "<string>"
            },
            "volumeID": "<string>"
        },
        "configMap": {
            "defaultMode": "<integer>",
            "items": "<[]COMPONENT.ConfigMapItem>",
            "name": "<string>",
            "optional": "<boolean>"
        },
        "csi": {
            "driver": "<string>",
            "fsType": "<string>",
            "nodePublishSecretRef": {
                "name": "<string>"
            },
            "readOnly": "<boolean>",
            "volumeAttributes": "<map[string]string>"
        },
        "downwardAPI": {
            "defaultMode": "<integer>",
            "items": "<[]COMPONENT.DownwardAPIItem>"
        },
        "emptyDir": {
            "medium": "<string>",
            "sizeLimit": "<string>"
        },
        "fc": {
            "fsType": "<string>",
            "lun": "<integer>",
            "readOnly": "<boolean>",
            "targetWWNs": "<[]string>",
            "wwids": "<[]string>"
        },
        "flexVolume": {
            "driver": "<string>",
            "fsType": "<string>",
            "options": "<map[string]string>",
            "readOnly": "<boolean>",
            "secretRef": {
                "name": "<string>"
            }
        },
        "flocker": {
            "datasetName": "<string>",
            "datasetUUID": "<string>"
        },
        "gcePersistentDisk": {
            "fsType": "<string>",
            "partition": "<integer>",
            "pdName": "<string>",
            "readOnly": "<boolean>"
        },
        "gitRepo": {
            "directory": "<string>",
            "repository": "<string>",
            "revision": "<string>"
        },
        "glusterfs": {
            "endpoints": "<string>",
            "path": "<string>",
            "readOnly": "<boolean>"
        },
        "hostPath": {
            "path": "<string>",
            "type": "<string>"
        },
        "iscsi": {
            "chapAuthDiscovery": "<boolean>",
            "chapAuthSession": "<boolean>",
            "fsType": "<string>",
            "initiatorName": "<string>",
            "iqn": "<string>",
            "iscsiInterface": "<string>",
            "lun": "<integer>",
            "portals": "<[]string>",
            "readOnly": "<boolean>",
            "secretRef": {
                "name": "<string>"
            },
            "targetPortal": "<string>"
        },
        "name": "<string>",
        "nfs": {
            "path": "<string>",
            "readOnly": "<boolean>",
            "server": "<string>"
        },
        "persistentVolumeClaim": {
            "claimName": "<string>",
            "readOnly": "<boolean>"
        },
        "photonPersistentDisk": {
            "fsType": "<string>",
            "pdID": "<string>"
        },
        "portworxVolume": {
            "fsType": "<string>",
            "readOnly": "<boolean>",
            "volumeID": "<string>"
        },
        "projected": {
            "defaultMode": "<integer>",
            "sources": "<[]COMPONENT.ProjectedVolumeSources>"
        },
        "quobyte": {
            "group": "<string>",
            "readOnly": "<boolean>",
            "registry": "<string>",
            "tenant": "<string>",
            "user": "<string>",
            "volume": "<string>"
        },
        "rbd": {
            "fsType": "<string>",
            "image": "<string>",
            "keyring": "<string>",
            "monitors": "<[]string>",
            "pool": "<string>",
            "readOnly": "<boolean>",
            "secretRef": {
                "name": "<string>"
            },
            "user": "<string>"
        },
        "scaleIO": {
            "fsType": "<string>",
            "gateway": "<string>",
            "protectionDomain": "<string>",
            "readOnly": "<boolean>",
            "secretRef": {
                "name": "<string>"
            },
            "sslEnabled": "<boolean>",
            "storageMode": "<string>",
            "storagePool": "<string>",
            "system": "<string>",
            "volumeName": "<string>"
        },
        "secret": {
            "defaultMode": "<integer>",
            "items": "<[]COMPONENT.SecretItem>",
            "optional": "<boolean>",
            "secretName": "<string>"
        },
        "storageos": {
            "fsType": "<string>",
            "readOnly": "<boolean>",
            "secretRef": {
                "name": "<string>"
            },
            "volumeName": "<string>",
            "volumeNamespace": "<string>"
        },
        "vsphereVolume": {
            "fsType": "<string>",
            "storagePolicyID": "<string>",
            "storagePolicyName": "<string>",
            "volumePath": "<string>"
        }
    }