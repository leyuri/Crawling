import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        print(id(self))
        print("function2 called!")


f = SelfTest()
# print(dir(f))

# f.function1()
# 호출이 안된다.
f.function2()
# self는 자동으로 넘겨간다는 의미?
# 주소값이 일치


print(SelfTest.function1())
