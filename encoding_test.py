# -*- coding: utf-8 -*-
import sys
import locale
import os

print("=== 인코딩 정보 확인 ===")
print(f"시스템 기본 인코딩: {sys.getdefaultencoding()}")
print(f"파일 시스템 인코딩: {sys.getfilesystemencoding()}")
print(f"stdout 인코딩: {sys.stdout.encoding}")
print(f"stdin 인코딩: {sys.stdin.encoding}")
print(f"로케일 인코딩: {locale.getpreferredencoding()}")
print(f"환경변수 PYTHONIOENCODING: {os.environ.get('PYTHONIOENCODING', '설정 없음')}")
print()

print("=== 한글 출력 테스트 ===")
print("안녕하세요! 파이썬에서 한글 출력 테스트입니다.")
print("한글 문자열:", "가나다라마바사아자차카타파하")
print("숫자와 한글:", "1번째 테스트", "2번째 테스트")
print()

# 다양한 한글 문자 테스트
korean_chars = ["가", "나", "다", "라", "마", "바", "사", "아", "자", "차"]
print("한글 문자 리스트:", korean_chars)
print()

# 한글이 포함된 딕셔너리
student_info = {
    "이름": "김철수",
    "나이": 25,
    "학교": "파이썬 대학교",
    "전공": "컴퓨터공학과"
}
print("학생 정보:", student_info)
print()

# f-string에서 한글
name = "이영희"
age = 23
print(f"이름: {name}, 나이: {age}세")
print()

print("=== 특수 문자 및 이모지 테스트 ===")
print("특수문자: ★☆♥♠♣♦")
try:
    print("이모지: 😀😊🎉🐍")
except UnicodeEncodeError as e:
    print(f"이모지 출력 실패: {e}")
print()

print("=== 인코딩 문제 해결 확인 ===")
print("만약 이 텍스트가 깨져 보인다면 인코딩 문제가 있습니다!")
print("정상적으로 보인다면 인코딩이 올바르게 설정되었습니다!") 