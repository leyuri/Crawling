import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url  = "http://www.kyobobook.co.kr/index.laf?OV_REFFER=https://www.google.co.kr/"


mem = req.urlopen(url)


# print((type(mem))
# print(type({}))
# print(type([]))
# print(type(()))

# print("geturl",mem.geturl())
# print("status",mem.status)
# print("headers",mem.getheaders())
#200(정상), 404, 403, 500(서버 error)


# print("info", mem.info())
# print("code", mem.getcode())
# print("read", mem.read(50).decode("utf-8")) #euc-kr ...
print(urlparse("https://www.google.com?test=test")) #query
