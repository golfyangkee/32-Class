''''
   1. com.test.MyScore :
       Score   : 이름 국어 영어  총점 평균 출력 메소드
       MyScore  :Score를 상속받아  3과목을 총 평균

    2. MyClass04에서 호출을 해서 객체 배열을 만들어서 접근해 보자.
'''
from com.test.MyScore import  *

if __name__ == '__main__':
    my_list  =  [MyScore ('홍길동1' ,100,100,100) , MyScore ('홍길동2' ,90,90,90),MyScore ('홍길동3' ,80,80,80)]

    #홍길동1의 국어점수를 50을 변경후 전체 출력해보자
    for res  in my_list:
        if res.getName() =='홍길동1':
            res.setKor(50)
            print(res)
        else:
            print(res)
