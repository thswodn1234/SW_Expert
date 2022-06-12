# 함수 호출 및 선언
## print()함수
```Python
a, b = 2, 3

c = a + b

print("내장함수 str.format() 과 print()를 이용한 c의결과 출력: {0}".format(c))
# str.format() 함수의 호출문이 print()함수의 인자로 전달
```
## 함수의 선언

```Python
def 함수명 (매개변수):
    명령문1
    명령문2
    return문
```

### calc_sum()함수 : 두 개의 값을 전달 받아 합을 구하는 사용자 정의 함수
```Python
def calc_sum(x,y): # 매개변수에 인자값 전달
    return x + y

a, b = 2, 3

c = calc_sum(a, b) #반환값 5가 c에 저장
d = calc_sum(a, c) #반환값 7이 변수 d에 저장

print("사용자 정의 함수 calc_sum() 호출을 이용한 c의 결과: {0}".format(c))
print("사용자 정의 함수 calc_sum() 호출을 이용한 d의 결과: {0}".format(d))
```
## 함수 선언의 위치 문제
-인터프리터 언어의 경우 함수 선언 위치가 매우 중요함

-실행 공간에 함수 정보가 없을 경우 오류가 발생할 수 있음
