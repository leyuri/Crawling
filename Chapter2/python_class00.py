import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#클래스 변수, 인스턴스 변수

class Warehouse:
    stock_num = 0
    def __init__(self,name):
        self.name = name
        Warehouse.stock_num += 1
    # 의무적으로 자동 소거
    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse('kim')
user2 = Warehouse('park')

print(user1.name)
print(user2.name)

#namespace확인하기
print(user1.__dict__)
print(user2.__dict__)

print(Warehouse.__dict__)

print(user1.stock_num)
#자신의 네임스페이스에 존재하지 않을 경우 클래스 네임페이스에서 확인
print(user2.stock_num)




#인스턴스 네임스페이스 -> 클래스 네임스페이스, 클래스 변수 (공유)
# 출력결과
# kim
# park
# {'name': 'kim'}
# {'name': 'park'}
# {'__init__': <function Warehouse.__init__ at 0x102266620>, '__weakref__': <attribute '__weakref__' of 'Warehouse' objects>, '__doc__': None, '__dict__': <attribute '__dict__' of 'Warehouse' objects>, 'stock_num': 2, '__del__': <function Warehouse.__del__ at 0x1022666a8>, '__module__': '__main__'}
# 2
# 2
# [Finished in 0.049s]
