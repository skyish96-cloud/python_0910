# 검색 -> 특정한 자료 덩어리에서 원하는 값을 찾는것
a = [3,4,1,2,3,4,'G','F','G']
# 원하는 값에 인덱스 찾기
# 2 라는 값은 어느 위치에 있는가?
print(f'2는 어디?:{a.index(2)}')
print(f'G는 어디?:{a.index('G')}') # G는 2개지만 처음 찾은 값만 알려준다.

# 5번 인덱스부터 'G'를 찾아라
print(f'G는 어디?:{a.index('G',5)}')

# print(a.index('H'))
# ValueError: 'H' is not in list
# 값이 없으면 에러(예외)를 발생시킨다.

b = [3,4,1,2,3,4,5,6,1,3,2] # 모든 3을 찾아보세요.
print(f'3은 어디?:{b.index(3,0)}')
print(f'3은 어디?:{b.index(3,1)}')
print(f'3은 어디?:{b.index(3,5)}')

#이렇게도 방법이 있다.
# idx = b.index(3,0)
# print(f'3의 값은 {idx}번에 있다.')
# idx = b.index(3,1)
# print(f'3의 값은 {idx}번에 있다.')
# idx = b.index(3,5)
# print(f'3의 값은 {idx}번에 있다.')

idx = 0
# while True:
#     idx = b.index(3,idx)
#     print(f'3의 값은 {idx}번에 있다.')
#     idx += 1

#가장 고전적인 방법이다.
for n in b: # for in을 이용하면 list에 있는 값을 순서대로 하나씪 뽑아낸다.
    if n == 3:
      print(f'3이 있는 인덱스 : {idx}')
    idx += 1

# 코드리뷰를 해야함...
# while True:
#     idx = b.index(3,idx)
#     print(f'3의 값은 {idx}번에 있다.')
#     idx += 1