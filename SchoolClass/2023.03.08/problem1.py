# 아무 문자열 공백 제거 후 모음(aeiou)빼고 출력하기


y = input() # "hello my name is baekseojin"
yresult = y.replace(" ", "")

for i in yresult:
    if i in ("aeiouAEIOU"):
        yresult = yresult.replace(i, '')

    
print(yresult)