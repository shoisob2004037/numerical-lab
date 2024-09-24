import numpy as np
import xlrd
from matplotlib import pyplot as plt
# A function has been created below for the Gauss elimination method.
#This function will be used to determine the unknowns of the curve fitting 
#equation from a set of equations using Gauss elimination method. 
def Gauss_elimination(a):
    
    n=np.shape(a)[0]
    #Initialize variables
    b=np.zeros([n,n+1])
    B=np.zeros([n-1,n,n+1])
    C=np.zeros([n,n+1])
    X=np.zeros([n])
    p=np.zeros([n])
    
    #Forward Elimination
    for i in range(n):
        for j in range(n+1):
            if i==0:
                b[i,j]=a[i,j]
            if i>0:
                b[i,j]=a[i,j]-(a[0,j]*(a[i,0]/a[0,0]))
    #print(b)            
    if n<3:
        C=b
    
    if n>2:
        B[0,:,:]=b 
            
        for k in range(n-2):
            for i in range(n):
                for j in range(n+1):
                    
                    if all ([i>k+1, j<k+1]):
                        B[k+1,i,j]=B[k,i,j]-(B[k,k,j]*(B[k,i,k]/B[k,k,k]))
            
                    if all ([i>k+1, j>k]):
                         B[k+1,i,j]=B[k,i,j]-(B[k,k+1,j]*(B[k,i,k+1]/B[k,k+1,k+1]))
            
                    if i<k+2:
                        B[k+1,i,j]=B[k,i,j]
                    #print(k,i,j)    
                    #print(B[k+1,:,:])
                    #print(C)
                
        C=B[k+1,:,:]
    
    #Backward Substitution
    X[n-1]=C[n-1,n]/C[n-1,n-1]
    for i in range(n-2,-1,-1):
        summation=0
        for k in range(i+1,n):
            summation=summation+C[i,k]*X[k]
            
        X[i]=(C[i,n]-summation)/C[i,i]  
        
    #Result Verification    
    for i in range(n):
        summation=0
        for j in range(n):
            summation=summation+a[i,j]*X[j]
        
        p[i]=summation-a[i,j+1]
        
    return X, p
# A function has been created below for the Gauss Jordan method.
#This function will be used to determine the unknowns of the curve fitting 

def Gauss_Jordan(a):
    
    n=np.shape(a)[0]
    #Initialize variables
    b=np.zeros([n,n+1])
    B=np.zeros([n,n,n+1])
    X=np.zeros([n])
    p=np.zeros([n])
    
    #Forward Elimination
    for i in range(n):
        for j in range(n+1):
            if i==0:
                b[i,j]=a[i,j]/a[0,0]
            if i>0:
                b[i,j]=a[i,j]-(a[0,j]*(a[i,0]/a[0,0]))
    #print(b)            
    if n<2:
        B[n-1,:,:]=b
    
    if n>=2:
        B[0,:,:]=b
        
        for k in range(n-1):
            for i in range(n):
                for j in range(n+1):
                    #print(k,i,j)    
                    if i==k:
                        B[k+1,i,j]=B[k,i,j]
                        
                        
                    if i==k+1:
                        B[k+1,i,j]=B[k,i,j]/B[k,i,i]
                        
                        
                    if i>k+1 or i<k+1:
                        B[k+1,i,j]=B[k,i,j]-(B[k,k+1,j]*(B[k,i,k+1]/B[k,k+1,k+1]))
                    #print(B[k+1,:,:])    
                   
            
    #Gathering results        
    for i in range(n):
        
        X[i]=B[n-1,i,n]
    
    #printing the results
    #print('The values of the unknown variables are respectively:')
    #print(X)
        
    #Result Verification    
    for i in range(n):
        summation=0
        for j in range(n):
            summation=summation+a[i,j]*X[j]
        
        p[i]=summation-a[i,j+1]
        
    return X, p
# A function has been created below for the LU decomposition method.
#This function will be used to determine the unknowns of the curve fitting 
#equation from a set of equations using LU decomposition method. 
def LU_decomposition(n):
    
    n=np.shape(a)[0]
    #Initialize variables
    b=np.zeros([n,n+1])
    B=np.zeros([n-1,n,n+1])
    U=np.zeros([n,n+1])
    L=np.zeros([n,n])
    X=np.zeros([n])
    d=np.zeros([n])
    p=np.zeros([n])
    
    #Forward Elimination for upper 
    #triangle matrix generation
    for i in range(n):
        for j in range(n+1):
            if i==0:
                b[i,j]=a[i,j]
            if i>0:
                b[i,j]=a[i,j]-(a[0,j]*(a[i,0]/a[0,0]))
    #print(b)            
    if n<3:
        U=b[:,:-1]
    
    if n>2:
        B[0,:,:]=b 
            
        for k in range(n-2):
            for i in range(n):
                for j in range(n+1):
                    
                    if all ([i>k+1, j<k+1]):
                        B[k+1,i,j]=B[k,i,j]-(B[k,k,j]*(B[k,i,k]/B[k,k,k]))
            
                    if all ([i>k+1, j>k]):
                         B[k+1,i,j]=B[k,i,j]-(B[k,k+1,j]*(B[k,i,k+1]/B[k,k+1,k+1]))
            
                    if i<k+2:
                        B[k+1,i,j]=B[k,i,j]
                    #print(k,i,j)    
                    #print(B[k+1,:,:])
                    #print(C)
                
        U=B[k+1,:,:-1]    #upper triangle matrix
    
    #print('The upper triangle matrix is:')
    #print(U)

    #Lower triangle matrix generation    
    for j in range(n):
        for i in range(n):
            
            if i==j:
                L[i,j]=1
            
            if all([j<i]):
                if j==0:
                    L[i,j]=a[i,j]/a[j,j]
                if j>0:
                    L[i,j]=B[j-1,i,j]/B[j-1,j,j]
    
    #print('The lower triangle matrix is:')
    #print(L)

    #Forward Substitution to compute 
    #the right hand side
    #[L][D]=[B]
    d[0]=a[0,n]/L[0,0]
    for i in range(1,n):
        summation=0
        for k in range(n):
            summation=summation+L[i,k]*d[k]
            
        d[i]=(a[i,n]-summation)/L[i,i]  
    
    #print('The right hand side matrix is:')    
    #print(d)

    #Backward Substitution using upper triangle 
    #matrix [U] and the right hand side matrix [d]
    X[n-1]=d[n-1]/U[n-1,n-1]
    for i in range(n-2,-1,-1):
        summation=0
        for k in range(i+1,n):
            summation=summation+U[i,k]*X[k]
            
        X[i]=(d[i]-summation)/U[i,i]  

    #Result Verification    
    for i in range(n):
        summation=0
        for j in range(n):
            summation=summation+a[i,j]*X[j]
        
        p[i]=summation-a[i,j+1]
    
    return X, p 
