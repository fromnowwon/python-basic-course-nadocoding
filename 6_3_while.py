# while
customor = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customor, index))
    index -= 1
    
if index == 0:
		print("커피는 폐기처분되었습니다.")
                
customor = "아이언맨"
index = 1
while True:
		print("{0}, 커피가 준비되었습니다. {1}번 호출.".format(customor, index))
		index += 1