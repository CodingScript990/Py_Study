# 2023/02/26

# [Data Types]

# print(len(1234))
'''
  TypeError : object of type 'int' has no len()
  -> 타입에러 : 객체 타입을 출력해야하는데, int 타입을 출력할려 해서 함수에서 원하는 조건이 아니기에 에러가 나는 것!
'''

print(len('hi'))


'''
  [String]
  1. 문자열 생성
    - 문자들이 가지런히 늘어서 있는 집합인 문자열을 말함
    - '' [Quotation marks]
    - "" [Double Quotation marks]
    - (''' ''') [Small Triple Quotation marks]
    - (""" """) [Big Triple Quotation marks]
  2. 문자열 분리(Slicing of a string)
    - [], [:]와 같은 슬라이싱 연산자(slice operator)를 사용해서 문자열의 일부분을 분리함
    - [] : index slicing[일부분]
    - ex) 'Hello'[0] = 'H'
    - [:] : first index from last index range[범위]
    - ex2) 'Hello'[0:2] = 'He'
  3. 문자열 합치기(concatenation of two strings)
    - string + string = sum(string)
    - ex) 'Hi, ' + 'World!' = 'Hi, World!'
  4. 문자열 반복하기(repetition of a string)
    - string * 2 = string string(1 X 2 = 2)
    - ex) 'Hi' * 2 = 'HiHi'
'''
# o가 출력 되도록 해봐라!

# 방법1
print('Hello'[-1])
# 방법2
print('Hello'[4])

# 123 345를 출력하면?
# string1 + string2 = string1,2가 나옴
print("123"+ "345") # 123(string1)345(string2)

'''
  [Numeric Types(수 타입)]
  1. Integer[정수]
    - 숫자형의 하나로 소수점이 없는 정수
    - ex) int + int = int => 1 + 2 = 3
  2. Real Number[실수]
    - 숫자형의 하나로 소수점이 있는 실수
    - ex) float + float = float => 1.0 + 1.0 = 2.0
  3. Complex Number[복소수]
    - 실수와 허수의 합인 복소수
  4. 사칙연산
    - +(ADD), -(SUB), *(MUL), /(DIV), //(QUO), %(REM), **(SQU)
    - ex)
      a = 1
      b = 2
      ADD(1,2) = 3
      SUB(1,2) = -1
      MUL(1,2) = 2
      DIV(1,2) = .5
      QUO(1,2) = 0
      REM(1,2) = 1
      SQU(1,2) = 1
'''

# Boolean Types
# True / False

street_name = "Abbey Road"
# Abbe"y"
# Abbey R"o"
print(street_name[4] + street_name[7])
# "yo"

