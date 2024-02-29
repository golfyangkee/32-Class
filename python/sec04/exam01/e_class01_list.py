'''
a,b라는 변수를 Test라는 이름의 자료형을 등록하고 싶다.
선언 -> 객체생성 -> 멤버호출 (값 전달 및 변경 리턴)
    a       b       --------------- Test
    100     200     t1 레코드 방
    300     400     t2 레코드 방
    500     600     t2 레코드 방
'''
class Test:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def __repr__(self):
        return f'{self.a} {self.b}'

if __name__ == '__main__':

    t1=Test(100,200)
    t2 = Test(300,400)
    t3=Test(500,600)
    print(t1.__repr__())
    print(t2)
    print(t3)
    print(dir(t1))
    print("===================case01. 객체 배열 _ 시퀀스형============================")
    test_all = [Test(100,200) , Test(300,400), Test(500,600)]
    print(test_all[0], test_all[1], test_all[2])    # 인덱스 명시 호출
    for res in test_all:    # 반복을 이용해서 전체 출력
        print(res)

    print("===================case02. 리스트 언팽킹============================")
    test_all = [Test(100, 200), Test(300, 400), Test(500, 600)]
    print(*test_all)    # 리스트 애들을 풀었다. 언팩킹한다고 한다. 프린트로 터플을 푸는 건 되는데 그냥 *test_all은 안된다.

    print("===================case03. 람다식 ============================")
    test_all02 = [Test(100, 200), Test(300, 400), Test(500, 600)]
    '''
    for res in test_all: #반복 전체 출력
        print(res)
    '''
    list(map(lambda res02: print(res02), test_all02))

    print("===================case04. 람다식 _ 번외편 ============================")
    my_array = [1,2,3,4,5,6,7,8,9,10]
    list(map(lambda ar : print(f'{ar*2}', end='\t'), my_array))