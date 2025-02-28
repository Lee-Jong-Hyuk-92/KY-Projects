import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "9 60 15 213 9495806474906 7581 28240 840414 3802773 425624"

p1 = r"\b\d{9,}\b"         # 자릿수가 3 이상 5 이하인 수
# \b는 단어와 단어 경계사이, 여기서 말하는 단어는 A-Z, a-z, 0-9, _ 로 이루어진 연속된 문자

m1 = re.findall(p1, text)

print("m1 결과 : ", m1)

