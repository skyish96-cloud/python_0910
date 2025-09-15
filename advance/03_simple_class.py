# JAVA에서는 파일명 == 클래스명
# 파이썬에서는 꼭 그렇지는 않다.
class Student: # Student라는 클래스
    # - (학생과 관련된 함수 및 변수가 들어오겠구나 라고 예측이 가능)
    pass # pass는 함수나 클래스에 아무것도 없을때 오류방지를 위해 넣는 키워드

# 클래스 선언하는 방법
std1 = Student()
std2 = Student()
std3 = Student()
# 일련번호가 서로 다르다.
# 파이썬에서도 객체화는 복사를 의미하므로 서로 다른 객체는 같지 않다.
# 물론 나중에는 원본으로 사용이 가능하기도 하다.
print(std1)
print(std2)
print(std3)






