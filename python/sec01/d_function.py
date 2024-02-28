# return 유무 / () 안에 파라미터(매개변수)의 유무 에 따라 함수가 달라짐 4가지
# def userName():
#   명령
# return이 있으냐 없느냐 에 따라 함수가 달라짐 리턴 없으면 그냥 실행하는 함수
def Test():     # 함수 선언
    print("파이썬이야")  # default 값으로 end=\n이 끝에 있다.

def Prn():      # 함수 선언
    print("off합시다.")    # 함수는 함수 안에 또 다른 함수를 호출할 수 있다.


# print('aaaaa')   ----- 먼저 프린트됨

'''
if __name__ == '__main__':  # 만약에 __name__이 __main__ 이면 모듈의 실행 진입점  ---1
    Test()  # "파이썬이야"를 출력 -----2
    Test()  #  함수 호출        ------3
    Prn()   # "off합시다." 출력
'''

if __name__ == '__main__':  #   ----1 만약에 main이 name을 가지고 있다면 호출해서 쓰자.
    # 콜론모양이 있으면 블럭으로 먼가를 가지고 있다고 생각하자. py파일에 한번만 쓴다.
    # __name__은 보통 모듈 안에 들어가는 애들이 함수 변수 클래스 기타 등등 키워드들이 들어가서
    # 모듈 안에 멤버(상수, 함수, 클래스).py 등등의 이름을 기억하고 있다.
    # 가장 작은 단위의 이름을 기억.
    # main은 진입점 실행할 때 외부에서 값 받지 않고 그냥 스스로 실행 (모듈 실행)
    Prn()   #   ----2
    # 작업하다가 원래 이름을 가지고 싶을 때 t1.__name__ 검색해서 원래 이름을 알 수 있다.
    Test()  #   ----3