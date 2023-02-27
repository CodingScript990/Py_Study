# 2023/02/27

# F-String

# 반올림
print(round(8 / 3, 2)) # 2.666인데 반올림 소숫점 2자리 까지라서 2.67이 됨

# 나머지
print(8 // 3) # 3 나누기 8은? 2.66이나? 여기서 나머지를 말하기에 소숫점을 제외하고 "2"를 말함

# 부동 소수점
print(8 / 3) # 3 나누기 8은? 2.66666665 가 나옴

# F-String 이전 Output
score = 0
height = 1.8
isWinning = True

# print("u r score is " + str(score)) # str 타입으로 변환 후 출력

# F-string 이후 Output
print(f'u r score is {score}, u r height is {height}, u r isWinning is {isWinning}') # str 타입으로 변환 없이 출력 가능함

# Don't change the code below
age = input("What's u r current age? ")
# Don't change the code above

# Write u r code below this line
# age -> int type
age_int = int(age)
# 90 - age -> int type
years_remaining = 90 - age_int
#  years * 365
days_remaining = years_remaining * 365
# days * 52
weeks_remaining = days_remaining * 52
# weeks * 12
month_remaining = weeks_remaining * 12

# Output[F-String]
print(f'You have {days_remaining} days, {weeks_remaining} weeks and {month_remaining} months left.')
