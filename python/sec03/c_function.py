from functools import partial #부분함수 , 함수분할(기능별 분할은 아니고)  functools는 고차함수를 가지고 있다.
# Map(), Reduce() -> MR작업하는 거 물어봄 -> 데이터 분리하는 거
# 분할 이유: 코드가 길거나 연산이 너무 복잡해서 단문은 의미가 없고 적어도 7~8줄 정도 함수는 7줄 이상이 되면 좀 더 빨리 돌아가서 단문이면 긴줄 함수보다 소요시간이 더 걸릴 수 있다.
#정보를 가져다가 저장하는건 매니패스트, 코드를 가져다가 속성을 추출하는 거는 리플렉션이라고 한다. 다른 프로그램은 리플렉션이 있는데 파이선은 속성으로 관리한다.
# 코드객체는 컴파일에 모여있다.

#함수의 원본
def power(base, exponent):
    return base ** exponent

#함수의 원본
def multiply(a, b):
    return a * b

if __name__ == '__main__':
              #partial(func, *args, **keywords)
    square = partial(power, base=2) #square 함수가 생성된다.
    print(square )
    result = square(exponent=3)
    print(result)
    #------------------------------------------#
    my_partial  =partial(multiply,5)   #부분함수 생성 a= 5
    result  = my_partial(3)  # b= 3 #원래 함수를 호출하게 된다.
    print(result)
