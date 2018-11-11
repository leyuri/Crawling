import sys
import io
import urllib.request

print('hi')
print('한글')

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://blogfiles.naver.net/20130502_54/dbsgusrl77_136748336507323OOv_JPEG/%BF%B5%C8%AD_%C0%BA%B9%D0%C7%CF%B0%D4_%C0%A7%B4%EB%C7%CF%B0%D4_%B8%DE%C0%CE_%BF%B9%B0%ED%C6%ED_%B5%BF%BF%B5%BB%F3_%281%29.jpg"
savePath = "/Users/yuri/Documents/section2/test1.jpg"


urllib.request.urlretrieve(imgUrl,savePath)
print("다운로드 완료!")

# import sys
# import io
# import urllib.request as dw
#
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#
# imgUrl ="http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg"
# htmlURL ="http://google.com"
#
# savePath1 ="/library/desktop pictures/qwe.jpg"
# savePath2 ="/library/desktop pictures/1.html"
#
# dw.urlretrieve(imgUrl, savePath1)
# dw.urlretrieve(htmlURL, savePath2)
#
# print("다운로드 완료!")
