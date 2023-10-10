def sreenedNumbersi(unknowNumber, primeNumber, lastNumber):
    print(lastNumber, unknowNumber, primeNumber)
    for i in primeNumber:
        unknowNumber += (lastNumber//i)
        print(lastNumber//i, lastNumber, i)
    return unknowNumber

def sreenedNumbers(unknowNumber, primeNumber, lastNumber):
    print(lastNumber, unknowNumber, primeNumber)
    for i in primeNumber:
        unknowNumber += (lastNumber//i)
        print(lastNumber//i, lastNumber, i)
    return unknowNumber

def main():
    primeNumber = [2, 3, 5]
    intNumber = [2, 1, 1]
    print(2 * 5 + 2)
    print(1 * 5 + 3)

    test = {'prime':[2, 3, 5, 7, 11, 13], 'ints':[6, 4, 2, 1, 1, 1], 'out':[84, 56, 33, 24, 15, 13]}
    print(169 - (10*13), 13*13)
    print((6*13) +6, (4*13) + 4, (2*13) + 6, 1*13, 1*13, 1*13)
    
    ## 7 11 13 17 19 23
    lastNumber = primeNumber[len(primeNumber)-1]**2
    ## 2 4 6 8 10 12 14 16 18 20 22 24
    ## 3 6 9 12 15 18 21 24
    ## 5 10 15 20 25

    ## 6 12 18 24
    ## 10 20
    ## 15

    ## 1 7 11 13 17 19 23
    ## 6 10 12 15 18 20 24
    
    print(lastNumber)
    unknowNumberi = sreenedNumbersi(0, primeNumber, primeNumber[len(primeNumber)-1]**2)
    unknowNumber = sreenedNumbersi(0, primeNumber, primeNumber[len(primeNumber)-1]**2)
    
    unknowNumber -= primeNumber[len(primeNumber)-1]
    
    unknowNumberi -= 12
    unknowNumberi -= 8
    unknowNumberi += 4
    unknowNumberi += 2
    unknowNumberi += 1
    
    print(unknowNumberi)  

if __name__== '__main__':
    main()
    

