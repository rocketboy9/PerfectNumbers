#prints out a list of perfect numbers between a user specified start value and end value
def PerfectNumbers(startVal, endVal):
    listOfPerfectNumbers = []
    listOfNumbers = list(range(startVal, endVal, 1))
    print(listOfNumbers)

    for number in listOfNumbers:
        sum = 0
        for x in range(1, number-1):
            if number % x == 0:
                sum = sum + x
        if(sum == number):
            listOfPerfectNumbers.append(number)
    print("List of perfect numbers: ",listOfPerfectNumbers)


if __name__ == '__main__':
    startVal = int(input("enter start value: "))
    endVal = int(input("enter start value: "))
    PerfectNumbers(startVal, endVal)
