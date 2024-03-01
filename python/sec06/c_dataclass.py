from  dataclasses import *
#__init__  / __repr__   을 줄여놓은게 어노테이션?
@dataclass      # 초기화, 출력
class Person:
    name :str   # 멤버 변수 초기화 및 출력 __init__(self,name,age): ~~
    age :int

##################################################
'''
def make_dataclass(cls_name: str,
                   fields: Iterable[str | tuple[str, type] | tuple[str, type, Field]],
                   *,
                   bases: tuple[type, ...] = ...,
                   namespace: dict[str, Any] | None = ...,
                   init: bool = ...,  재정의 함수
                   repr: bool = ...,  재정의 함수
                   eq: bool = ...,    재정의 함수
                   order: bool = ...,
                   unsafe_hash: bool = ...,
                   frozen: bool = ...) -> type
'''
C = make_dataclass('C',
                   [('x', int),                     # 1
                     'y',                                 # 2
                    ('z', int, field(default=5))],        # 3
                   namespace={'add_one': lambda self: self.x + 1}, )


if __name__ == '__main__':
     c=C(10,'python')  # C(x=10, y='python', z = 5 )
     print(c.x)
     print(c.add_one())
     print(c)

     p=Person("홍길동",10)
     print(p)