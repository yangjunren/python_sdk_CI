# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, DomainManager

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)
domain_manager = DomainManager(auth)

domain = "qb8z8byyd.bkt.clouddn.com"

ret, info = domain_manager.get_domain(domain)

print(ret)
print(info)
