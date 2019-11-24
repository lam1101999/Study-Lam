from datetime import *
from time import *
from math import *

def recursive_algo(n):
    if n <= 1:
        return n
    else:
        return recursive_algo(n-1)+recursive_algo(n-2)

def non_recursive_algo(n):
    n0 = 0
    n1 = 1
    for i in range(0,n,1):
        temp = n1
        n1 = n0 + n1
        n0 = temp
    return n0

def test(x):
    time1 = time()
    print("resursion",end ="")
    for i in range(0,x,1): 
        print(" %d " %(recursive_algo(i)), end ="")
    time1 = time() - time1

    time2 = time()
    print("\nnon_resursion",end="")
    for i in range(0,x,1): 
        print(" %d " %(non_recursive_algo(i)), end ="")
    time2 = time() - time2
    print("\nresursion:", time1)
    print("non_resursion:", time2)
    print("different:", abs(time1-time2))
    


       
    

def main():
    print("What algorithm do you want?\n-Press a for recursive algorithm.\n-Press b for loop algorithm.")
    option = input()
    print("How many number of Fibonancce do you wannt to print?")
    number = int(input(),base = 10)
    print("Fibonancce serie: ", end ="")

    # if option == "a":
    #     start = time()
    #     for i in range(0,number,1): 
    #         print(" %d " %(recursive_algo(i)), end ="")
    #     print("\ntime: %f second" %(time() - start))

    # elif option == "b":
    #     start = time()
    #     for i in range(0,number,1):
    #         print(" %d " %non_recursive_algo(i), end ="")
    #     print("\ntime: %f second" %(time() - start))

    test(number)

    



if __name__ == "__main__":
    main()