'''
홀수인 경우: 어떤 정수 n에 대해서, n % 2의 결과가 1이면, n은 홀수
짝수인 경우: 어떤 정수 n에 대해서, n % 2의 결과가 0이면, n은 짝수
정수의 배수: 어떤 정수 n에 대해서, n % 배수의 결과가 0이면 n은 해당 숫자의 배수이다. n % 5 == 0이면 n은 5의 배수이다.
'''

def Test():
    # 홀수는 반복하러 가고 짝수는 출력해줘
    for i in range(10):  #0 ~  9    range(stop)
        if i % 2 != 0:  # i를 2로 나눈 나머지가 0이 아닌 경우
            continue    # 반복을 계속 하자.
        print("%5d"%i,end="")

def Test01():   # 1~101까지 짝수만 출력해보자
    for i in range(1,102):
        if i%2==0:
            print("%5d"%i, end = ' ')

def Test02():   # 1~101까지 3의 배수만 출력해보자.
    for i in range(1, 102):
        if i % 3 == 0:
            print("%5d"%i, end = ' ')

def Test03():   # 1~101까지 2의 배수이면서 (and) 3의 배수를 출력해보자.
    for i in range(1, 102):
        if i % 2 == 0 and i % 3 ==0:
            print("%5d"%i, end = ' ')

def Test05():   # 1~101까지 2의 배수이면서 5의 배수를 출력하고 개수를 출력해보자.
    list1 = []
    for i in range(1, 102):
        if i % 2 == 0 and i % 5 == 0:
            print(i, end=' ')
            list1.append(i)
    else:
        print(f"list1={len(list1)}, value = {list1}")
    '''
    내가 프린트 한거
    print(list1)
    print(len(list1))
    '''

def Test04():   # 쌤이랑 Test04 문제 푼거
    count = 0
    for i in range(1, 102):
        if i % 2 == 0 and i % 5 == 0:
            count = count+1
            print(i, end=' ')
    else:
        print("cnt=", count)

if __name__ == '__main__':
    # 1. 각 함수를 dict에다가 지정한다.
    functions = {'1':Test01,
                 '2':Test02,
                 '3':Test03,
                 '4':Test04,
                 '5':Test05}
    # 2. input으로 입력 받는다.
    fun_num=input("함수1~5에 해당하는 번호를 입력해라 : ")
    # 3. 입력받은 함수명으로 실행한다.
    if fun_num in functions:
        functions[fun_num]()    # 해당 함수 실행 ()가 있어야 실행이 된다.
    else:
        print("없는 함수명이야")