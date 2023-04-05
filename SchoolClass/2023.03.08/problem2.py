# 여러 문장으로 구성된 복문을 입력받아서 문장의 첫 자를 대문자로 바꾸어 한 줄에 한 문장씩 출력해주는 프로그램 작성

y = input()

yresult = y.split('. ')
print(yresult)

for i in yresult:
    i = i.capitalize()
    print(i + ".")
