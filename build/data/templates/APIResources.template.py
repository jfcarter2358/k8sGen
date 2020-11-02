'''
Kubernetes (( APIRESOURCE )) component for use in API resources

Available manifest keys are:
    (( MANIFEST_KEYS ))
'''
class (( APIRESOURCE ))(K8sObject):
    def __init__(self):
        super().__init__(name="(( APIRESOURCE ))", data_source='api_resources_data')