# 4.break 문과 continue 문
## break 문
### 사용자의 입력 값이 문자열 "q"이면 반복문을 빠져나오는 코드

```Python

answer = ""

while True:
    answer = input("명령을 입력하세요.\n'q'를 입력하면 프로그램이 종료됩니다.:")
    
    if answer == "q":
        break 
    print("'{0}'를 입력하셨습니다.".format(answer))
    print()

print("프로그램을 종료합니다...")

```

## continue문
### 1부터 10까지 저장되어 있는 리스트 객체에서 3의 배수를 제외한 합을 구하는 코드
```Python
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for n in numlist:
    if n % 3 ==0:
        continue
    total += n

print("3의 배수를 제외한 총합: {0}".format(total))
```
## 반복문으로 트리만들기

``` Python
#step 1.

 for i in range(1,5):
     print("*" * i)

 i = 1
 while i <= 4:
     print("*" * i) 
     i = i + 1

#step 2.

 for i in range(1, 3):
     for k in range(1,5):
         print("*" * k)

 i, k = 1, 1
 while i <= 2:
     while k <= 4:
         print("*" * k)
         k = k +1
     i = i + 1
     k = 1

#step 3.
i, k = 5, 1
while i >= 0:
    print("{0}{1}".format(" " * i, "*" * (2 * k - 1)))
    i = i - 1
    k = k + 1
```
