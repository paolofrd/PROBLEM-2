import numpy as np
import math

#squares the given x and y axis depending on the supplied power
def squareIt(x, y, power):
    b = -(x)**power - (y)**power
    return b

#storage of x,y,b values
x = np.array([]) #x axis
y = np.array([]) #y axis
b = np.array([])
n = 0
vector = [] #storage of vector [D,E,F]

#Coordinates input loop
while n < 3:
    n = n + 1
    x = np.append(x,(int(input('Input x value number ' + str(n) + ' : '))))
    y = np.append(y,(int(input('Input y value number ' + str(n) + ' : '))))
   
#Reset counter to 0
n = 0
#b storing loop
while n < 3:
    b = np.append(b,squareIt(x[n], y[n], 2))
    n = n + 1

#solving for vector[D,E,F]    
#B = np.array([[b[0]],[b[1]],[b[2]]])
A = np.array([[x[0],y[0],1],[x[1],y[1],1],[x[2],y[2],1]])
forD = np.array([[b[0],y[0],1],[b[1],y[1],1],[b[2],y[2],1]])
forE = np.array ([[x[0],b[0],1],[x[1],b[1],1],[x[2],b[2],1]])
forF = np.array ([[x[0],y[0],b[0]],[x[1],y[1],b[1]],[x[2],y[2],b[2]]])
D = np.linalg.det(forD)/np.linalg.det(A)
E = np.linalg.det(forE)/np.linalg.det(A)
F = np.linalg.det(forF)/np.linalg.det(A)
vector.extend([D,E,F])
print ('Vector [D,E,F]: ',vector,'\n')

#computation of squares
sq1 = ((1/2)*D)*((1/2)*D)
sq2 = ((1/2)*E)*((1/2)*E)

#completing the square
rightS = -(F) + sq1 + sq2
h = (D*(1/D))*math.sqrt(sq1)
k = (E*(1/E))*math.sqrt(sq2)

print ('The Standard Equation of the Circle:')
print ('x',' - ' ,h,'^2', ' + ', 'y',' - ',k,'^2',' = ',rightS,'\n')
print ('Coordinates of the center of the circle: ','(',h,',',k,')\n')

#solving for radius
r = math.sqrt(rightS)
print ('Radius of the circle: ', r)