num = int(input("숫자 입력: "))
i = 2
prime = True    #소수 인지 판별을 위한 flag 변수
while i <= num-1 :
    if num%i == 0 :
        prime = False   #나누어 떨어지면 소수가 아님
    i += 1

if prime == True :   #한 번이라도 나누어 떨어져서 False로 변경되지 않은 경우
    print(num, "은(는) 소수(prime number) 입니다.")
else :
    print(num, "은(는) 소수(prime number)가 아닙니다.")
