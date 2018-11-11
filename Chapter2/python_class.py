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

class UserInfo:
    def set_info(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("---------------")
        print("Name: " + self.name)
        print("Phone: " + self.phone)
        print("---------------")

#인스턴스 메모리에 올리는 과정
user1 = UserInfo()
user2 = UserInfo()

# print(id(user1))
# print(id(user1))

user1.set_info("yuri","010-1234-1234")
user2.set_info("yumi","010-1234-1224")

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)

print(user1.phone,user1.name)
