'''
하위 디렉토리 검색하기
특정 디렉터리부터 시작해서
그 하위(디렉터리 포함)의
모든 파일 중 파이썬 파일(*.py)만
출력해 주는 프로그램을 만들어보자.

필요한 기능은? 파이썬 파일만 찾아서 출력하기
입력받는 값은? 검색을 시작할 디렉터리
출력하는 값은? 파이썬 파일명
'''
import glob

a=input('검색 디렉터리를 입력하세요:')

num = glob.glob(f'{a}*.py')
print(len(num))

file_list=glob.glob(f'{a}*.py')
print(file_list)
print(len(file_list))

'''
다시풀기
'''