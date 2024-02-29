# 4) 상속관계를 통해서 후손을 통한 객체를 생성하고 후손의 객체를 통해서
#    선조의 메소드와 후손의 메소드를 자유롭게 호출할 수 있다.

from inspect import *

class 선조:
    def prn(self):  # 4 33
        print("선조의 Prn")    # 44
class 후손(선조):
    def prn(self):  # 3 5   22
        super().prn()   #   33
        print("후손의 Prn")    # 55
class Myclass(후손):
    def prn(self):  # 2 6
        super().prn()           # 11
        print("Myclass Prn")    # 66

if __name__ == '__main__':
    print("=========4. 후손을 통해 선조의 메소드를 호출해보자")
    a1=Myclass()    # 1 7 히든 처리되기에 다른 prn에는 멀 하든 나오지 않는다.
    a1.prn()    # 77

    print("1. 계층관계 : ", getmro(Myclass))
    print("2. 멤버 확인  :", getmembers(Myclass))
    print("3. 모듈파일확인  :", getfile(Myclass))
    print("4. 모듈 확인  :", getmodule(Myclass))
    print("5. 소스확인 :", getsource(Myclass))