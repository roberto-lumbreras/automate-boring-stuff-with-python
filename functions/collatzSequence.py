def collatz(number):
    if number % 2 == 0:
        output = number // 2
        print(output)
        return output
    if number % 2 == 1:
        output = number * 3 + 1
        print(output)
        return output
number = 0
while number != 1:
    print('Enter number:')
    try:
        number = int(input())
        while number != 1:
            number = collatz(number)
    except ValueError:
        continue