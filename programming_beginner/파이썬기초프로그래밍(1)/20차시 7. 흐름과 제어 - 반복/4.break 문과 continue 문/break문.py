# 4.break 문과 continue 문
# break 문
# 사용자의 입력 값이 문자열 "q"이면 반복문을 빠져나오는 코드

answer = ""

while True:
    answer = input("명령을 입력하세요.\n'q'를 입력하면 프로그램이 종료됩니다.:")
    
    if answer == "q":
        break 
    print("'{0}'를 입력하셨습니다.".format(answer))
    print()

print("프로그램을 종료합니다...")