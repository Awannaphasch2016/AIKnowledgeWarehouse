import boto3 

s3 = boto3.client('s3')
s3.list_objects_v2(Bucket='example-bukkit')

def get_s3_keys(bucket):
    """Get a list of keys in an S3 bucket."""
    keys = []
    resp = s3.list_objects(Bucket=bucket)
    for obj in resp['Contents']:
        keys.append(obj['Key'])
    return keys

if __name__ == '__main__':
    bucket = 'covid19trendprediction'

    keys = get_s3_keys(bucket)
    print(keys)
