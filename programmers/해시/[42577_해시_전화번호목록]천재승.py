def solution(phone_book):
    
    #오름차순으로 정렬하면 현재 번호에 다른 번호를 접두어로 가지고 있는 경우, 접두어 대상이 되는 번호는 현재 번호보다 무조건 앞에 있다. 
    phone_book.sort()
    leng=len(phone_book)
    
    for i in range(1,leng):
        before=phone_book[i-1]

        cur=phone_book[i][0:len(before)]
        # print(before, cur)

        if before==cur:
            return False

    return True

print(solution(["12","123","1235","567","88"]))