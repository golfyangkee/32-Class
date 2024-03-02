import json
def Test01():
    data=[{'a':'A', 'b':(2,4), 'c':3.0}]  # list
    print('data :', data , 'repr(data) : ' ,repr(data), str(data))
    # data : [{'a': 'A', 'b': (2, 4), 'c': 3.0}] repr(data) :  [{'a': 'A', 'b': (2, 4), 'c': 3.0}] [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
    print(type(data) ,   type(repr(data)))
    data_string = json.dumps(data)  # 파이선 데이터를 json형식으로 변환 후 문자열로 리턴 // 파일(dump)은 안 줬기 때문에 객체로
    # Serialize obj to a JSON formatted str. = Json으로 str으로 반환?
    print('json :', data_string , type(data_string)) # 결과확인 () 터플이 [] list로 바뀜 ''는 ""로 바뀜
    # json : [{"a": "A", "b": [2, 4], "c": 3.0}] <class 'str'>

def Test02():
    data ={'a': 'A', 'c': 3.0, 'b': (2, 4)}  # {} dict 타입
    data_string = json.dumps(data, indent=4,sort_keys=True) # 인코딩
    ## ★★★★★ 암기 디코딩 = loads
    # indent 들여쓰기, sort_keys 키값도 정렬하겠다. dumps 문자열로 리턴하겠다
    # dumps 직렬화해서 제이슨을 포맷 - 자동으로 endoced , decoded 해줌 그래서 loads dumps 자주 씀
    슴
    print('Encoded :', data_string)
    # repr(data_string))
    decoded  = json.loads(data_string)  # 디코딩
    print("decoded :", decoded, type(decoded))  # type 확인 딕트로 리턴해줌
    # decoded : {'a': 'A', 'b': [2, 4], 'c': 3.0} <class 'dict'> (2,4) 는 이미 []로 받아서 못 돌려놓음
    # dumps는 json 타입으로 loads 는 python 타입으로 변환
def Test03():
    obj_json = '{"str": [42.2,1,2,3,4,5], "str01": 42, "str02":100}'  #str
    obj = json.loads(obj_json)
    print(obj)
    print(json.dumps(obj, indent=4, sort_keys=True))

def Test04():
    obj_json = {"str": [42.2], "str03": [42.2,1,2,3,4,5], "str01": 42, "str02":'대한민국'}

    file  = "data.json"
    json.dump(obj_json,fp=open(file,'w'),indent=4, sort_keys=True)
    # dump 니까 파일을 넣는다.
    # load 랑 dump 는 텍스트 형태만 가지고 오는데 wb 나 rb는 바이너리 타입이 아니고
    # 왜냐면 내부적으로 json 파일 자체가 알아서 바이너리 타입으로 데이터를 관리한다.

    #파일에서 읽어서 화면 출력 하기
    # 2가지 방법 중 하나
    # file = open("data.json", 'r') #r+b
    # # file = open("data.json", 'rb')
    # result = json.load(fp=file)
    # print(result)
    # file.close()

    # 2가지 방법 중 또다른 하나
    result = json.load(fp=open(file,'r'))
    print(result)

# json 타입 자체가 알아서 바이너리 타입으로 관리를 함

if __name__ == '__main__':
    Test04()