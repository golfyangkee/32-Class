import json
My_s = '''{"name":"RuRi", 
        "brothers":["Ruse", "RuO"], 
        "addr":"Toronto"}'''

class my_jsonObject:
    def __init__(self, res):  #res  = My_s
        self.__dict__ = res     # 대입
        # __dict__: Object 클래스가 준 dict 객체를 관리하는 메소드이다.
        # 재정의를 하면서 dict에다가 res문자열을 주면 알아서 key value key value라는 데이터 타입으로 관리를 하겠다.
        print(self.__dict__, res)   # 출력 확인

if __name__ == '__main__':
    # object_hook은 대상을 클래스인 객체로 연동해서 구현된다.
    data = json.loads(My_s, object_hook= my_jsonObject)
    # object_hook : loads 가 약간 데이터클래스 별로 만들어져서 값을 입력 받는 거 같다
    # 핸들링을 따로 하는 코레이블? 함수가 따로 있다는 거다
    # 대상 값을 가져다가 애한테 좀 맡기고 싶다. my_jsonObject 라는 친구한테
    # My_s 값을 클래스 my_jsonObject가 위임을 받는거다
    # 클래스 my_jsonObject가 res에 My_s 값을 받는 거
    print(data, type(data))
    print('=======')
    print(data.name)
    print(data.addr)
    for brother in data.brothers:
        print(brother)