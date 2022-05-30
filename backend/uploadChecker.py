import boto3

BUCKET_NAME = "bucket-checker"

s3 =  boto3.client("s3")

# s3.create_bucket(Bucket=BUCKET_NAME)

buckets_resp = s3.list_buckets()

# for bucket in buckets_resp["Buckets"]:
#     print(bucket)

with open("./Shoes.jpg", "rb") as f:
    s3.upload_fileobj(f, BUCKET_NAME, "shoe_new.jpg", ExtraArgs={"ACL": "public-read"})