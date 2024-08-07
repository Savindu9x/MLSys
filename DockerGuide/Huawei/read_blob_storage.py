!pip install esdk-obs-python

from obs import ObsClient
import traceback

accessKey = '--------------'
securityKey =  '----------------'
endpoint = 'https://obs.la-south-2.myhuaweicloud.com'

obsClient = ObsClient(
    access_key_id=accessKey,    
    secret_access_key=securityKey,    
    server=endpoint
)

def readBucketObjects(obsClient):
    """list objects in a bucket"""

    try:

        bucketName = 'sample-docs'
        max_keys = 10

        resp = obsClient.listObjects(bucketName, max_keys=max_keys, encoding_type='url')

        if resp.status < 300:
            print('List Objects Succeeded')
            print('requestId:', resp.requestId)
            print('name:', resp.body.name)
            print('prefix:', resp.body.prefix)
            print('max_keys:', resp.body.max_keys)
            print('is_truncated:', resp.body.is_truncated)
            index = 1
        for content in resp.body.contents:
            print('object [' + str(index) + ']')
            print('key:', content.key)
            print('lastModified:', content.lastModified)
            print('etag:', content.etag)
            print('size:', content.size)
            print('storageClass:', content.storageClass)
            print('owner_id:', content.owner.owner_id)
            print('owner_name:', content.owner.owner_name)
            index += 1
        else:
            print('List Objects Failed')
            print('requestId:', resp.requestId)
            print('errorCode:', resp.errorCode)
            print('errorMessage:', resp.errorMessage)
    except:
        print('List Objects Failed')
        print(traceback.format_exc())


def listBuckets():
    """list buckets in blob storage"""
    try:
        resp = obsClient.listBuckets(True) 
        if resp.status < 300: 
            print('requestId:', resp.requestId) 
            print('name:', resp.body.owner.owner_id) 
            print('create_date:', resp.body.owner.owner_name) 
            index = 1 
            for bucket in resp.body.buckets: 
                print('bucket [' + str(index) + ']') 
                print('name:', bucket.name) 
                print('create_date:', bucket.create_date) 
                print('location:', bucket.location)
                index += 1 
        else: 
            print('errorCode:', resp.errorCode) 
            print('errorMessage:', resp.errorMessage)
    except:
        print(traceback.format_exc())
