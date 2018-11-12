import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = requests.Session()

r = s.get('http://httpbin.org/stream/20', stream=True)
#print(r.text)
#print(r.encoding)
#print(r.json())
if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    #print(line)
    b = json.loads(line) #dict
    for e in b.keys():
        print("key:",e,"values:",b[e])

# import sys
# import io
# import requests, json
#
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#
# #Response 상태코드
# s = requests.Session()
# r = s.get('http://httpbin.org/stream/20')
# # print(r.text)
# # print(r.encoding)
# # >>>None
# if r.encoding is None:
#     r.encoding  = 'utf-8'
#
# # iterator 부분은 어떤 데이터 타입이 (배열, 리스트, Set, 딕셔너리) 형태인경우 인덱스를 사용해서
# # 순회 할 수 있는 기능이며, 대다수의 api에서 제공하고 있습니다.
# # 말그대로 라인별로 순서대로 순회에서 데이터를 처리하겠다는 메소드 입니다.
# for line in r.iter_lines(decode_unicode=True):
#     # print(line)
#     # print(json.loads(line))
#     b = json.loads(line))
#     print(b['origin'])
