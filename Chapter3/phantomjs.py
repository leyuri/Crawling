import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver = webdriver.PhantomJS('/Users⁩/yuri⁩/Documents/⁨crawling⁩/Chapter3⁩/⁨webdriver⁩/phantomjs⁩/bin/phantomjs⁩⁩')
