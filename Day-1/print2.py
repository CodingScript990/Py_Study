# 2023/02/24

# print('Hello' + ' ' + 'Angela')

'''
  [디버깅]
   - 프로그램의 오류를 발견하고 그 원인을 밝히는 작업 과정을 말함
   - 버그는 '벌레'를 뜻하며, 디버그는 '벌레를 잡다'라는 뜻이며, 버그는 프로그램이 개발자가 의도하지 않은 방향으로 실행된다거나 갑자기 오류가 발생해 실행이 중단되는 등 프로그램의 임무를 정상적으로 실행하지 못하는 오작동을 의미 함
   - 컴퓨터 프로그램 개발 단계 중 발생하는 시스템의 논리적인 오류나 비정상적 연산(버그)을 찾아내고 그 원인을 밝히고 수정하는 작업 과정을 말하며, 프로그램 개발 단계의 마지막이라고 생각하면 됨
   - 오류 수정 프로그램과 작업을 통칭하는 반면, 작업에 중점을 둔 어휘는 디버깅을 쓰며, 오류 수정 S/W를 가리킬 때는 디버거라는 말을 사용함
'''

# Example
# 문제점이 무엇이며 디버깅을 통해서 옳바르게 코딩하시오
'''
  print(Day 1 - String Manipulation")
  print("String Concatenation is done with the "+" sign.")
    print('e.g. print()"Hello " + "world")')
  print("New lines can be created with a backslash and n.")
'''
# 이유 1 - 첫 번째 print 함수에서 ""(따옴표)가 없어서 에러가 났음
# 위 코드(이유 1을 수정 후 Output)
'''
  print("Day 1 - String Manipulation")
  print("String Concatenation is done with the "+" sign.")
    print('e.g. print()"Hello " + "world")')
  print("New lines can be created with a backslash and n.")
'''
# 이유 2 - 세 번째 print 함수에서 들여쓰기 때문에 에러가 났음
# 위 코드(이유 2를 수정 후 Output)
print("Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
print('e.g. print()"Hello " + "world")')
print("New lines can be created with a backslash and n.")
# 이유 1, 2를 수정 후 출력이 잘되는 것을 알 수 있음! -> 1. print함수에 문자열을 출력 시 ""(큰따옴표), ''(작은따옴표)를 열고,닫기를 잘해줄 것! 2. 들여쓰기는 항상 주의! 코드는 순차적으로 실행하는데 들여쓰기의 문제로 인하여 오류가 종종 발생함! 주의 할 것!
