import json
def Test01():
    # 문제 1: Json 데이터 읽기와 쓰기
    # 1단계: Python 딕셔너리 생성
    data1={"name":"John","age":30,"city":"NewYork"}

    # 2단계: 딕셔너리를 Json 문자열로 변환하여 파일에 저장\
    with open('data1.json','w') as file:
        json.dump(data1,file)

    # 3단계: 파일 읽기
    with open('data1.json','r') as file:
        loaded_data1=json.load(file)

    # 4단계: 데이터 출력
    print("문제 1 결과:", loaded_data1)

def Test02():
    data={"employees":[{"name":"John", "age":30},{"name":"Jane","age":25}]}
    file="address_exam02"
    json.dump(data, fp=open(file, 'w'))
    result=json.load(fp=open(file,'r'))
    print(result)
    # 'Jane'의 나이를 26으로 변경하세요
    result['employees'][1]['age']=26
    print(result)
    json.dump(result,fp=open(file,'w'))

def Test03():
    # 문제 3: JSON 데이터 필터링
    # JSON 파일 생성
    products=[
        {"id":1,"product":"Laptop","price":800},
        {"id": 2, "product": "Mouse", "price": 20},
        {"id": 3,"product": "Monitor", "price": 200},
    ]
    # 파일 읽기 및 필터링

    # 필터링된 데이터 출력
    print("문제 3 결과:", expensive_)
    pass

def Test04():
    # 문제 4: 중첩된 JSON 데이터 처리
    # JSON 데이터 생성 및 파일 저장
    company_data= {
        "company": "TechCorp",
        "employees": [
            {"name":"John Doe", "dapartment":"HR", "email":"john@example.com"},
            {"name": "Jane Smith", "dapartment": "IT", "email": "jane@example.com"},
        ]
    }

    with open('company.json', 'w') as file:
        json.dump(company_data,file)

    # 파일 읽기 및 직원 정보 출력
    with open('company.json','r') as file:
        loaded_company_data=json.load(file)
        for employee in loaded_company_data["employ"]:
            print(f'문제 4 결과: {employee}')

if __name__ == '__main__':
    Test01()
