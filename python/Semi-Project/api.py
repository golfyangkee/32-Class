import requests

url = 'http://apis.data.go.kr/B490007/qualAcquPtcond/getQualAcquPtcond'
params ={'serviceKey' : 'MVjz9RWKT+f0Y2MMw8uqcvgm7TnH+d3Ggf8YGw5hmslFACluBQDvAqwNJnMDckPOxTLpQjrWodVV19tVMuksdg==',
         'numOfRows' : '10',
         'pageNo' : '1',
         'dataFormat' : 'xml',
         'acquYy' : '2020',
         'qualgbCd' : 'T',
         'rgnCd' : '001',
         'ageGrupCd' : '3',
         'genderCd' : 'M',
         'seriesCd' : '03',
         'jmCd' : '1320',
         'jmNm' : '정보처리기사' }

response = requests.get(url, params=params)
print(response.content)