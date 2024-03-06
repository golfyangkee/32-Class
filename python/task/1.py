# for 문을 while 문으로 변경해라

for inx in range(6):
    for jnx in range(inx + 1):
        print("*", end="")
    print("@")

print("===while 문 변경===")
i=1
while i <= 5:
    j=1
    while j <= i:
        j += 1
        print("*", end="")
    i += 1
    print("@")
