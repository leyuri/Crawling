import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


firefox_options = Options()
#CLI환경구축 driver만으로 원하는 에플리케이션을 만들 수 있다.
firefox_options.add_argument("--headless")

driver = webdriver.Firefox(firefox_options=firefox_options, executable_path="/Users/yuri/Documents/crawling/Chapter3/webdriver/firefox/geckodriver")
# driver = webdriver.Chrome("/Users/yuri/Documents/crawling/Chapter3/webdriver/chrome/chromedriver")
# 시각적 브라우저를 띄어줌으로써 확인할 수 있음
# driver.set_window_size(1900,1200)
# time.sleep(5)
# driver.implicitly_wait(5)

driver.get('https://google.com')
driver.save_screenshot("/Users/yuri/Documents/crawling/Chapter3/Website_1.png")

# driver.implicitly_wait(5)

driver.get('https://www.daum.net')

driver.save_screenshot("/Users/yuri/Documents/crawling/Chapter3/Website_2.png")
driver.quit()

print("스크린샷 완료")

#왜 안되냐...
