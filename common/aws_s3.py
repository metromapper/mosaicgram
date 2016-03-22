# coding: utf8

"""
S3に関する処理をここでおこなう
"""

import boto3

from secret_info import (
    BUCKET_NAME,
    ACCESS_KEY_ID,
    SECRET_ACCESS_KEY,
)

client = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
)

# upload images
def upload_image(image_name):
    """
    :param image_name:
    :return True or False:
    jpgの画像をあげるようにしてもらう
    """
    data = open('neko.jpg', 'rb')
    if client.Bucket(BUCKET_NAME).put_object(Key= image_name + '.jpg', Body=data) == None:
        return True
    else:
        return False
