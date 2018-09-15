import sys
import itertools

# This function returns the next prime number starting from 2 at each function call - using Sieve of Eratosthenes
def next_prime():

    # Creating a dataset for storing the non prime numbers
    dataSet = {}

    # Return 2 for the first call
    yield 2

    # Checking for only odd numbers
    for iteratorValue in itertools.count(start=3, step=2):

        popValue = dataSet.pop(iteratorValue, None)

        # If the iteratorValue is not found in the dataSet -> prime
        if popValue is None:

            yield iteratorValue

            # Add the square value of the iteratorValue as non-prime -> factor iteratorValue
            dataSet[iteratorValue**2] = iteratorValue

        # Store the next possible composite excluding the even numbers produced by iteratorValue + (N * popValue)
        # Where N is minimum
        else:
            checkValue = popValue + iteratorValue
            while checkValue % 2 == 0 or checkValue in dataSet:
                # (N * popValue)
                checkValue = checkValue + popValue

            # Add the checkValue if composit
            dataSet[checkValue] = popValue

try:
    userInput = int(sys.argv[1])

    if userInput <= 0:
        print("Prime number does not exist for given input")
    for counter, prime in enumerate(next_prime(), 1):
        if counter == userInput:
            print(prime)
            break;
except Exception as e:
    print(e)
