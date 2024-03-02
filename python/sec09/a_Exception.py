# 예외라고 하는 거는 문법은 멀쩡하나 런타임 시에 발생되는 프로그램의 중단 지점에 pvm에 Traceback을 생성시켜 중단이유를 알려줌

# 예외가 발생되면 pvm 해당 에러의 종류를 확인하고 확인된 객체를 생성해서 에러가 난 시점으로 리턴한다.
# 1. 개발자는 예외가 발생한 위치를 확인하고 try ~ except 구문을 작성한다.
# 2. except 구문에서 예외를 처리한다.
if __name__ == '__main__':
    a=10
    b=0
    res=0
    try:
        res=a/b
        print("========만줄의 코드========") # 에러가 나오니 바로 except 로 넘어가서 안 나옴
    except ZeroDivisionError as zd:
        # 예외를 처리하는 부분
        print(str(zd))
        print(zd)
        print(f'{a}/{b}={res}')
    print("========222만줄의 코드========")