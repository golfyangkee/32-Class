# 함수 안에 또 다른 함수를 넣을 수 있다.

x = 10 # G에 해당 global 변수 이란 뜻
y = 11
print(id(x))    # id 동적할당한 유동주소
def foo():
    x = 20 # foo함수의 L에 해당, bar함수의 E에 해당 함수 안에 변수는 로컬 변수 매개변수
    print("foo's X=",x , id(x))
    def bar():
      a = 30 # L에 해당
      print( a, x, y ) # 각 변수는 L, E, G에 해당
    bar()
    x = 40
    bar()
def test():
    x=2000  # L local 로컬변수 우선 순위를 가지고 있다.
    print("test's X=", x, id(x))


if __name__ == '__main__':

    foo()
    test()
    print('x=',id(x)) # test() 안에 이는 x(로컬)와 밖에 있는 x(글로벌) 다른 x이다. 자기 방에 있으면