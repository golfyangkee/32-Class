### getter, setter : 값을 리턴하고, 값을 전달 및 변경하는 구조
class My:
    def __init__(self):
        self.x  =0
    @property               # 함수를 변수로 만듦 getter 인줄 안다.
    def myFun(self):        # 값을 리턴하는 용도
        return  self.x      # getter 기능

    @myFun.setter
    def myFun(self, x):
         self.x =x          # setter의 기능
'''
########################################################################
m=My()
m.myFun = 100
print(m.myFun)
'''

#클래스외부에서 함수를 선언하고
def f1(self, x, y):         # 누군가의 메소드이다. self 가 있으니까
    return min(x, x+y)

class C:
    f = f1 #클래스 내부에서 참조하는 방법
    def g(self):
        return 'hello world'
    h = g

if __name__ == '__main__':
    c =C()
    y=c.g()
    print(y)
    r =c.f(3,4)
    print(r)