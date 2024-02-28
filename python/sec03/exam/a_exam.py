
def My():
    print("0000")
    return 100 # return은 함수가 사용하는 종료 키워드 break continue는 제어문이 사용하는 키워드
    print('000')    # 이게 들어가도 return에서 이미 함수가 끝나서 출력되지 않는다.

def MyTest(a,b,c,d):
    # 매개인자의 초기값이 없는 함수를 선언해서 호출할 경우 반드시 순서 및 변수명을 호출해서 값 대입
    print(a,b,c,d)

def MyTest02(a=10,b=2,c=0,d=33):
    # 초기값이 있을 경우 값 전달 없이 호출해도 된다.
    # 외부에서 () 안에 값을 1개를 주든 계수 개수가 안 맞아도 무조건 채워준다는 의미로 오버로드할 수 있다
    print(a,b,c,d)

def MyTest03(a,b=2,c=0,d=33):
    # 초기값이 있을 경우 값 전달 없이 호출해도 된다.
    # 외부에서 () 안에 값을 1개를 주든 계수 개수가 안 맞아도 무조건 채워준다는 의미로 오버로드할 수 있다
    print(a,b,c,d)

if __name__ == '__main__':
    # print(My()) -> None My(): pass 가 리턴하는 게 없을 때
    # print(My()) -> None My(): return 가 줄게 없을 때
    # print(My())     # My()를 호출하게 되면 100을 리턴해서 출력하게 된다.

    # MyTest(1,2,3,4)
    # print(MyTest(1,2,3,4)) 하면 1 2 3 4 프린트하고 줄게 없어서 None 도 같이 나온다.
    # MyTest(b=2,a=1,c=3,d=4)
    # 계수가 갯수가 맞아야 하고, 혹은 변수명이 정확하게 맞아야 한다.

    MyTest02(100)               # 100 2 0 33
    MyTest02()                  # 10 2 0 33
    MyTest02(100,200)     # 100 200 0 33
    MyTest02(a=1,d=3)           # 1 2 0 3

    # MyTest03() -> error  너 a 값 줘야해! 해서 에러난다.

