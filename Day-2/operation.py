# 2023/02/27

# operation(연산)

'''
  [PEMDAS - 여러 연산이 혼합된 연산순서]
  () : 괄호(Parentheses)
  ** : 지수(Exponents)
  *  : 곱셈(Multiplication)
  /  : 나눗셈(Division)
  +  : 덧셈(Addition)
  -  : 뺄셈(Subtraction)
  [순서]
  ()
  **
  *,/
  +,-
'''
print(3*3+3/3-3)
# 실행 순서 => 1. (3*3), (3/3) => 2. (9 + 1) => 3. (10 - 3) => 4.  7
#                  ( * , / )          (+)            (-)         (=)

print(3 * (3 + 3) / 3 - 3)
# 실행 순서 => 1. (3 + 3) => 2. (3 * 6) => 3. (18 / 3) => 4. (6 - 3) => 5. 3
#                   ( )          (*)            (/)           (-)       (=)

# BMI operations 

# Don't change the code below
height = input("Enter u r height in m: ")
weight = input("Enter u r weight in kg: ")
# Don't change the code above

# Write u r code below this line
# operator
BMI = int(weight) / float(height) ** 2
# PEMDAS
# BMI = int(weight) / float(height * height)
# BMI_INT = int(BMI)

print(f'BMI : {int(BMI)}')