def sumTwo(a, T):
    D = {}
    
    no1 = 0
    no2 = 0
    for i in range (0,len(a)):
        D[i] = a[i]
    
    print(D)

    for i in range (0,len(a)):
        no1 = a[i]
        no2 = T - no1
        if no2 in D.values():
            print("Result: ", no1, " ", no2)
            return True
        elif i == len(a) - 1:
            return False

def sumThree(a, T):
    for i in range (0,len(a)):
        no1 = a[i]
        if sumTwo(a, T-no1):
            print(no1)
        

sumTwo([10,12, 2, 3, 15, 5, 8, 19, -2, 23, 25, 18, 45], 28)
sumTwo([10,12, 2, 3, 15, 5, 8, 19, -2, 23, 25, 18, 45], -3)
sumThree([10,12, 2, 3, 15, 5, 8, 19, -2, 23, 25, 18, 45], 30)