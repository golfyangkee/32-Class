def test():
    def my_inner():
        return 100
    return my_inner # 주소 넘김
def test01(a):
    b = [1,2,3,4,5]
    def my_inner(): # a를 여기서 선언을 하던 밖에서 하던 똑같이 local 변수이다.
        return 100*a + b[a]
    return my_inner

def quadratic( a, b, c ):
    cache = {}
    def f( x ):
        if x in cache:
            return cache[x]
        y = a * x * x + b * x + c
        cache[ x ] = y
        return y
    def mytest():
        return 9999
    return f

if __name__ == '__main__':
    '''
    
    res=test        # 주소 넘김
    print(res())    # 주소 프린트
    print(res)
    print(test01(3))    # 주소 프린트
    '''

    f1=quadratic(3,-4,5)    # mytest 주소 넘어감
    print(f1)
    print(f1(3))
    '''
    print("=================================")
    print(f1.__closure__,"------>", type(f1.__closure__))
    print(f1.__closure__[0])
    print(f1.__closure__[1])
    print(f1.__closure__[2])
    print(f1.__closure__[3])
    '''
    print("=================================")
    res=[cell.cell_contents for cell in f1.__closure__]
    print(res, type(res)
          )