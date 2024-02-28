def my():
    return 100

def test01():
    # def my(): return 100
    res = lambda : 100
    print(res)
    print(res(), type(res))

def my01(x):
    return 100+x
def test02():
    #def my01(x): return 100+x
    res = lambda x : 100+x
    print(res(3))
    pass

def my02(x,y,z):
    return x+y+z
def test03():
    res = lambda x,y,z: x+y+z
    print(res(3,5,9))
    pass

def my03(x):
    return x
def test04():
    my_list = [1,2,3,4,5]
    res = lambda x:x
    print(res(my_list))

def my04(x):
    return x

def test05():   # x의 값 중 짝수만 리턴 해보자.
    my_list = [1,2,3,4,5]
    even_res = lambda x : [ x for x in my_list if x%2==0 ]
    print(even_res(my_list))

if __name__ == '__main__':
    test05()