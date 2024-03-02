import traceback
def f1(a,b):
    return f2(a) + f2(b)

def f2(x):
    return  1.0/x

if __name__ == '__main__':
    try:
       f1(1.0,0.0)
    except (ZeroDivisionError , IOError) : # 여러개의 예외 클랙스를 () 터플로 묶어서 지정할 수 있다. //
        # 괄호로 묶는 거는 에러가 1개가 아니라 여러개 나올 수 있어서 , 는 or 이니까
        pass
        traceback.print_exc()   # 추적한 거 전체적으로 출력해줘 라는 의미
