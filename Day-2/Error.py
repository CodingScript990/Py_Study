# 2023/02/26

# Error Types

# num_char = len(input("What's u r name? "))
# print("u r name has " + num_char + " characters.") <- 에러가 남! 그이유는 Number Type인데, String 이여서 그럼

# int type
# print(type(num_char)) # <class 'int'>

# string type
# new_num = str(num_char) # int -> string
# print("u r name has " + new_num + " characters.")

# Integer type

a = 123
print(type(a))

# String type
a = str(123)
print(type(a))

# Float type
a = float(123)
print(type(a))

print(70 + float("100.5")) # 70(int) +_ float(100.5) = 170.5

print(str(70) + str(100)) # 70100

# Example

# input -> 39
# output -> 3 + 9 = 12

# Try to find out the data type of two_digit_number
# Think about what u learnt about subscripting
# Think about type conversion

# two_digit_number = input("Type a two digit number: ")
# 방법1
# sum = int(two_digit_number[0]) + int(two_digit_number[1])
# print(f'{sum}')

# 방법2
two_digit_number = input("Type a two digit number: ")

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

two_digit_number = second_digit + first_digit

print(two_digit_number)