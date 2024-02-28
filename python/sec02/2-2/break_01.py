def Test():
    for i in range(1,10):
        if i > 5:
            break
        print("%5d"%i,end="")
    else:
        print("~ else ~") # 안 나오는 게 정상 break 했으니까 for문을 탈출한다는 의미 제어문 탈출

    print(" outter = %5d"%i,end="")


def Test01():
    for i in range(1, 10):
        if i > 3:
            continue    # 반복을 계속하자 4부터는 for문 처음으로 가라
        print("%5d" % i, end="")
        print("//")

    print(" outter = %5d" % i, end="")
    '''
    1   출력 
    2   출력
    3   출력
    4   위로 -> 컨티뉴
    5   위로 -> 컨티뉴
    6   위로 -> 컨티뉴
    7   위로 -> 컨티뉴
    8   위로 -> 컨티뉴
    9   위로 -> 컨티뉴 -> 반복 끝(레인지 끝남)
    
    '''

def Test02():
    for i in range(1, 10):
        if i > 5:
            print(f"\n{i}>5~~~", end=' ')
            continue
        print("%5d" % i, end="")
    else:
        print("\n=====else======")

    print(" outter = %5d" % i, end="")

if __name__ == '__main__':
    # print(Test01()) -> outter =     9None
    # return이 없는 함수를 호출해서 출력할 때 None 라고 한다.
    Test02()
