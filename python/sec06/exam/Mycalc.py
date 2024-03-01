from dataclasses import *

# 두수(a,b)를 받아서 4칙연산을 구현하는 클래스를 만들고 싶다.
def make_dataclass(cls_name: 'Calc',
                   fields: [('a',int,0),('b',int,0)],
                   namespace= {
                        'getHap':lambda self: self.a+self.b,
                        'getSub':lambda self:self.b-self.a,
                        'getMul':lambda self: self.a*self.b,
                        'getDiv':lambda self: self.b/self.a,
                        '__str__': lambda self: f'{self.a}  + {self.b}  = {self.getHap()} \n' +  \
                                                f'{self.b}  - {self.a}  = {self.getSub()} \n' +  \
                                                f'{self.a}  * {self.b}  = {self.getMul()} \n' +  \
                                                f'{self.b}  / {self.a}  = {self.getDiv():5.1f} \n'
                   })
if __name__ == '__main__':
    cm  = Calc(100,200)  # __init__
    print(cm)
    print(repr(cm))
    print(helf(make_dataclass))