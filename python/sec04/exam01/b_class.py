'''
 name    kor     eng     mat      => Score
홍길동     90      80      70      => s1
정길동     50      60      70      => s2
이길동     100     100     100     => s3
'''

class Score:
    def __init__(self,name,kor,eng,mat):    # 객체를 생성할 때 값을 받으면서 방을 생성하겠다. (초기값을 자동으로 생성하지 않고 받아서 초기화)
        self.name=name
        self.kor=kor
        self.eng=eng
        self.mat=mat

if __name__ == '__main__':
    s1=Score('홍길동',90,80,70)
    s2=Score('정길동',50,60,70)
    s3=Score('이길동',100,100,100)

    print(f's1 = {s1.name} {s1.kor} {s1.eng} {s1.mat}')
    print(f's2 = {s2.name} {s2.kor} {s2.eng} {s2.mat}')
    print(f's3 = {s3.name} {s3.kor} {s3.eng} {s3.mat}')