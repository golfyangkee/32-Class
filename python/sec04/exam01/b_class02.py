'''
 name    kor     eng     mat      => Score
홍길동     90      80      70      => s1
정길동     50      60      70      => s2
이길동     100     100     100     => s3
'''
# 클래스를 선언하게 되면 모든 클래스의 수퍼인 Object의 자식이 되어 기능 및 변수 등을 상속받게 된다.
class Score:    # Score(object)가 숨어 있다. 클래스에서 멤버는 self가 있는 애들. self가 있어야 올 수 있다
    def __init__(self,name,kor,eng,mat) -> None: #def __init__(self,a,b,c,d):해도 됨 저게 원형임
        # 객체를 생성할 때 값을 받으면서 방을 생성하겠다. (초기값을 자동으로 생성하지 않고 받아서 초기화)
        self.name=name
        self.kor=kor
        self.eng=eng
        self.mat=mat

    def __repr__(self) -> str:  # 재 정의 내가 준 값을 가져다가 그대로 출력 , 실행할 때마다 값이 같음 , 랜덤값에는 안 씀
                                # def __repr__(self): 이렇게 해도 됨 저게 원형임

        return f'name={self.name} kor={self.kor} eng={self.eng} math={self.mat}'

if __name__ == '__main__':
    s1=Score('홍길동',90,80,70)
    s2=Score('정길동',50,60,70)
    s3=Score('이길동',100,100,100)

    print(s1)   # __repr__없이 하면 선조 주소 호출된다. == print(s1.__repr__) 같음
    print(s2)
    print(s3)