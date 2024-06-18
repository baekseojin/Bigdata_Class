# 주민등록번호 유효성을 체크해보자

print("주민등록번호 유효성 검사")
a = input()

a1 = int(a[0]) * 2
a2 = int(a[1]) * 3
a3 = int(a[2]) * 4
a4 = int(a[3]) * 5
a5 = int(a[4]) * 6
a6 = int(a[5]) * 7
a7 = int(a[7]) * 8
a8 = int(a[8]) * 9
a9 = int(a[9]) * 2
a10 = int(a[10]) * 3
a11 = int(a[11]) * 4
a12 = int(a[12]) * 5
a13 = int(a[13])

a = (a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11 + a12)

a = a % 11

if(a>9):
    a = a % 10

a = 11 - a

if(a13 == a):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호 입니다.")