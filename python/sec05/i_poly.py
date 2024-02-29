from sec04.exam03.Mycalc import Calc


if __name__ == '__main__':
     #c1 = Calc(100,50)
     #print(c1)

     mlist =[Calc(100,50),Calc(200,150),Calc(300,250)]
     print("=== 1. 전체 출력 ===")
     for x in mlist:
          print(x)

     print("=== 2. a의 값이 100인 값을 찾아서 777 바꾼 후 출력 하자 ===")
     mlist=list(map(lambda x : Calc(777, x.b) if x.a==100 else x, mlist ))
     for x in mlist:
          print(x)
'''
     for res  in mlist:
          if res.get_a() == 100:
               res.set_a(777)
               print(res)
          else:
               print(res)
'''
     print('=== b 값이 150인값을 찾아서 888  바꾼 후 출력 하자 ===')
     mlist = list(map(lambda x : Cal(x.a,888) if x.b == 150 else x. mlist))
     for x in mlist:
          print(x)

    '''
     for res  in mlist:
          if res.get_b() == 150:
               res.set_b(888)
               print(res)
          else:
               print(res)
'''

