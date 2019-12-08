import matplotlib.pyplot as plt

num = list(range(100))
#Will set the range to be used to 0-99
def xofn(n):
    if n < 9:
        return n ** 2 - 7
    #n^2 - 7
    else:
        return xofn(n - 10)
    #recursive function that will return xofn(n-10) 
    #Recursive function = a function that calls on itself    
x = [xofn(item) for item in num]
#will be used as the data points

plt.stem(num, x)
plt.grid()
plt.ylabel("Y(n)")
plt.xlabel("X(n)")
plt.tight_layout()

