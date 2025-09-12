# 사전은 키 : 값 형태로 되어있다.
# 비슷한 자료구조로느 자바스트립트에 오브젝트, 자바의 맵이 있다.
# dic = {}
# tuple = ()
# list = []

dic = {
    'name':'kim,ji-hoon',
    'phone':'010-1234-1234',
    'age':55
}

dic2 = {
    'name':'hong,gil-dong',
    'phone':'010-2233-5454',
    'friends':['Alice','John','Smith']
}

# 사전에 데이터 넣기 1
a = {'first':'a'}
print(a)

# 사전에 데이터 넣기 2
a['second'] = 'b'
print(a)

# 사전에서 특정 요소를 삭제
del a['second']
print(a)