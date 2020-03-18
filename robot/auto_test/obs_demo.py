#!/usr/bin/python
# -*- coding:utf-8 -*-



'''
This sample demonstrates how to post object under specified bucket from
OBS using the OBS SDK for Python.
'''

AK = 'YOUER AK'
SK = 'YOUER SK'
server = 'obs.cn-north-4.myhuaweicloud.com'
bucketName = 'obs-m-upload'
objectKey = 'obs-m-upload/shop/auction'
objectKey_path = 'shop/auction/'

import sys, os
IS_PYTHON2 = sys.version_info.major == 2 or sys.version < '3'

if IS_PYTHON2:
    import httplib
else:
    import http.client as httplib

def createSampleFile(sampleFilePath):
    if not os.path.exists(sampleFilePath):
        _dir = os.path.dirname(sampleFilePath)
        if not os.path.exists(_dir):
            os.makedirs(_dir, mode=0o755)
        import uuid
        with open(sampleFilePath, 'w') as f:
            f.write(str(uuid.uuid1()) + '\n')
            f.write(str(uuid.uuid4()) + '\n')
    return sampleFilePath

from obs import *

signature = 'obs'

# Constructs a obs client instance with your account for accessing OBS
obsClient = ObsClient(access_key_id=AK, secret_access_key=SK, server=server, signature=signature)


# Create bucket
# print('Create a new bucket for demo\n')
# obsClient.createBucket(bucketName)

# Create sample file
# sampleFilePath = '/temp/text.txt'
# createSampleFile(sampleFilePath)
def upload(sampleFilePath):
    # Claim a post object request
    formParams = {'x-obs-acl': 'public-read', 'content-type': 'text/plain'} if signature == 'obs' \
    else {'acl': 'public-read', 'content-type': 'text/plain'}
    res = obsClient.createPostSignature(bucketName, objectKey, expires=3600, formParams=formParams)

    # Start to post object
    formParams['key'] = objectKey
    formParams['policy'] = res['policy']

    ak_param = 'AccessKeyId' if signature == 'obs' else 'AwsAccessKeyId'
    formParams[ak_param] = res['accessKeyId']
    formParams['signature'] = res['signature']

    print('Creating object in post way')
    boundary = '9431149156168'

    buffers = []
    contentLength = 0

    # Construct form data
    buffer = []
    first = True
    for key, value in formParams.items():
        if not first:
            buffer.append('\r\n')
        else:
            first = False

        buffer.append('--')
        buffer.append(boundary)
        buffer.append('\r\n')
        buffer.append('Content-Disposition: form-data; name="')
        buffer.append(str(key))
        buffer.append('"\r\n\r\n')
        buffer.append(str(value))

    buffer = ''.join(buffer)
    buffer = buffer if IS_PYTHON2 else buffer.encode('UTF-8')
    contentLength += len(buffer)
    buffers.append(buffer)

    # Construct file description
    buffer = []
    buffer.append('\r\n')
    buffer.append('--')
    buffer.append(boundary)
    buffer.append('\r\n')
    buffer.append('Content-Disposition: form-data; name="file"; filename="')
    buffer.append('myfile')
    buffer.append('"\r\n')
    buffer.append('Content-Type: text/plain')
    buffer.append('\r\n\r\n')

    buffer = ''.join(buffer)
    buffer = buffer if IS_PYTHON2 else buffer.encode('UTF-8')
    contentLength += len(buffer)
    buffers.append(buffer)

    # Contruct end data
    buffer = []
    buffer.append('\r\n--')
    buffer.append(boundary)
    buffer.append('--\r\n')

    buffer = ''.join(buffer)
    buffer = buffer if IS_PYTHON2 else buffer.encode('UTF-8')
    contentLength += len(buffer)
    buffers.append(buffer)

    contentLength += os.path.getsize(sampleFilePath)


    conn = httplib.HTTPConnection(bucketName + '.' + server, 80)
    conn.request('POST', '/', headers={'Content-Length': str(contentLength), 'User-Agent': 'OBS/Test', 'Content-Type': 'multipart/form-data; boundary=' + boundary})

    # Send form data
    conn.send(buffers[0])

    # Send file description
    conn.send(buffers[1])

    # Send file data
    with open(sampleFilePath, 'rb') as f:
        while True:
            chunk = f.read(65536)
            if not chunk:
                break
            conn.send(chunk)

    # Send end data
    conn.send(buffers[2])


    result = conn.getresponse()
    status = result.status
    responseContent = result.read()
    if status < 300:
        print('Post object successfully.')
    else:
        print('Post object failed!!')

    if responseContent:
        print('\tresponseContent:')
        print('\t%s' % responseContent)
    conn.close()
    print('\n')

