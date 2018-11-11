from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 안녕하세요. 현재 네이버에서 헤더정보가 없는 크롤링 및 스크랩핑은 403 forbidden (접근 거부) 가
#발생되도록 막아놓은 상태입니다.
# 코드 설명을 드리면 헤더(Header)정보를 심어서 User-agent 정보를 같이 보내는 코드입니다.

opener = req.build_opener()
opener.addheaders = [("User-agent", "Mozilla/5.0")]
req.install_opener(opener)

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="

quote = rep.quote_plus("떡볶이")
# quote = rep.quote_plus("고래")
url = base + quote

res = req.urlopen(url)
savePath = "/Users/yuri/Documents/crawling/section2/Tteokbokki/"

#예외처리
try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")
li_list = soup.select("div.img_area._item > a.thumb._thumb > img")

for i, li_list in enumerate(li_list,1):
    # print(li_list)
    # print (li_list['data-source'])
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    # print(fullFileName)
    req.urlretrieve(li_list['data-source'],fullFileName)

print("다운로드 완료")
