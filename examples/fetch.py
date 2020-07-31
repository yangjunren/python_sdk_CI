# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth
from qiniu import BucketManager

access_key = '...'
secret_key = '...'

bucket_name = '...'

q = Auth(access_key, secret_key)

bucket = BucketManager(q)

url = '...'

key = '...'

ret, info = bucket.fetch(url, bucket_name, key)
print(ret)
print(info)