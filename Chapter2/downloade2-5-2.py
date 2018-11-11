from urllib.parse import urljoin
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html>
<body>
<h1> BeautifulSoup study</h1>
<p>css그 선택자</P>
<p>채그 선택자</P>
</body>
</html>

"""


soup = BeautifulSoup(html, 'html.parser')
# print('soup', type(soup))
# 태그 tab 자동완성
# print('prettify', soup.prettify())

h1 = soup.html.body.h1
# print('h1',type(h1)) >>> class 형태로 출력
print(h1.string)

# p tag가 두개이면? next_sibling(하지만 공백 포함
# 위 예제에서는 enter을 첬음..) 따라서 next_sibling.next_sibling 두번

p1 = soup.html.body.p
print('p1',p1)
p2 = p1.next_sibling.next_sibling
print('p2', p2)


p3 = p1.previous_sibling.previous_sibling
print('p3', p3)


print("h1 >>", h1.string)
print("p >>", p1.string)
print("p >>", p2.string)
