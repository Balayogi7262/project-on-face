"""
def pypart(n):
    for i in range(0, n):
     
        for j in range(0, i+1):
    
            print("7 ",end="")
        print("\r")
        
        
n = 5
pypart(n)"""

def pypart(n):
    if n==0:
        return
    else:
        pypart(n-1)
        print("* "*n)
  
# Driver Code
n = 5
pypart(n)
