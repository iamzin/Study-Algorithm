# X : zip, startwidth
def solution(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

# # zip 함수
# print(list(zip([1,2,3], (4,5,6), "abcd")))
# # [[1, 4, 'a'], [2, 5, 'b'], [3, 6, 'c']]

# # startwidth
# print("dfagd".startswith("abcd"))
# print("abcde".startswith("abcd"))
# # False
# # True