#This function determine the breaking condition
#of the Gauss Seidel Method. When relative error 
#of each unknown variable is less than the desired 
#relative error then it'll stop the loop.
def brcond_Seidel(E,err,n):
    
    a=0
    for i in range(n):  
        if E[i]<err:
            a=a+1
    return a/n
# A function has been created below for the Gauss Seidel method.
#This function will be used to determine the unknowns of the curve fitting 
#equation from a set of equations using Gauss Seidel method. 
def Gauss_Seidel(a):
    
    #Default parameters assumed for percentage relative error 
    #and number of iterations
    err=10**-15         #Assumed percentage relative error
    ite=10**4          #Assumed number of iterations
    
    n=np.shape(a)[0]
    #Initialize variables
    E=np.zeros([n])
    rel_err=np.zeros([ite,n])
    X=np.zeros([n])
    x=np.zeros([ite,n])
    itern=np.zeros([ite])
    p=np.zeros([n])
    
    #Iteration for Gauss Seidel begins here.
    for j in range(ite):
        #storing the values of iteration
        itern[j]=j+1
                 
        for i in range(n):
            summation=0
            
            for k in range(n):
                
                if k>i or k<i:
                    summation=summation+a[i,k]*x[j,k]
            
            x[j,i]=(a[i,n]-summation)/a[i,i]   #Determining the values of unknown variables
            
            #Error calculation
            if j>0:
                rel_err[j,i]=((x[j,i]-x[j-1,i])/x[j,i])*100
                E[i]=rel_err[j,i]
        
        #print(x[j,:])
        #print(E)
        
        #Breaking condition calculation
        if j>0:
            Q=brcond_Seidel(E,err,n)
            
            if Q==1:
                break
        
        #To stop the iteration when maximum iteration is reached
        if j==ite-1:
            break
         
        x[j+1,:]=x[j,:]
    
    #num_of_iter=j
    X=x[j,:]
    
    #Result Verification    
    for i in range(n):
        summation=0
        for j in range(n):
            summation=summation+a[i,j]*X[j]
        
        p[i]=summation-a[i,j+1]
        
    return X, p

#taking necessary input values from keyboard
m=int(input('Enter the order of the regression polynomial: ' ))

#Reading data from excel file
loc = (r'E:\Study Material\Code\Numerical_Lab\data_Polynomial Regression.xls')

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(4)

N=sheet.ncols-1    #number of data points
#initialize variables
x=np.zeros([N])
y=np.zeros([N])
Y=np.zeros([N])
a=np.zeros([m+1,m+2])

#creating matrix from the data 
for i in range(1,sheet.ncols):
    #print(sheet.cell_value(1, i))
    x[i-1]=sheet.cell_value(0, i)
    y[i-1]=sheet.cell_value(1, i)

#Computing the coefficients of equations
#to determine the unknown coefficients
for p in range(m+1):
    for q in range(m+2):
        if all([p==0, q==0]):
            a[p,q]=N
        if all([p==0, q>0]):
            a[p,q]=sum(x**q)
        if all([p>0, q<m+1]):
            a[p,q]=sum(x**(q+p))
        if q==m+1:
            a[p,q]=sum(x**(p)*y)

#n=m+1   #Number of equations or unknown variables
# The coefficients correspond to a set of equations determined above are
#used below to determine the unknown curve fitting parameters using the 
#methods for solving a set of linear algebraic equations.
#e.g. Gauss elimination, Gauss Jordan, LU decomposition, Gauss Seidel
#X, p=Gauss_elimination(a)   #Applying Gauss elimination method to solve the set of equations
#X, p=Gauss_Jordan(a)   #Applying Gauss Jordan method to solve the set of equations
#X, p=LU_decomposition(a)   #Applying LU decomposition method to solve the set of equations
X, p=Gauss_Seidel(a)   #Applying Gauss Seidel method to solve the set of equations
#print('The values of the unknown variables are respectively:')
#print(X)       
# The values of y are being estimated below using the above determined 
#curve fitting parameters to compare with the given/measured y values.
for Z in range(N):
    addition=0
    for v in range(m+1):
        addition=addition+X[v]*x[Z]**(v)

    Y[Z]=addition
# The following plot shows the graphical comparison between the estimated and 
#measured/given y values.
#Displaying the curve fitting result graphically
plt.figure(1)
plt.plot(x,y,'o') 
plt.plot(x,Y)
plt.xlabel('Values of x')
plt.ylabel('Values of y')
plt.title('Curve fitting using polynomial regression')
plt.legend(['Measured','Estimated'], loc='upper left')
plt.show()