
from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://finance.naver.com/sise/"
res = req.urlopen(url).read()
content = res.decode('euc-kr','replace').encode('utf-8','replace')
soup = BeautifulSoup(content, "html.parser")


top = soup.select("#siselist_tab_0 > tr")

# for e in top:
#     if e.find("a") is not None:
#             print(e.find("a"))


#select_one을 이용하여 title값에 해당하는 string을 추출함

i = 1
for e in top:
    if e.find("a") is not None:
            print(i, e.select_one(".tltle").string)
            i += 1
