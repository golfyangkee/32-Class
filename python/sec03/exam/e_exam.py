from functools import reduce

def my(x):
    return x*2
def test01_map():
    numbers = [1,2,3,4,5]
    res = map(lambda x : x*2, numbers)
    # res = map(my, numbers)
    print(list(res))

def my02(x):
    if x % 2 == 0:
        print(x)
        return x
def test02_filter():    # 조건을 줘서 트루인 애들만 리턴
    numbers = [1,2,3,4,5]
    res = filter (lambda x : x % 2 ==0, numbers)
    # res = filter(my02,numbers)
    print(list(res))

def my03(x,y):
    return x*y
def test03_reduce():    # 왼쪽에서부터 오른쪽으로 매개인자 2개 만나서 진행
    numbers = [1,2,3,4,5]
    res = reduce(lambda x,y: x*y, numbers)  #((((1*2)*3)*4)*5)
    print(res)

if __name__ == '__main__':
    test01_map()
    test02_filter()
    test03_reduce()