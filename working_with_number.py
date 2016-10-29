# working with fraction №1
from fractions import Fraction
f = Fraction(3,4)
print(f)

#working with fraction №2
print(Fraction(3, 4) + 1 + 1.5)

#working with fraction №3
print(Fraction(3,4) + 1 + Fraction(1/4))

#complex number
a = complex(2, 3)
print(a)

#complex number: add, substruction, multiplication, division
b = 3 + 3j
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)

#The real and imaginary parts of a complex number can be retrieved using its real and imag attributes, as follows:

z = 2 + 3j
print(z.real) #for real part
print(z.imag) #for imaginary part

#The conjugate of a complex number has the same real part but an imaginary part with an equal magnitude and an opposite sign.
print(z.conjugate())

#calculate the magnitude of a complex number
print((z.real ** 2 + z.imag ** 2) ** 0.5)

#calculate the magnitude of the complex number with abs() function. It gives the same result as expected
print(abs(z))

#handling exceptions and invalid input

#try and except block

try:
    a = float(input('Enter a number: '))
except ValueError:
    print('You entered an invalid number')

#calculating the factors of an integer
'''
Calculste


def is_factor(a, b):
    if b % a == 0:
        return True
    else:
        return False

print(is_factor(4, 1024))

'''

#find the factors of an integer
''' Factor

def factors(b):

    for i in range(1, b + 1):
        if b % i == 0:
            #print(b)
            print(i)

    if __name__=='__main__':
        b = input('Your Number Please:')
        b = float(b)

        if b > 0 and b.is_integer():
            factors(int(b))
        else:
            print('Please enter a positive integer')

factors(14)
'''

''''''

#creating multiplication tables

'''
Multiplication table printer
def multi_table(a):
    for i in range(1,11):
        print('{0} x {1} = {2}'.format(a,i,a*i))

if __name__ == '__main__':
    a = input('Enter a number: ')
    multi_table(float(a))

'''

'''
#Unit converter: Miles and


def print_menu():
    print('1.Kilometes to Miles')
    print('2 Miles to Kilometers')

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609

    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles:'))
    km = miles * 1.609

    print('Distance in kilometers: {0}'.format(km))

if __name__=='__main__':
    print_menu()
    choice = input('Which conversion would you like to do?: ')

    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()
'''

#finding the roots of a Quadratic quation

#Quadratic equation root calculator

def roots(a, b,c ):
    D = (b*b - 4*a*c)**0.5
    x_1 = (-b+D)/(2*a)
    x_2 = (-b-D)/(2*a)

    print('x1: {0}'.format(x_1))
    print('x2: {0}'.format(x_2))

if __name__=='__main__':
    a = input('Enter a:')
    b = input('Enter b:')
    c = input('Enter c:')
    roots(float(a), float(b), float(c))

