# \x04 : 16진수 04이고 십진수 4이다
# \x00  : 16진수 00이고 10진수 0이다.
print((1024).to_bytes(2,byteorder='big'))        # 길이가 2 byte수=16진수표시
print((1024).to_bytes(2,byteorder='little'))
print((-1024).to_bytes(4,byteorder='big',signed=True))

print(int.from_bytes( b'\x04\x00', byteorder = 'big' ) )
print(int.from_bytes( b'\x00\x04', byteorder = 'little' ) )

print( int.from_bytes( b'\xff\xff\xfc\x00', byteorder = 'big' )) # 기본값은 False로 양수값만 주겠다고 해서 값이 이상함
print( int.from_bytes( b'\xff\xff\xfc\x00', byteorder = 'big', signed=True ))

print(int.from_bytes(bytes([4,0]),byteorder='big'))  # [4,0]은 바이트를 의미한다 16진수 \x04\x00 의미
