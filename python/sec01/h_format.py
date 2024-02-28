#print("출력서식")  -> page 40 
import datetime  # 날짜 시간 모듈
import math

def case01():
    #정수%d %o %x, 실수%f, 문자열%s 각 10자리씩 출력해보자.
    print("%10d %5d"%(100 , 200) )  #전체 정수 10자리 확보 후 100을 출력 , 5자리 확보후 200  
    print("%-5d %5d %5.1f"%(1,2,3.88888))   # 1정수 5자리 확보 후 왼쪽정렬, 2정수 5자리 확보 후 출력, 전체 5자리 확보 후 소수 이하 한자리
    print("%10s : %10s "%("aaaaaa","bbbbbbbbbbbbbbbbbbb"))  # bb... 은 값을 우선하기에 10자리로 짜르는게 아니라 전체 값이 다 나온다.
    ##  정수, 8진수, 16진수
    print("%d %o %x %5f"%(100,100,100,3.14)) #소수점 기본정밀도 자리가 출력 어제 sys에 가서 확인함

def case02():
    #str's format ->  S.format(*args, **kwargs) -> str
     print("{0} {1}".format( "apple", 7.77 ) )  #apple 7.77
     print("{1} {0}".format( "apple", 7.77 ) )  #7.77 apple
     print("{0} {0}".format( "apple", 7.77 ) )  #apple apple
     print("{0:^10s} {1:20f}".format( "apple", 7.77 ) ) #  apple      7.770000      10f
                                                              #  apple                7.770000  220f
     print("a={1} b={1} c={1}".format("apple", 7.77))
 
def case03():
    #str.format() 정수활용해 보자 . 
    num =42
    num01=100
    f= "The number is {} {}".format(num,num01)          # {} 없으려면 다 없고 있으려면 다 있고
    f1= "The number is {0} {1}".format(num, num01)
    print(f)    # print는 기본 표준 출력 장치가 커맨드(모니터)임
    print(f1)

def case04():
    #str.format() 실수활용해 보자 . 
    pi=3.14159
    f= "The number is {: .2f}, {:}".format(pi, math.pi) # import math해서 math.pi 호출해본다.
    print(f)
    
def case05():
    #str.format() 제로패딩 활용해 보자 . -> 용도: 수치 데이터를 가져다가 저장대상(파일)이 있고 빈칸은 0으로 채워서 저장하고 싶을 때
    # 년월일 자리수 맞추던가 금융권에서 제로패딩 수치를 가지고 와서 내가 원하는 자리에 채우고 나머지는 0으로 채우고 싶을 때 제로패딩하는 법 zfill()
    # 2진화 -> 10진화 방법 : bin(value) -> int(bin(value, base=0))
    num =42
    f= "The number is {:010d}".format(num)
    print(f, type(f))

    f= "Binary is {:08b}".format(num)    # b -> 101010   // 08b -> 00101010 // bin(42) -> 바이너리타입(0b~)으로
    print(f, type(f))
    
    # bin(10) -> 0b1010
    # int(bin(10)) -> error 왜냐하면 base=10으로 되어 있어서?
    # help(int) 하면 int([x]) -> integer   int(x, base=10) -> integer  이렇게 설명됨
    # int(bin(10), base=0) or int(bin(10), 0) 으로 해줘야 10이 나옴
    # int('0b1010', base=0) or int('0b1010', 0) 으로 해줘야 10 나옴
    
def case06():  
    #날짜서식 date(year, month, day) --> date object
    date  = datetime.date(2023,11,9)
    f= "Date : {: %Y-%m-%d}".format(date)   # Y는 대문자 m은 소문자 d는 소문자
    print(f,  date) #Date :  2023-11-09 2023-11-09
    print("today=", datetime.datetime.today())  #today= 2023-11-09 11:10:23.669503
    print('==========today()를 가지고 {: %Y-%m-%d}으로 출력을 해보자=============')
    m= datetime.datetime.today()
    res = "Date : {: %Y-%m-%d}".format(m)
    print(res)
    '''
    datetime 모듈에 datetime 클래스의 today 함수 now(각 국가별의 시간) 함수 구분 (timezone에 따라 달라진다.)
    1. datetime.datetime.today() : 현재 로컬기반으로 datetime객체를 리턴한다. (로컬 시간대 적용)
                                    - 로컬시간대와 상관없이 사용된다.
    2. datetime.datetime.now() : 현재 로컬기반으로 datetime객체를 리턴한다. (컴퓨터 시간대(현지시간) 적용)
    '''

def case07():
    #튜플/터플 -> *
    point=(1,2,3,4)
    point01 = (11, 22, 33, 44)
    f= "Point: (  {},{},{},{} ) Point01: ( {},{},{},{} )".format(*point,*point01)
    print(f)    
'''
a,b,*c = 1,2,3,4,5,6,7   * 마지막을 다 받겠다 라는 의미라서 *c, *d 이렇게 못 씀
a=1; b=2; c= [3,4,5,6,7]
type(c) = class 'list'

a,b,*c = 1,2,(3,4,5,6,7)
a=1; b=2; c= [(3,4,5,6,7)]
type(c) = class 'list'

*a = 1,2,3,4,5
a = error
*a = [1,2,3,4,5]
a = error
'''
def case08():
    #사전형dict **  
    person={'name':'홍길동' ,'age77':20}
    f="person : Name:{name} , age:{age77}".format(**person)
    print(f)

def case09():
    #인수위치  
    f=" {2} {0} {1}" .format(1,2,3)
    print(f)
       
if __name__ == '__main__':
    case09()




