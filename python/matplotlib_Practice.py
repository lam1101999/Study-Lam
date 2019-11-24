import matplotlib.pyplot as plt
def main():
   
   y1 = [0.31,0.2331,0.53,0.3441,0.623,0.734,1.0321,1.3023]
   x1 = [x for x in range(len(y1))]

   plt.plot(x1,y1, label = "Canada")

   plt.xlabel("YEAR")
   plt.ylabel("number of trees")
   plt.title("Number of trees in some areas on the world")
   plt.legend()
   plt.show()
if __name__ == "__main__":
    main()    
