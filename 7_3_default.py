# 기본값
# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
#           .format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")



# 이름만 다른 경우
def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
          .format(name, age, main_lang))
    
profile("유재석")