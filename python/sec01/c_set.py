a={1,4,5,6,10}
b={6,10,7,8,9}
print(a)
print(b)

print('===합집합 ', (a|b), a.union(b))
print('===차집합 ', (a-b), a.difference(b))
print('===교집합 ', (a & b), a.intersection(b))
print('===배타 집합 ', (a^b), a.symmetric_difference(b))

# 셋은 순서가 없는 자료형 -> (인덱스를 활용해서 데이터를 출력할 수 없다.)
# set -> list -> index or 반복문으로 출력

print(list(a))
print(list(a)[0])

#요소를 리스트로 변환한 후 출력
my_list=list(a)
print(my_list)

#요소를 반복문을 사용하여 출력
for element in a:
    print(element)

# 숫자 10을 byte로 출력하고 int로 변형해 보자.
print('=========================')
tenbytes=bytes(10)
print(tenbytes)
int.from_bytes(bytes(10),'big')
int.from_bytes(bytes(10),'little')

print('=========================')
number= 10
res = number.to_bytes(1,'big')
print(res)
res01 = number.to_bytes(1,'little')
print(res01)
res=frozenset([1,2,3,4,5])
my={res:'abcde'}
print(my) # {frozenset({1, 2, 3, 4, 5}): 'abcde'}

#ex {서울,여의도,과장 : 홍길동}, 복합키 생성해서 키값이 불변이다.
