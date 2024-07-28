# Loop over all numbers from start to End excluding last value.
# If number is divisible by 3, print Fizz
# If number is divisible by 5, print Buzz
# If number is divisible by 3 and 5, print FizzBuzz
# If number is not divisible by 3 or 5, print number

def fizzbuzz(start, end):
    for num in range(start, end):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)


# Don't Touch Below This Line


def main():
    test(1, 100)
    test(5, 30)
    test(1, 15)


def test(start, end):
    print("Starting test")
    fizzbuzz(start, end)
    print("======================")


main()
