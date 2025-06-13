- 사용한 룰
```text
    1. 한글로 설명해줘
    2. filesystem mcp 서버를 이용해서 ipynb 파일을 작성해줘
    3. 토큰제한이 걸리면 일단 작성하고 추가로 작성을 이어갈 수 있게 해줘 
    4. 아래는 Jupyter Notebook 생성 규칙이야

    # Jupyter Notebook 생성 규칙
    When creating .ipynb files:
    4-1. Always use valid JSON syntax
    4-2. Set cell_type correctly ("markdown" or "code")
    4-3. Include proper metadata structure
    4-4. Set execution_count to null for code cells
    4-5. Set outputs to empty array [] for code cells
    4-6. Use nbformat: 4 and nbformat_minor: 4
    4-7. Include kernelspec and language_info in metadata
    4-8. For markdown cells, escape quotes and use \n for line breaks
    4-9. Validate JSON structure before output

    아래 구조로 작성 해야 돼
    gen_python/
    ├── Python_문법_수업_계획서.md
    ├── Chapter01_파이썬_시작하기/
    │   ├── 01_파이썬_소개_및_설치.ipynb
    │   ├── 02_개발환경_설정.ipynb
    │   └── 03_첫_번째_프로그램.ipynb
    ├── Chapter02_변수와_자료형/
    │   ├── 01_변수_기초.ipynb
    │   ├── 02_숫자형_자료형.ipynb
    │   ├── 03_문자열_자료형.ipynb
    │   ├── 04_불린형_자료형.ipynb
    │   └── 05_미니프로젝트_간단한_계산기.ipynb
    ├── Chapter03_연산자/
    │   ├── 01_산술_연산자.ipynb
    │   ├── 02_비교_논리_연산자.ipynb
    │   ├── 03_연산자_우선순위.ipynb
    │   └── 04_미니프로젝트_숫자_맞추기_게임.ipynb
    ├── Chapter04_자료구조/
    │   ├── 01_리스트_기초.ipynb
    │   ├── 02_리스트_고급.ipynb
    │   ├── 03_튜플.ipynb
    │   ├── 04_딕셔너리.ipynb
    │   ├── 05_집합.ipynb
    │   └── 06_미니프로젝트_학생_성적_관리.ipynb
    ├── Chapter05_제어문/
    │   ├── 01_조건문_if.ipynb
    │   ├── 02_반복문_for.ipynb
    │   ├── 03_반복문_while.ipynb
    │   ├── 04_분기문_break_continue.ipynb
    │   └── 05_미니프로젝트_가위바위보_게임.ipynb
    ├── Chapter06_함수/
    │   ├── 01_함수_기초.ipynb
    │   ├── 02_매개변수와_반환값.ipynb
    │   ├── 03_내장_함수.ipynb
    │   ├── 04_람다_함수.ipynb
    │   └── 05_미니프로젝트_단어_검색기.ipynb
    ├── Chapter07_객체지향_프로그래밍/
    │   ├── 01_클래스_기초.ipynb
    │   ├── 02_생성자와_메서드.ipynb
    │   ├── 03_상속.ipynb
    │   ├── 04_캡슐화와_다형성.ipynb
    │   └── 05_미니프로젝트_도서관_관리_시스템.ipynb
    ├── Chapter08_모듈과_패키지/
    │   ├── 01_모듈_기초.ipynb
    │   ├── 02_패키지_사용법.ipynb
    │   ├── 03_외부_라이브러리.ipynb
    │   └── 04_미니프로젝트_날씨_정보_앱.ipynb
    ├── Chapter09_파일_입출력/
    │   ├── 01_파일_읽기_쓰기.ipynb
    │   ├── 02_CSV_JSON_처리.ipynb
    │   └── 03_미니프로젝트_일기장_프로그램.ipynb
    └── Chapter10_예외처리/
        ├── 01_예외처리_기초.ipynb
        ├── 02_사용자_정의_예외.ipynb
        └── 03_최종프로젝트_종합_퀴즈_게임.ipynb
```