n_list= [[1,2,3 ],[4,5,6],[7,8,9]]

# sublist  [1,2,3 ][4,5,6][7,8,9]
print([num for sublist in n_list for num in sublist])
'''
mylist=[]
for sublist in n_list:
    for num in sublist:
        mylist.append(num)
print(mylist)

이렇게 표현해야 할 걸
위에 한 줄로 표현
'''