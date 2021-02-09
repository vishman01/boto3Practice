import boto3

#Creating an S3 Bucket

s3 = boto3.resource('s3')
bucket = s3.create_bucket(
            ACL='public-read',
            Bucket = "vishnubucket5feb2021",
            CreateBucketConfiguration = {'LocationConstraint' : "ap-south-1"})

# Sending files to S3 

s3.meta.client.upload_file('sampleupload.txt', 'vishnubucket5feb2021', 'sample.txt')