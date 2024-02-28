# 시퀀스->  리스트=CRUD , 터플CRUD(X) , str = 문자열= CRUD(X),  딕트 사전형
# 자료형 : 인덱스로 관리할 수 있다
items = ("apple", "banana", "cherry", "date")
#1. 튜플의 첫 번째 요소를 출력
print("1. 튜플의 첫 번째 요소:", items[0])
#2. 튜플의 마지막 요소를 출력
print(items[-1])
#3. 튜플에서 "banana"가 몇 번째 인덱스에 있는지 찾아 출력
banana_index=items.index("banana")
print("3. banana의 인덱스", banana_index)
print(items.index("banana"))

############################################
# dict   {키 : 값 , ,,,}
fruits = {'apple': 2.5, 'banana': 1.2, 'orange': 1.0, 'grape': 3.0}

#1 fruits에서 'banana'의 가격을 출력
print("banana의 가격")
banana_price=fruits['banana'] #fruits.get('banana')
print(banana_price)
print(fruits['banana'])
#2.orange'의 가격을 출력
print("orange의 가격")         #fruits.get('orange')
orange_price=fruits['orange']
print(orange_price)
print(fruits['orange'])
#3.apple'과 'grape'의 가격을 더한 결과를 출력
print(float(fruits['apple'])+float(fruits['grape']))

total_price=fruits['apple']+fruits['grape']
print(total_price)

### 번외편
'''
apple_price = fruits.get('apple',o) #'apple' 키가 없으면 0으로 가정
grape_price = fruits.get('grape',o) #'grape' 키가 없으면 0으로 가정
total_price = apple_price+grape_price
print(f"'apple'과 'grape'의 가격을 합하면 {total_price}입니다.")
'''

#4.'watermelon'을 키로 가진 항목을 추가하고, 해당 키에 4.5 값을 할당
fruits['watermelon']=4.5    #fruits.update({'watermelon':4.5})
print(fruits)

#5.'banana'의 가격을 1.5로 업데이트 코드 작성 후 출력
fruits['banana']=1.5        #fruits.update({'banana':1.5})
print(fruits['banana'])

'''
test(a,*b,**d)
test(value,*tuple,**dict)

E elemet 약자
**F dict 약자
-> 뒤를 리턴해준다. None 은 리턴하는 게 없다는 뜻
... 점 세개는 1 more
'''

# if __name__ == '__main__':
# IndentationError: expected an indented block after 'if' statement on line 59
### {} + {} -> update로 딕트랑 딕트랑 결합가능  : 중복키가 있을 경우 덮어쓰기를 한다.
print('=====================================')
fruits = {'apple': 2.5,'grape': 3.0, 'banana': 1.2, 'orange': 1.0}
fruits02 = {'apple': 2.5, 'Banana': 1.2, 'orange': {'a':40}, 'grape': {'a':40,'b':77,'c':(1,2,[3,4,],5,6,)}}
print(fruits)       # 준 데로 프린트 진행 , 대소문자 구분
#del fruits

del fruits02    # del 있는 친구들은 compile 2번씩 해주기
# NameError: name 'fruits02' is not defined. Did you mean: 'fruits'?

# fruits.update(fruits02) # fruits02를 참조할 수 없을 경우 현재 fruits 주소는 유효하다. (파이참 판단) 소멸의 시점을 잡고 있다. 셀에서 돌리면 오류가 나기에 파이참도 오류 다른 곳에서는 안 나는데 dict.update에서만 나온다.
# fruits.update(fruits03) 이건 03이 없으니까 오류가 난다?

print(fruits)


