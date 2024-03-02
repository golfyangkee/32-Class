import sys

def  case01():          # t1=Score()
    try:                # 나는 ZDE를 가져가다 ZDE=Zero~Erro() 빈방을 만드려고 했는데 'division by zero'로 받음
     res  = 10/0
     # pvm이 traceback이 했을 때 sys_infor_로 확인했는데
     # ZDE=ZeroDivisionError('arg: division by zero') 로 생성을 해서
     # 에러 발생 시 프로그램 중단 콘솔에 출력하려는 거를 except가 받음
    except  ZeroDivisionError as  ZDE  : #pvm에서 Error의 종류에 해당하는 클래스를 생성해서 리턴되는 것을 except에서 해결한다
        print(" 0으로 나누려고 했잖아 예외처리 부분", ZDE.args, ZDE) # ('division by zero',) division by zero
    else :
        print("else 예외가 나지 않을 경우 실행하는 부분")
    finally:
        print("오류 상관없이 반드시 수행할 명령  : 백업파일, 디비close() , 로그아웃  ")

    print( "===========case01 만줄 ============")

def case02():
    L= [1,2,3]
    try:
        num = L[4]
    except IndexError as IE:    # 하나의 try에 여러개의 except를 줄 수 있다. except Error를 안 적으면 어떤 에러일 지 알 경우 except만 씀
        print("list index out of range" )  # IndexError  : list index out of range
        print("IE =============> ",  IE , type(IE)) #  에러 메세지 IE.__str__() 이 실행
        # IE.with_traceback("abc") # with_traceback : 추적 실행 // 추적한 내용을 출력한 것
        tb = sys.exception().__traceback__
        # import sys 해서 dir() 안에 sys 넣고 dir(sys)에 exception 있고 dir(sys.exception) 안에 __traceback__ 있음
        print(tb, type(tb))   # 객체의 주소
        num = L[0] #예외 처리
    else :
        print("else")
    finally:
        print("오류 상관없이 반드시 수행할 명령  : 백업파일, 디비close() , 로그아웃  ")
    print(num)

if __name__ == '__main__':
    case02()