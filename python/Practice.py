
def bala():
    x = int(input("input x:"))
    y = int(input("input y:"))
    A = []

    for i in range(x):                                                                                              
        temp = []
        for j in range(y):     
            element = i*j
            temp.append(element)
        A.append(temp)   
    print(A)    




if __name__ =='__main__':
 bala()