from functools import  singledispatch   # 함수의 오버로딩을 만드는데 사용하는 것
'''
이런 기능을 오버로드라고 한다.
함수는 1개 인데 객체 안 줬을 때, 하나 줬을 때, 두개 줬을 때 어떻게 작용하는 지 다 정의
def A():
    pass
def A(a):
    pass
def A(a,b):
    pass

def A(a=0,b=0):
    pass
이런 식으로 함축해서 쓰기도 한다.
'''
@singledispatch
def  my_data(data) :
    print("Error")

@my_data.register
def _(data :int, t :int):
    print(" int  " , data , t)
@my_data.register
def _(data :str):
    print(" str  " , data)
@my_data.register
def _(data:list):
    print("list" , data)

if __name__ == '__main__':
      my_data(10 ,100)
      my_data("abc")
      my_data([1,2,3,])
      my_data(90.9)
