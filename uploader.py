import boto3
import os

access_key = #############
secret_access_key  = #######################

s3_client = boto3.client('s3',
                          aws_access_key_id = access_key,
                          aws_secret_access_key = secret_access_key)

for file in os.listdir():
    if ".csv" in file:
        file_key = 'downloads/' +str(file)
        bucket = 'bucketnamehere'
        s3_client.upload(file,bucket,file_key)
        
