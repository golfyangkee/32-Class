'''
홍길동 서울시 02-0000
박길동 부산시 051-0000
정길동 인천시 032-0000
'''
'''
1) 위 주소록을 json으로 저장해 보자. 키를 name, addr, tel로 구현하자.
2) 파일 이름은 address.json
3) 이름   : 홍길동, 박길동, 정길동
   전화번호:
   주소   : 
'''
import json

if __name__ == '__main__':

    address_data = [
        {"name": '홍길동', "addr" : "서울시", "tel":"02-0000"},
        {"name": '박길동', "addr": "부산시", "tel": "051-0000"},
        {"name": '정길동', "addr": "인천시", "tel": "032-0000"}
        ]

    file  = "address.json"
    json.dump(address_data,fp=open(file,'w'),indent=4) # json으로 쓰고
    data=json.load(fp=open('address.json','r')) # address.json 으로 읽어서 데이터로 리턴을 받았어

    for entry in data:
        print(f'이름:{entry['name']}, 전화번호 {entry['tel']}, 주소: {entry['addr']}')

    print('=========================')
    names=','.join(entry['name'] for entry in address_data)
    tels = ','.join(entry['tel'] for entry in address_data)
    addrs = ','.join(entry['addr'] for entry in address_data)
    print(f'이름:{names}')
    print(f'전화번호:{tels}')
    print(f'주소:{addrs}')