'''
 name    kor     eng     mat      => Score
홍길동     90      80      70      => s1
정길동     50      60      70      => s2
이길동     100     100     100     => s3
noname     0       0       0      => s4
박길동     0       0       0      => s5
'''

class Score:
    def __init__(self,name='noname',kor=0,eng=0,mat=0):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.mat=mat

    def __repr__(self) :
        return f'name={self.name} kor={self.kor} eng={self.eng} math={self.mat}'

if __name__ == '__main__':
    s1=Score('홍길동',90,80,70)
    s2=Score('정길동',50,60,70)
    s3=Score('이길동',100,100,100)
    s4=Score()
    s5=Score('박길동')
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)