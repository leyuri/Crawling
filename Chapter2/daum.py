from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "[](https://www.daum.net/) [https://www.daum.net/](https://www.daum.net/)"
res = req.urlopen(url).read()
soup = BeautifulSoup(res,"html.parser")

top = soup.find_all("a", tabindex="-1")
for e in top:
    print(e.string)
    print(e.get('href'))
