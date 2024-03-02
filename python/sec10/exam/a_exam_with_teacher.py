import json

def Exam01():
        # 문제 1: JSON 데이터 읽기와 쓰기
        # 1단계: Python 딕셔너리 생성
        data1 = {"name": "John", "age": 30, "city": "New York"}

        # 2단계: 딕셔너리를 JSON 문자열로 변환하여 파일에 저장
        with open('data1.json', 'w') as file:
            json.dump(data1, file)

        # 3단계: 파일 읽기
        with open('data1.json', 'r') as file:
            loaded_data1 = json.load(file)

        # 4단계: 데이터 출력
        print("문제 1 결과:", loaded_data1)

def Exam02():
    # 문제 2: JSON 데이터 수정
    # JSON 파일 생성
    data2 = {"employees": [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]}
    with open('data2.json', 'w') as file:
        json.dump(data2, file)

    # 파일 읽기 및 수정
    with open('data2.json', 'r') as file:
        loaded_data2 = json.load(file)
    loaded_data2["employees"][1]["age"] = 26  # Jane의 나이 수정

    # 수정된 데이터 저장
    with open('data2.json', 'w') as file:
        json.dump(loaded_data2, file)

def Exam03():
    # 문제 3: JSON 데이터 필터링
    # JSON 파일 생성
    products = [
        {"id": 1, "product": "Laptop", "price": 800},
        {"id": 2, "product": "Mouse", "price": 20},
        {"id": 3, "product": "Monitor", "price": 200}
    ]
    with open('products.json', 'w') as file:
        json.dump(products, file)

    # 파일 읽기 및 필터링
    with open('products.json', 'r') as file:
        loaded_products = json.load(file)
    expensive_products = [product for product in loaded_products if product["price"] >= 50]

    # 필터링된 데이터 출력
    print("문제 3 결과:", expensive_products)

def Exam04():
    # 문제 4: 중첩된 JSON 데이터 처리
    # JSON 데이터 생성 및 파일 저장
    company_data = {
        "company": "TechCorp",
        "employees": [
            {"name": "John Doe", "department": "HR", "email": "john@example.com"},
            {"name": "Jane Smith", "department": "IT", "email": "jane@example.com"}
        ]
    }
    with open('company.json', 'w') as file:
        json.dump(company_data, file)

    # 파일 읽기 및 직원 정보 출력
    with open('company.json', 'r') as file:
        loaded_company_data = json.load(file)
        for employee in loaded_company_data["employees"]:
            print(f"문제 4 결과: {employee['name']} - {employee['email']}")

if __name__ == '__main__':
    Exam01()
    Exam02()
    Exam03()
    Exam04()