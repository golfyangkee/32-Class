class Test02:
    def __init__(self,a=0, b=0):    # 지역변수 초기값으로 설정
        print('명시된 값을 받는 생성자야', a,b)

class Test03:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def __repr__(self):
        return f' a={self.a} b={self.b}'

if __name__ == '__main__':
    Test02()    # a=0,b=0 출력을 했으면 좋겠다. 빈방이었으면 좋겠다.
    Test02(100) # a=100, b=0 값을 한개 주는 방
    Test02(50,50)   # a=50, b=50    값을 두개 주는 방 만들고 싶다.
    print("=====================")
    print(Test03())               #a=0 b=0
    print(Test03(100))            #a=100 b=0
    print(Test03(50,50))    #a=50 b=50 -> 그래서 계속 다시 처음값으로 돌아간다.
    t1=Test03() # 주소를 알려준다는 거는 참조관계가 되어서 변경할 수 있게 된다. CRUD 할 수 있다.
    t1.a=1000
    print(t1)
    print(Test03())