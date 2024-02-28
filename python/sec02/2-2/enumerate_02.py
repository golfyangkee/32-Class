
#enumerate()함수 미사용 한 경우
fruit  = ['apple','watermelon','peach','pear']
for i in range(len(fruit)):
   print(i+100, fruit[i])


print('--------------------------')
#enumerate()함수 사용 한 경우
for i, res in enumerate(fruit,100):
    print(i,res)

print('--------------------------')
# 결과를 파일로 저장해보자. 파일을 잘 이용해야 한다. 너무 쉬워서 잘 잊어버리니 자꾸 써봐야 한다.
with open('fortest.txt', 'w') as file:
    for i, res in enumerate(fruit, 100):
        file.write(f"{i},{res}\n")

print('--------------------------')
with open('fortest.txt', 'r') as file:
    print(file.read())
