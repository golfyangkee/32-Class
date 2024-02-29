''''
   1. com.test.MyScore :
       Score   : 이름 국어 영어  총점 평균 출력 메소드
       MyScore  :Score를 상속받아  5과목 국어, 영어, 수학, 음악 체육 (MUs, PE)을 총, 평균, 학점

    2. sec04.exam03.Score에서 호출을 해서 객체 배열을 만들어서 접근해 보자.
'''
from sec04.exam03.Score import  *

class MyScore(Score):
    # 1. 생성자로 매개 인자 받아 선조에게 전달
    def __init__(self,name,kor,eng,mat,scn,mus):
        super().__init__(name,kor,eng,mat)
        self.scn=scn
        self.mus=mus
    # 2. getTot() 재 정의
    def getTot(self):
        return (super().getTot()+ self.scn+self.mus)    # 선조의 3과목 총점 + 내꺼 2과목
    def getAvg(self):
        return self.getTot() / 5    # 내꺼 5과목의 총점 / 5

    # 3. __str__ 출력
    def __str__(self):
        return (f'{self.name:<5} \t {self.kor:5d} \t {self.eng:5d} \t {self.mat:5d} \t {self.scn:5d} \t {self.mus:5d}'
                f' |super: {super().getTot()} self: {self.getTot()} '
                f' |super: {super().getAvg():5.1f} self: {self.getAvg():5.1f}'
                f' |super: {super().getGrade()} self: {self.getGrade()}')

if __name__ == '__main__':

    my_list  =  [MyScore ('홍길동1',100,100,100,100,100),
                 MyScore ('홍길동2',90,90,90,90,90),
                 MyScore ('홍길동3',80,80,80,80,80)]

    list(map(lambda x : print(x), my_list))