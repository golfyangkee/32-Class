#산술연산
print( 10 + 2 )  
print( 10 - 2 ) 
print( 10 * 2 ) 
print( 10 / 2 ) 
print( 10 ** 2 ) 
print( 10 // 2 )  # 몫을 정수로 리턴, 가장 가까운정수로 내림 (음의 무한)
print( 10 % 2 )

print('// 연산자 번외편')
print( 10 // 3 )
print( 7 // 2 )  #3.5 
print( -7 // 2 ) #-3.5 : //연산자는 음의 무한대로 가장 가까운 정수로 내림한다.   

print(format(1.234567,"10.3f"))
print('{0}{1}'.format('apple',7.77))
print('{0:<10}{1:5.2f}'.format('apple',7.77))
print('{0:>10}{1:5.2f}'.format('apple',7.77))
print('{0:=^10}'.format('hi'))

import pprint

numbers = [[1,2,3], [4,5],[6,7,8,9]]
print(numbers)
print(*numbers)
print(*numbers, sep='\n')
pprint.pprint(numbers)
pprint.pprint(numbers,width=20)
pprint.pprint(numbers,width=20,indent=4)