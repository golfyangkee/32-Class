'''
 name    kor     eng     mat      => Score
홍길동     90      80      70      => s1
정길동     50      60      70      => s2
이길동     100     100     100     => s3
'''
class Score:
    def __init__(self,name,kor,eng,mat) -> None:
        self.name=name
        self.kor=kor
        self.eng=eng
        self.mat=mat
    def getTot(self):
        return self.kor + self.eng + self.mat
    def getAvg(self):
        return self.getTot() / 3
    def getGrade(self):
        if self.getAvg() >= 90:
            return 'A'
        elif self.getAvg() >= 80:
            return 'B'
        elif self.getAvg() >= 70:
            return 'C'
        else:
            return 'F'

if __name__ == '__main__':
    s1=Score('홍길동',90,80,70)
    s2=Score('정길동',50,60,70)
    s3=Score('이길동',100,100,100)
    print("이름 \t 국어 \t 영어 \t 수학 \t 합계 \t 평균 \t 학점" )
    print(f'{s1.name:<5} \t {s1.kor:5d} \t {s1.eng:5d} \t {s1.mat:5d} \t {s1.getTot()} \t {s1.getAvg():5.1f} \t {s1.getGrade()}')
    print(f'{s2.name} \t {s2.kor} \t {s2.eng} \t {s2.mat} \t {s2.getTot()} \t {s2.getAvg()} \t {s2.getGrade()}')
    print(f'{s3.name} \t {s3.kor} \t {s3.eng} \t {s3.mat} \t {s3.getTot()} \t {s3.getAvg()} \t {s3.getGrade()}')