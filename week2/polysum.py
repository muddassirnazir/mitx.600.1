from math import tan
from math import pi

def polysum(n,s):
    #upper divisor
    var1 = 0.25*n*(s**2)
    #lower divisor
    var2 = tan(pi/n)
    #area of the polygon
    area = var1 / var2

    #perimeter of the polygon
    perimeter = (n*s)**2

    #round function returns a rounded value upto the defined decimal place
    #in this case 4
    return round(area + perimeter, 4)

#to call this function, uncomment below line:
#print(polysum(43,83))
