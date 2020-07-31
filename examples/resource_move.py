# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, BucketManager

# 七牛账号的 Access Key 和 Secret Key
access_key = "<access_key>"
secret_key = "<secret_key>"

# 源 空间名
bucket_name = ""

# 文件名
key = ""

# 目标空间名
bucket_name_to = ""

# 文件名
key_to = "test7.txt"

q = Auth(access_key, secret_key)

bucket = BucketManager(q)

ret, info = bucket.move(bucket_name, key, bucket_name_to, key_to)

print(ret)
print(info)
