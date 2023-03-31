import boto3

KEY_BUCKET = "AKIAVVKH7VVUPMQIKXWX"


def upload_file(file_name, bucket):
    object_name = file_name
    s3_client = boto3.client("s3")
    response = s3_client.upload_file("/public/" + file_name, bucket, object_name)
    return response


def list_files(bucket):
    s3_client = boto3.client("s3")
    contents = []
    try:
        for item in s3_client.list_objects(Bucket=bucket)["Contents"]:
            contents.append(item)
    except Exception as e:
        pass
    return contents


def show_image(bucket):
    s3_client = boto3.client("s3")
    # location = boto3.client('s3').get_bucket_location(Bucket=bucket)['LocationConstraint']
    public_urls = []
    try:
        for item in s3_client.list_objects(Bucket=bucket)["Contents"]:
            presigned_url = s3_client.generate_presigned_url(
                "get_object",
                Params={"Bucket": bucket, "Key": item["Key"]},
                ExpiresIn=100,
            )
            public_urls.append(presigned_url)
    except Exception as e:
        pass
    return public_urls
