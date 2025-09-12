dic = {
    'name':'hong,gil-dong',
    'phone':'010-1234-1234',
    'friends':['Alice','Smith','Jhone']
}


# dic.keys() : 특정한 사전의 키들만 가져와 dict_keys라는 객체를 반환한다.
print(dic.keys())
for item in dic.keys():
    print(item)

# dict_keys -> list로 변환
keys = list(dic.keys())
print(keys)

#dic.values() : 특정 사전의 값만 가져와 dict_values라는 객체를 반환
print(dic.values())
#list로 변경해서 valuse라는 변수를 담아보자
for item in dic.values(): # 딕셔너리의  values 값들을 하나씩 꺼내면서 item에 넣어줌
    print(item)

valuses = list(dic.values()) # values값을 딕셔너리에 리스트형태로 넣는다.
print(valuses)

# dic. items() : 사전의 키 : 값을 한쌍으로 가져와 dict_items로 반환한다,.
# 각 키와 값은 ()모양으로 보아 tuple 이다.
print(dic.items())
# lis로 변환해 보면 list 안에 각 키와 값이 tuple로 저장되어 있음을 알 수 있다.
li = list(dic.items())
print(li)

# 값을 가져오기
print(dic.get('name'))
print(dic['phone'])

# dic 안에 있는 모든 키와 값을 키:값 형태로 출력해보자
# 1. 키를 뽑아낸 다음, 키를 가지고 값을 뽑아내는 방법
for key in dic.keys(): # 딕셔너리의  key 값들을 하나씩 꺼내면서 key에 넣어줌
    print(f'{key}:{dic[key]}')

# 2. 키와 값을 동시에 뽑아낸 다음 거기서 키와 값을 각각 추출하는 방식
for item in dic.items():
    print(f'{item[0]}={item[1]}')


