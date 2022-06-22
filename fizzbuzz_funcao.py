def fizzbuzz(int):
    if int%3==0 and not int%5==0:
        return 'Fizz'
    if int%5==0 and not int%3==0:
        return 'Buzz'
    if int%3==0 and int%5==0:
        return 'FizzBuzz'
    else:
        return int

