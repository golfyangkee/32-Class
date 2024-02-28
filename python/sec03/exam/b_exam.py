
def myFunc(*a): # *a는 터플
    print(a)

def myFunc01(*a,b=10):
    # *a는 터플 터플 뒤에 오는 값 뒤는 초기값을 주는 게 에러를 막을 수 있다.
    # print(*args, sep=' ', end = '\n', file=None, flush=False)
    print(f'a={a} b={b}')

def myFunc02(*a,**d):    # print(*args, sep=' ', end = '\n', file=None, flush=False)
    print(f'tuple={a} dict={d}')

def myFunc03(*a,b=10,**d):    # print(*args, sep=' ', end = '\n', file=None, flush=False)
    print(f'tuple={a} b={b} dict={d}')

if __name__ == '__main__':
    '''
    myFunc01(1,2,3,4,5, b=100)
    myFunc01(1)
    myFunc02(1,2,z=100, y=200)
    mytuple=(1,2,3,4,5)
    mydict={'a':1, 'b':2}
    myFunc02(mytuple, mydict)  # *a에 다 들어감
    myFunc02(*mytuple,**mydict)    # * 로 구분
    '''
    myFunc03(1,2,3,4, z=100, y=200)
    # tuple=(1, 2, 3, 4) b=10 dict={'z': 100, 'y': 200} // b는 안 바뀜
    myFunc03(1, 2, 3, 4, b=4, z=100, y=200)
    # tuple=(1, 2, 3, 4) b=4 dict={'z': 100, 'y': 200}