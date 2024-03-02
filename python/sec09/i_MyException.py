class MyException(Exception):
    pass
def myPrn(a,b):
    if b== 0:
        raise MyException("0 이 잖아")
    return a/b

if __name__ == '__main__':
    try:
        res  =  myPrn(10,0)
        print(res)
    except MyException as e:
        print("Error  :", str(e))
        res = myPrn(10,100) # 목적이 있기 때문에 추후 작업까지(finally까지) 다 진행해야 한다.
    finally:
        print(res)
