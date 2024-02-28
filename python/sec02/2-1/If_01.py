
def If_test():
    my_id= input("Enter your id: ")
    if my_id == "a1234":  # 값 비교
        #pass    그냥 말 그대로 pass 아무 것도 안 하겠다.
        print("true :", my_id)

def If_test02():    # >  <  >=  <=  ==  != -> bool(True/False)
    my_id= input("Enter your id: ")
    if my_id != "a1234":  # 입력받은 my_id가 "a1234"와 같지 않다면
        print("true :", my_id)

def If_test03():
    if None:
        print("True")
    elif False:
        print("Flase")
    else:
        print("etc...")

if __name__ == '__main__':
    If_test03()