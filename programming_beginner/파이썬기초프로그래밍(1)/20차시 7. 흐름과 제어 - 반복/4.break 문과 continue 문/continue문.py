#continue문
#1부터 10까지 저장되어 있는 리스트 객체에서 3의 배수를 제외한 합을 구하는 코드

numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for n in numlist:
    if n % 3 ==0:
        continue
    total += n

print("3의 배수를 제외한 총합: {0}".format(total))