import time
import boto3
import os

def s3listener():
    s3 = boto3.client('s3')
    s3items = s3.list_objects_v2(Bucket="vishnubucket5feb2021")['Contents']
    ls = []
    for items in s3items:
        temp = items['Key']
        ls.append(temp)
        # print(ls)
    return ls

# i = 1
while True:
    lsold = os.listdir(path="./s3bucket/")
    print(lsold)
    lsdiff = []
    time.sleep(10)

    lsnew = s3listener()

    if lsnew == lsold:
        pass
    else:
        s3 = boto3.client('s3')
        lsdiff = list(list(set(lsold) - set(lsnew)) + list(set(lsnew) - set(lsold)))
        # print(lsdiff)
        for item in lsdiff:
            #print(item)
            # filename = item
            # print(item)
            s3.download_file("vishnubucket5feb2021", item , "./s3bucket/%s" %(item))
            # s3.download_fileobj("vishnubucket5feb2021", item, "./s3bucket/%s" % (item))
    # i += 1