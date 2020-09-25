PersistentVolume
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

+-----------------------------------------------+--------------------------------+
| Key                                           | Type                           |
+===============================================+================================+
| apiVersion                                    | v1                             |
+-----------------------------------------------+--------------------------------+
| kind                                          | PersistentVolume               |
+-----------------------------------------------+--------------------------------+
| metadata                                      | <COMPONENT.Metadata>           |
+-----------------------------------------------+--------------------------------+
| spec_accessModes                              | <[]string>                     |
+-----------------------------------------------+--------------------------------+
| spec_awsElasticBlockStore_fsType              | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_awsElasticBlockStore_partition           | <integer>                      |
+-----------------------------------------------+--------------------------------+
| spec_awsElasticBlockStore_readOnly            | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_awsElasticBlockStore_volumeID            | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_azureDisk_cachingMode                    | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_azureDisk_diskName                       | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_azureDisk_diskURI                        | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_azureDisk_fsType                         | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_azureDisk_kind                           | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_azureDisk_readOnly                       | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_azureFile_readOnly                       | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_azureFile_secretName                     | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_azureFile_secretNamespace                | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_azureFile_shareName                      | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_capacity                                 | <map[string]string>            |
+-----------------------------------------------+--------------------------------+
| spec_cephfs_monitors                          | <[]string>                     |
+-----------------------------------------------+--------------------------------+
| spec_cephfs_path                              | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_cephfs_readOnly                          | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_cephfs_secretFile                        | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_cephfs_secretRef_name                    | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_cephfs_secretRef_namespace               | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_cephfs_user                              | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_cinder_fsType                            | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_cinder_readOnly                          | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_cinder_secretRef_name                    | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_cinder_secretRef_namespace               | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_cinder_volumeID                          | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_claimRef_apiVersion                      | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_claimRef_fieldPath                       | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_claimRef_kind                            | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_claimRef_name                            | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_claimRef_namespace                       | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_claimRef_resourceVersion                 | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_claimRef_uid                             | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_csi_controllerExpandSecretRef_name       | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_csi_controllerExpandSecretRef_namespace  | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_csi_controllerPublishSecretRef_name      | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_csi_controllerPublishSecretRef_namespace | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_csi_driver                               | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_csi_fsType                               | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_csi_nodePublishSecretRef_name            | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_csi_nodePublishSecretRef_namespace       | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_csi_nodeStageSecretRef_name              | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_csi_nodeStageSecretRef_namespace         | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_csi_readOnly                             | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_csi_volumeAttributes                     | <map[string]string>            |
+-----------------------------------------------+--------------------------------+
| spec_csi_volumeHandle                         | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_fc_fsType                                | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_fc_lun                                   | <integer>                      |
+-----------------------------------------------+--------------------------------+
| spec_fc_readOnly                              | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_fc_targetWWNs                            | <[]string>                     |
+-----------------------------------------------+--------------------------------+
| spec_fc_wwids                                 | <[]string>                     |
+-----------------------------------------------+--------------------------------+
| spec_flexVolume_driver                        | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_flexVolume_fsType                        | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_flexVolume_options                       | <map[string]string>            |
+-----------------------------------------------+--------------------------------+
| spec_flexVolume_readOnly                      | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_flexVolume_secretRef_name                | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_flexVolume_secretRef_namespace           | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_flocker_datasetName                      | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_flocker_datasetUUID                      | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_gcePersistentDisk_fsType                 | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_gcePersistentDisk_partition              | <integer>                      |
+-----------------------------------------------+--------------------------------+
| spec_gcePersistentDisk_pdName                 | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_gcePersistentDisk_readOnly               | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_glusterfs_endpoints                      | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_glusterfs_endpointsNamespace             | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_glusterfs_path                           | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_glusterfs_readOnly                       | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_hostPath_path                            | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_hostPath_type                            | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_iscsi_chapAuthDiscovery                  | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_iscsi_chapAuthSession                    | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_iscsi_fsType                             | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_iscsi_initiatorName                      | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_iscsi_iqn                                | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_iscsi_iscsiInterface                     | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_iscsi_lun                                | <integer>                      |
+-----------------------------------------------+--------------------------------+
| spec_iscsi_portals                            | <[]string>                     |
+-----------------------------------------------+--------------------------------+
| spec_iscsi_readOnly                           | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_iscsi_secretRef_name                     | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_iscsi_secretRef_namespace                | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_iscsi_targetPortal                       | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_local_fsType                             | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_local_path                               | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_mountOptions                             | <[]string>                     |
+-----------------------------------------------+--------------------------------+
| spec_nfs_path                                 | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_nfs_readOnly                             | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_nfs_server                               | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_nodeAffinity_required_nodeSelectorTerms  | <[]COMPONENT.NodeSelectorTerm> |
+-----------------------------------------------+--------------------------------+
| spec_persistentVolumeReclaimPolicy            | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_photonPersistentDisk_fsType              | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_photonPersistentDisk_pdID                | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_portworxVolume_fsType                    | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_portworxVolume_readOnly                  | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_portworxVolume_volumeID                  | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_quobyte_group                            | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_quobyte_readOnly                         | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_quobyte_registry                         | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_quobyte_tenant                           | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_quobyte_user                             | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_quobyte_volume                           | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_rbd_fsType                               | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_rbd_image                                | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_rbd_keyring                              | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_rbd_monitors                             | <[]string>                     |
+-----------------------------------------------+--------------------------------+
| spec_rbd_pool                                 | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_rbd_readOnly                             | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_rbd_secretRef_name                       | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_rbd_secretRef_namespace                  | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_rbd_user                                 | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_scaleIO_fsType                           | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_scaleIO_gateway                          | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_scaleIO_protectionDomain                 | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_scaleIO_readOnly                         | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_scaleIO_secretRef_name                   | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_scaleIO_secretRef_namespace              | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_scaleIO_sslEnabled                       | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_scaleIO_storageMode                      | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_scaleIO_storagePool                      | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_scaleIO_system                           | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_scaleIO_volumeName                       | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_storageClassName                         | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_storageos_fsType                         | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_storageos_readOnly                       | <boolean>                      |
+-----------------------------------------------+--------------------------------+
| spec_storageos_secretRef_apiVersion           | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_storageos_secretRef_fieldPath            | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_storageos_secretRef_kind                 | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_storageos_secretRef_name                 | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_storageos_secretRef_namespace            | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_storageos_secretRef_resourceVersion      | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_storageos_secretRef_uid                  | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_storageos_volumeName                     | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_storageos_volumeNamespace                | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_volumeMode                               | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_vsphereVolume_fsType                     | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_vsphereVolume_storagePolicyID            | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_vsphereVolume_storagePolicyName          | <string>                       |
+-----------------------------------------------+--------------------------------+
| spec_vsphereVolume_volumePath                 | <string>                       |
+-----------------------------------------------+--------------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "apiVersion": "v1",
        "kind": "PersistentVolume",
        "metadata": "<COMPONENT.Metadata>",
        "spec": {
            "accessModes": "<[]string>",
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
                "secretNamespace": "<string>",
                "shareName": "<string>"
            },
            "capacity": "<map[string]string>",
            "cephfs": {
                "monitors": "<[]string>",
                "path": "<string>",
                "readOnly": "<boolean>",
                "secretFile": "<string>",
                "secretRef": {
                    "name": "<string>",
                    "namespace": "<string>"
                },
                "user": "<string>"
            },
            "cinder": {
                "fsType": "<string>",
                "readOnly": "<boolean>",
                "secretRef": {
                    "name": "<string>",
                    "namespace": "<string>"
                },
                "volumeID": "<string>"
            },
            "claimRef": {
                "apiVersion": "<string>",
                "fieldPath": "<string>",
                "kind": "<string>",
                "name": "<string>",
                "namespace": "<string>",
                "resourceVersion": "<string>",
                "uid": "<string>"
            },
            "csi": {
                "controllerExpandSecretRef": {
                    "name": "<string>",
                    "namespace": "<string>"
                },
                "controllerPublishSecretRef": {
                    "name": "<string>",
                    "namespace": "<string>"
                },
                "driver": "<string>",
                "fsType": "<string>",
                "nodePublishSecretRef": {
                    "name": "<string>",
                    "namespace": "<string>"
                },
                "nodeStageSecretRef": {
                    "name": "<string>",
                    "namespace": "<string>"
                },
                "readOnly": "<boolean>",
                "volumeAttributes": "<map[string]string>",
                "volumeHandle": "<string>"
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
                    "name": "<string>",
                    "namespace": "<string>"
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
            "glusterfs": {
                "endpoints": "<string>",
                "endpointsNamespace": "<string>",
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
                    "name": "<string>",
                    "namespace": "<string>"
                },
                "targetPortal": "<string>"
            },
            "local": {
                "fsType": "<string>",
                "path": "<string>"
            },
            "mountOptions": "<[]string>",
            "nfs": {
                "path": "<string>",
                "readOnly": "<boolean>",
                "server": "<string>"
            },
            "nodeAffinity": {
                "required": {
                    "nodeSelectorTerms": "<[]COMPONENT.NodeSelectorTerm>"
                }
            },
            "persistentVolumeReclaimPolicy": "<string>",
            "photonPersistentDisk": {
                "fsType": "<string>",
                "pdID": "<string>"
            },
            "portworxVolume": {
                "fsType": "<string>",
                "readOnly": "<boolean>",
                "volumeID": "<string>"
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
                    "name": "<string>",
                    "namespace": "<string>"
                },
                "user": "<string>"
            },
            "scaleIO": {
                "fsType": "<string>",
                "gateway": "<string>",
                "protectionDomain": "<string>",
                "readOnly": "<boolean>",
                "secretRef": {
                    "name": "<string>",
                    "namespace": "<string>"
                },
                "sslEnabled": "<boolean>",
                "storageMode": "<string>",
                "storagePool": "<string>",
                "system": "<string>",
                "volumeName": "<string>"
            },
            "storageClassName": "<string>",
            "storageos": {
                "fsType": "<string>",
                "readOnly": "<boolean>",
                "secretRef": {
                    "apiVersion": "<string>",
                    "fieldPath": "<string>",
                    "kind": "<string>",
                    "name": "<string>",
                    "namespace": "<string>",
                    "resourceVersion": "<string>",
                    "uid": "<string>"
                },
                "volumeName": "<string>",
                "volumeNamespace": "<string>"
            },
            "volumeMode": "<string>",
            "vsphereVolume": {
                "fsType": "<string>",
                "storagePolicyID": "<string>",
                "storagePolicyName": "<string>",
                "volumePath": "<string>"
            }
        }
    }