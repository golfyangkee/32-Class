def Test01():
    for i in range(1, 4):
        print(f"======== {i} =========")
        for j in range(1, 4):
            print(f"({i}, {j})", end=' ')   # 열의 값 띄기00000000000000000000000000000000000000000
        print() # 줄의 값 띄기

def Test02():
    start_num = 1
    matrix = ""
    for i in range(5):
        for j in range(5):
            matrix += f"{start_num}\t"
            start_num += 1
        matrix += "\n"
    print(matrix)

def Test05():        # 과제                  # 1 6  11
    start_num = 1                           # 2 7  12
    matrix = ""                             # 3 8  13
    for i in range(5):                      # 4 9  14
        for j in range(5):                  # 5 10 15
            matrix += f"{start_num}\t"
            start_num += 1
        matrix += "\n"
    print(matrix)

def Test04():
    start_num = 25
    matrix = ""
    for i in range(5):
        for j in range(5):
            matrix += f"{start_num}\t"
            start_num -= 1
        matrix += "\n"
    print(matrix)

def Test03():
    for i in range(2, 10,2):    # 2~9까지 스텝이 2니까 2 4 6 8
        print(f'=== {i} 단 ==')
        for j in range(2, 9,2):   # 1~8까지니까 1 2 3 4 5 6 7 8
            print ("%d * %d = \t" %(i, j), i*j)
        print(f'===========')
        
        
if __name__ == '__main__':
    Test05()
        
        
        
        