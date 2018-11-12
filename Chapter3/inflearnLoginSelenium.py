import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


# chrome_options = Options()
#CLI환경구축 driver만으로 원하는 에플리케이션을 만들 수 있다.
# chrome_options.add_argument("--headless")

# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/Users/yuri/Documents/crawling/Chapter3/webdriver/chrome/chromedriver")
driver = webdriver.Chrome("/Users/yuri/Documents/crawling/Chapter3/webdriver/chrome/chromedriver")
# 시각적 브라우저를 띄어줌으로써 확인할 수 있음
driver.set_window_size(1900,1200)
time.sleep(5)
driver.implicitly_wait(3)

driver.get('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F')
time.sleep(5)
driver.implicitly_wait(3)


print("스크린샷 완료")
