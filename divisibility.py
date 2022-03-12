def divisibility(num):
    result=""
    if num% 3 == 0 and num% 5 == 0:
        result = "FizzBuzz"
    elif num% 3 == 0:
        result ="Fizz"
    elif num% 5 == 0:
        result = "Buzz"
    return result
# def divisibility(num):
#     result=""
#     if num%3 ==0 :
#         result += "Fizz"
#     if num%5 ==0 :
#         result +="Buzz"
#     return result
print(divisibility(15))
print(divisibility(9))
print(divisibility(20))
print(divisibility(22))