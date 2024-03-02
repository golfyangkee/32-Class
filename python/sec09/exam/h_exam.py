# 숫자를 입력받아 음수일 경우 예외를 발생하자
import sys

class U_exception(Exception):   # () 안에 Exception 있던 없던 파이썬은 실행된다. 파이썬만 다른 프로그램은 안됨
    pass

if __name__ == '__main__':
    try:
        a = int(input("input number : " ))
        if a<0:
            raise U_exception("0보다 작잖아")
        raise U_exception("연습용")    # raise는 생성될 클래스인 BaseException() 객체를 상속받는 클래스를 생성한다.
        # raise 키워드가 뒤에오는 애들은 전부다 객체를 class 생성해서 무조건 Exception이랑 연결시켜줌
    except U_exception as e:
        print("~~~~~~~~~~~~~~~~~~~~",e, e.args)
        print(e.args)
        print("예외 유형 " , sys.exc_info()[0])
        print("예외 인스턴스 객체 ", sys.exc_info()[1])
        print("예외에 대한 traceback = stackframe ,호출내용  ", sys.exc_info()[2])
        print("예외  원래 traceback 예외 e와 연결하는 사용하는 내용")
        e.with_traceback(sys.exc_info()[2])
