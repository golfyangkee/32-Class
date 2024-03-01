from abc import abstractmethod, ABCMeta

class AA(metaclass=ABCMeta):
    @abstractmethod             # 무조건 재정의!!!!
    def prn(self):              # 보통 재정의를 원칙으로 하기에 내용이 필요없다. 추상매소드에 내용을 적지 않는다.
        pass
class BB(AA):
    def prn(self):
        print("BB's method")

'''
class DD(AA):
    def Prn(self):              # 재정의 안 하면 추상클래스가 된다. -> 객체 생성 불가
        print("DD's method")
'''

def my_call(res:AA):
    res.prn()

def test(a:int):    # 데이터 타입을 명시 // a의 형을 명시하는 거다. 넘어오는게 int만 받겠다라는 의미
    pass

if __name__ == '__main__':
    #my_call(AA())  추상클래스라서 객체 생성 불가능해서 오류 뜸
    my_call(BB())
    #my_call(DD())  Can't instantiate abstract class DD without an implementation for abstract method 'prn'