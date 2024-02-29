#두 수(a,b)를 받아서 4칙연산을 구현하는 클래스를 만들고 싶다.
class Calc:
    def __init__(self, a=0,b=0):
        self.a=a
        self.b=b
    def getHap(self):
        return self.a + self.b
    def getSub(self):
        if self.a>=self.b:
            return self.a - self.b
        else:
            return self.b - self.a
    def getMul(self):
        return self.a * self.b
    def getDiv(self):
        if self.a>=self.b:
            return self.a / self.b
        else:
            return self.b / self.a

    def __str__(self):
        return f'{self.a}+{self.b}={self.getHap()} \n' +    \
               f'{self.b}-{self.a}={self.getSub()} \n' +    \
               f'{self.a}*{self.b}={self.getMul()} \n' +    \
               f'{self.b}/{self.a}={self.getDiv()} \n'
# 계산기에는 출력은 출력 대로
# 합이랑 빼기 등 계산은 다 나누어져 있어야 한다.

if __name__ == '__main__':
    cm = Calc(100,200)  # __init__
    print(cm)

'''
========결과==============
100+200=
200-100=
100*200=
200/100=

조건1] 각 4칙 연산의 메소드를 getHap(), getSub(), getMul(), getDiv()로 설정하고 구현한다.
조건2] __str__()에 전체 출력문을 구현하고 cm의 객체를 호출했을 때 출력되도록 아웃풋을 구현한다.


'''