!pip install esdk-obs-python

from obs import ObsClient

obsClient = ObsClient(
    access_key_id=ak,    
    secret_access_key=sk,    
    server=endpoint
)
