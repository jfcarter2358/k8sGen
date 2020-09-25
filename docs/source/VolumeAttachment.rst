VolumeAttachment
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

+-----------------------------------------------------------------------+--------------------------------+
| Key                                                                   | Type                           |
+=======================================================================+================================+
| apiVersion                                                            | storage.k8s.io/v1              |
+-----------------------------------------------------------------------+--------------------------------+
| kind                                                                  | VolumeAttachment               |
+-----------------------------------------------------------------------+--------------------------------+
| metadata                                                              | <COMPONENT.Metadata>           |
+-----------------------------------------------------------------------+--------------------------------+
| spec_attacher                                                         | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_nodeName                                                         | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_accessModes                              | <[]string>                     |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_awsElasticBlockStore_fsType              | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_awsElasticBlockStore_partition           | <integer>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_awsElasticBlockStore_readOnly            | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_awsElasticBlockStore_volumeID            | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_azureDisk_cachingMode                    | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_azureDisk_diskName                       | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_azureDisk_diskURI                        | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_azureDisk_fsType                         | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_azureDisk_kind                           | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_azureDisk_readOnly                       | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_azureFile_readOnly                       | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_azureFile_secretName                     | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_azureFile_secretNamespace                | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_azureFile_shareName                      | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_capacity                                 | <map[string]string>            |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_cephfs_monitors                          | <[]string>                     |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_cephfs_path                              | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_cephfs_readOnly                          | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_cephfs_secretFile                        | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_cephfs_secretRef_name                    | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_cephfs_secretRef_namespace               | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_cephfs_user                              | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_cinder_fsType                            | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_cinder_readOnly                          | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_cinder_secretRef_name                    | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_cinder_secretRef_namespace               | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_cinder_volumeID                          | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_claimRef_apiVersion                      | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_claimRef_fieldPath                       | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_claimRef_kind                            | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_claimRef_name                            | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_claimRef_namespace                       | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_claimRef_resourceVersion                 | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_claimRef_uid                             | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_csi_controllerExpandSecretRef_name       | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_csi_controllerExpandSecretRef_namespace  | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_csi_controllerPublishSecretRef_name      | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_csi_controllerPublishSecretRef_namespace | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_csi_driver                               | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_csi_fsType                               | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_csi_nodePublishSecretRef_name            | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_csi_nodePublishSecretRef_namespace       | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_csi_nodeStageSecretRef_name              | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_csi_nodeStageSecretRef_namespace         | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_csi_readOnly                             | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_csi_volumeAttributes                     | <map[string]string>            |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_csi_volumeHandle                         | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_fc_fsType                                | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_fc_lun                                   | <integer>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_fc_readOnly                              | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_fc_targetWWNs                            | <[]string>                     |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_fc_wwids                                 | <[]string>                     |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_flexVolume_driver                        | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_flexVolume_fsType                        | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_flexVolume_options                       | <map[string]string>            |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_flexVolume_readOnly                      | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_flexVolume_secretRef_name                | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_flexVolume_secretRef_namespace           | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_flocker_datasetName                      | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_flocker_datasetUUID                      | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_gcePersistentDisk_fsType                 | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_gcePersistentDisk_partition              | <integer>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_gcePersistentDisk_pdName                 | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_gcePersistentDisk_readOnly               | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_glusterfs_endpoints                      | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_glusterfs_endpointsNamespace             | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_glusterfs_path                           | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_glusterfs_readOnly                       | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_hostPath_path                            | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_hostPath_type                            | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_iscsi_chapAuthDiscovery                  | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_iscsi_chapAuthSession                    | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_iscsi_fsType                             | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_iscsi_initiatorName                      | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_iscsi_iqn                                | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_iscsi_iscsiInterface                     | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_iscsi_lun                                | <integer>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_iscsi_portals                            | <[]string>                     |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_iscsi_readOnly                           | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_iscsi_secretRef_name                     | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_iscsi_secretRef_namespace                | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_iscsi_targetPortal                       | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_local_fsType                             | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_local_path                               | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_mountOptions                             | <[]string>                     |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_nfs_path                                 | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_nfs_readOnly                             | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_nfs_server                               | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_nodeAffinity_required_nodeSelectorTerms  | <[]COMPONENT.NodeSelectorTerm> |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_persistentVolumeReclaimPolicy            | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_photonPersistentDisk_fsType              | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_photonPersistentDisk_pdID                | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_portworxVolume_fsType                    | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_portworxVolume_readOnly                  | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_portworxVolume_volumeID                  | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_quobyte_group                            | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_quobyte_readOnly                         | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_quobyte_registry                         | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_quobyte_tenant                           | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_quobyte_user                             | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_quobyte_volume                           | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_rbd_fsType                               | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_rbd_image                                | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_rbd_keyring                              | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_rbd_monitors                             | <[]string>                     |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_rbd_pool                                 | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_rbd_readOnly                             | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_rbd_secretRef_name                       | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_rbd_secretRef_namespace                  | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_rbd_user                                 | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_scaleIO_fsType                           | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_scaleIO_gateway                          | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_scaleIO_protectionDomain                 | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_scaleIO_readOnly                         | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_scaleIO_secretRef_name                   | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_scaleIO_secretRef_namespace              | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_scaleIO_sslEnabled                       | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_scaleIO_storageMode                      | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_scaleIO_storagePool                      | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_scaleIO_system                           | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_scaleIO_volumeName                       | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_storageClassName                         | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_storageos_fsType                         | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_storageos_readOnly                       | <boolean>                      |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_storageos_secretRef_apiVersion           | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_storageos_secretRef_fieldPath            | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_storageos_secretRef_kind                 | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_storageos_secretRef_name                 | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_storageos_secretRef_namespace            | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_storageos_secretRef_resourceVersion      | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_storageos_secretRef_uid                  | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_storageos_volumeName                     | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_storageos_volumeNamespace                | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_volumeMode                               | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_vsphereVolume_fsType                     | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_vsphereVolume_storagePolicyID            | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_vsphereVolume_storagePolicyName          | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_inlineVolumeSpec_vsphereVolume_volumePath                 | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+
| spec_source_persistentVolumeName                                      | <string>                       |
+-----------------------------------------------------------------------+--------------------------------+


JSON fields
-----------

.. code-block:: JSON

    {
        "apiVersion": "storage.k8s.io/v1",
        "kind": "VolumeAttachment",
        "metadata": "<COMPONENT.Metadata>",
        "spec": {
            "attacher": "<string>",
            "nodeName": "<string>",
            "source": {
                "inlineVolumeSpec": {
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
                },
                "persistentVolumeName": "<string>"
            }
        }
    }