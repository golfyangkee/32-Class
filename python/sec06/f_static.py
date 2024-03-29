
class Test:
    my = 0      # 전역변수
    @staticmethod           # staticmethod는 self 가 없다. 영역이 달라서
    def get_hap(a,b):
        return a+b
    @classmethod
    def get_mul(self,a,b):
        return a*b

    @classmethod
    def get_mul02(cls,a,b):   # 상속 시 클래스 간의 다형성을 유지하자. (팩토리 패턴 : 팩토리 메소드를 사용하자.) 자유다.
        print(f'클래스 메소드 {cls.my}')
        return a*b

if __name__ == '__main__':
    print(Test.get_hap(10,10))
    print(Test.get_mul(10, 10))

    #호출은 되지만 영역은 다르게 바운드 되고  Test.get_hap(10,10) 생각하고 컴파일된다.
    t1  = Test()
    print(t1.get_hap(1,2))    # X