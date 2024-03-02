import csv
# 아마 엑셀파일? 텍스트 애들을 뽑아다가 json으로 json을 텍스트로 csv로 xml로 왔다 갔다.
# json 타입을 할때는 반드시 csv로 저장을 해야 하니까

# CSV 파일 경로 설정
csv_file_path = 'address.csv'

# 주소록 데이터
address_data = [
    {"name": "홍길동", "addr": "서울시", "tel": "02-0000"},
    {"name": "박길동", "addr": "부산시", "tel": "051-0000"},
    {"name": "정길동", "addr": "인천시", "tel": "032-0000"}
]

# CSV 파일로 데이터 쓰기
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "addr", "tel"])
    writer.writeheader()  # 컬럼명을 쓴다.
    writer.writerows(address_data)  # 행 데이터를 쓴다.


