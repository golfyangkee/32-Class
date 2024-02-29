#[Step 01:  클래스 선언 ]
class Test: # object의  후손 클래스가 되어 선조의 메소드들을 참조하고 있다.    object <- Test
    '''
    def __init__(self):
        pass 와 같은 진행이다.
    '''
    def empty(self):    # Test Class의 멤버함수
       self.data = []  #빈리스트 객체 선언 / 멤버변수

    def add(self, x):   # x 지역변수, Test 의 멤버함수
       self.data.append(x) #리스트에 요소를 추가한다.

if __name__ == '__main__':
#[Step 02:  클래스 객체 생성  ]
    my01 = Test()   #CRUD 관계
    my02 = Test()   #CRUD 관계

#[Step03 :  멤버 호출]
    my01.empty()    # 각 빈 리스트 생성
    my02.empty()    # 빈 리스트 새성
    for  i in range(1,6):  # my01에다가 요소를 1~ 5 append
        my01.add(i)

    # list 객체를  출력 해본다.
    print(my01.data)   #1~ 5 []가 출력
    print(my02.data)  #[]

    print(my01, my02) # 주소가 다르다. = 다른 객체 이다.
    my03= my01  # my03이라는 객체변수에 my01 주소를 대입해서 얕은 카피를 했다, 같은 공간을 참조한다.
    print(my03.data) #my01 동일한 값,   1~ 5 []가 출력
    print(my01, my03) # 각 주소를 호출해 본다. ?  -> 같은 주소가 나올까?

    my03.add(1000)
    print(my01.data, my01)
    print(my03.data, my03)
    del my01    #my01 삭제

    print("======삭제후============")
    #print(my01.data, my01) -> 이거 실행하면 오류뜸
    print(my03.data, my03)





