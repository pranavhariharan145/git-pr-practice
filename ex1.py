# Simple Guessing Game
'''
pseudo-code:
function fizzbuzz(number)
    for number in range 0 - n+1:
        if i%3 = 0 and i % 5 = 0 -> FizzBuzz
        if i % 3 = 0 -> fizz
        if i % 5 = 0 -> buzz
        else -> i
number -> User input
function fizzbuzz(number)
'''


def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

num = int(input("Enter a number: "))
fizzbuzz(num)