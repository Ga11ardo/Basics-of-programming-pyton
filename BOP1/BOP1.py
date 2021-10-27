import math
print ("input sides of triangle")
a=float (input ())
c=float (input ())
b=sqrt(math.pow(c, 2)-math.pow(a,2))
p=(a+b+c)/2
r=sqrt((p-a)*(p-b)*(p-c)/p)
print ("the length of the bisector is drawn to the side b =", "%.4f" % (b))
print ("the radius of the inscribed circle = ", "%.4f" % (r))