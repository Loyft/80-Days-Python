for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:      # 'or' should be 'and'
        print("FizzBuzz")
    if number % 3 == 0:     # elif instead of if
        print("Fizz")
    if number % 5 == 0:     # elif instead of if
        print("Buzz")
    else:
        print([number])     # print(number)
