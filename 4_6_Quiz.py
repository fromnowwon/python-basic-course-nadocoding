# 사이트별로 비밀번호를 만들어주는 프로그램

# 예) http://naver.com
address = "http://naver.com"

# 규칙 1: http:// 부분은 제외
address = address.replace("http://", "");

# 규칙 2: 처음 만나는 점(.) 이후 부분은 제외
dotIdx = address.index(".");
address = address[0:dotIdx];

# 규칙 3: 남은 글자 중 처음 세 자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로 구성
count = str(len(address))
countE = str(address.count("e"))

print(address[0:3] + count + countE + "!")
