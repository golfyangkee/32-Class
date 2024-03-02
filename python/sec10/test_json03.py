import json
def prn01():
    # data.json  파일을   read() 해 보자.
    print('======첫번째 방법========')
    with open('data.json', 'r')  as f:  # default = r이다
        s = f.read()
        print(s, type(s))
    # 그대로 읽어가지고 온다.
    print('======두번째 방법========')
    result = json.load(fp=open('data.json', 'r'))
    print(result)
    # 자동으로 디코더해서 원래대로 가지고 온다.
class Student:  #객체 생성
    def __init__(self, data):  #생성자로 넘어온 대입된 데이터
        self.__dict__= data    #dict로 대입
        print(self.__dict__)
def prn02():
    '''
    1. json 모듈을 사용해서 STUDENT.json을 읽어오자.
    2. Object_hook Student 클래스를 만들어서 데이터를 대입한다.
    3.  파일을 오픈된 파일 read()를 이용해서 출력을 먼저 해본다.
    4. 이름  : 총점  으로 출력한다.
       ex) RuRe  :  270 점
    '''
    # f = open('STUDENT.json', 'r')
    # str = f.read()
    # print(str)
    # f.close()
    # data = json.loads(str, object_hook=Student)
    # 일반파일을 읽어서 일반파일 내용을 loads한테 주면 클래스 객체로 들어가서 키 밸류로 리턴을 해준다.
    #--------위 내용을 한줄로 표현하자 (위 방식 권장 X , 이 방식은 굳이 close 안 줘도 된다.----------
    data = json.load(fp=open('STUDENT.json', 'r'), object_hook=Student)

    for my in data.STUDENT:
        hap = my.SCORE.KOR + my.SCORE.ENG + my.SCORE.MATH
        print(my.NAME + ":%3d 점" % hap)
        # print(type(my))
if __name__ == '__main__':
    prn02()



















