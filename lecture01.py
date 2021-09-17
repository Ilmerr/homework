#Task 1
import math

b = int(input('What walue is side b: '))

c = int(input('What walue is side c: '))

A_deg = int(input('What walue is angle A in degrees: '))

A = A_deg * (3.142 / 180.0)

a_squared = (b * b) + (c * c) -2 * b * c *math.cos(A)

a = math.sqrt(a_squared)

print('The walue of the side a is %0.1f'%a)

#Task 2
c = int(input('Enter temperature in Celsius: '))

f = (c * 1.8) +32

print('Temperature in Fahrenheit is %0.1f'%f)