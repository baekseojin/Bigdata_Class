a = ["전화번호 등록", "전화번호 삭제", "전화번호 검색", "전화번호 전체 보기", "종료"]
dic = {

}

while True:
    for i in range(5):
        print( (i+1) , " : " , a[i])

    num = int(input())

    if num == 1:

        b = input("이름:전화번호 형태로 입력 >>  ").split(':')
        dic[ b[0] ] = b[1]

    if num == 2:
        c = input("삭제할 이름을 입력하세요 >>  ")
        del dic[c]
    
    if num == 3:
        d = input("검색할 이름을 입력하세요 >>  ")
        
        print(dic[d])

    if num == 4: 
        print(dic)

    if num == 5:
        break

            


        

    

