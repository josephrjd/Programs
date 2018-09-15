import sys

def is_prime(number):
    if number<2:
        return False
    elif number==2 or number==3:
        return True
    i=2
    while (i**2 <= number):
        if number % i ==0:
            return False
        i = i+1
    return True

userInput = int(sys.argv[1])
counter = 0
i = 1
while True:
    if is_prime(i):
        counter = counter+1
    if counter == userInput:
        print(i)
        break;
    i=i+1
