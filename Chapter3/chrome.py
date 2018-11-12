import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


chrome_options = Options()
chrome_options.add_argument("--headless") #CLI환경구축

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/Users/yuri/Documents/crawling/Chapter3/webdriver/chrome/chromedriver")
# driver.set_window_size(1900,1200)
# time.sleep(5)
# driver.implicitly_wait(5)

driver.get('https://google.com')
driver.save_screenshot("/Users/yuri/Documents/crawling/Chapter3/Website1.png")

# driver.implicitly_wait(5)

driver.get('https://www.daum.net')

driver.save_screenshot("/Users/yuri/Documents/crawling/Chapter3/Website2.png")
driver.quit()

print("스크린샷 완료")
