import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#클래스 변수, 인스턴스 변수
class NameTest:
    total = 0

print(dir())
print("before: ", NameTest.__dict__)
NameTest.total = 1
print("after: ", NameTest.__dict__)
