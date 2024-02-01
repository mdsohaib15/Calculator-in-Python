import math as M
print("-----------------Calculator------------")

def BasicCalculator():
          print("---------------------------------------")
          choice = input("-----------Basic Calculator------------ \n1.Addition(+) \n2.Subtraction(-) \n3.Multiplication(*) \n4.Division(/) \n5.Exponential(^) \nChoice any one of following options: ")
          print("---------------------------------------")
          if choice == "+":
                    a = float(input("Enter a: "))
                    b = float(input("Enter b: "))
                    sum = lambda a,b: a+b
                    print(f"the Sum of {a} and {b} is: {sum(a,b)}")
          elif choice == "-":
                    c = float(input("Enter a: "))
                    d = float(input("Enter b: "))
                    sub = lambda c,d: c-d
                    print(f"The Subtraction of {c} and {d} is: {sub(c,d)}")
          elif choice == "*":
                    a = float(input("Enter a: "))
                    b = float(input("Enter b: "))
                    mult = lambda a,b: a*b
                    print(f"The Multiplication of {a} and {b} is: {mult(a,b)}")
          elif choice == "/":
                    a = float(input("Enter a: "))
                    b = float(input("Enter b: "))
                    div = lambda a,b: a/b
                    print(f"The Division of {a} and {b} is: {div(a,b)}")
          elif choice == "^":
                    b = float(input("Choose power : "))
                    a = float(input("Enter a number: "))
                    exp = lambda a,b: a**b
                    print(f"The Value of {a} ^ {b} is : {exp(a,b)}") 

def AreaOfCircle(): 
          # area = π * r^2
          radius = float(input("Enter a radius of Circle "))
          area_of_the_circle = M.pi * radius ** 2
          print(f"The Area of a Circle is: {area_of_the_circle}")


def CirumferenceOfCircle():
          # C=2πr -->perimeter of a circle
          radius = float(input("Enter radius of Circle: "))
          circumference_of_the_circle =2 * M.pi * radius
          print(f"The Circumference of a Circle  is: {circumference_of_the_circle}")


def AreaOfTriangle():
          # A = ½ (b × h)
          base = float(input("Enter base of Triangle: "))
          height = float(input("Enter height of a Triangle: "))
          area_of_the_triangle = (1/2) * base * height
          print(f"The Area of a Triangle is : {area_of_the_triangle}")

def AreaOfaRectangle():
          length = float(input("Enter the length of rectangle in cm = "))
          width = float(input("Enter the width of rectangle in cm = "))
          area = float(length*width)
          print("The area of rectangle a/c to your given values = ",area,"cm")

def VolumeOfSphere():
          r = float(input("Enter the radius of sphere :"))
          voloume = 3.142 * r*r
          print("The voloume of sphere =",voloume,"cubic metre")
def AreaOfaTriangle():
          base = float(input("Enter value of base in cm = "))
          perpendicular = float(input("Enter the value of perpendicular in cm = "))
          hypotenuse = float(input("Enter the value of hypotenuse in cm = "))
          area = base+perpendicular+hypotenuse
          print(f"Expression = {base} + {perpendicular} + {hypotenuse}")
          print("Area of triangle =",area,"cm")

def CelciustoFahrenheit():
          celcius = float(input("Enter temperature in Celcius = "))
          fahrenheit = float(celcius*9/5+32)
          print("The temperature in Fahrenheit Scale is",fahrenheit,"°F")
def FahrenheittoCelsius():
          # Celsius (°C) = (Temperature in degrees Fahrenheit (°F) - 32) * 5/9.
          fahrenheit = float(input("Enter temperature in Fahrenheit = "))
          celcius = (fahrenheit-32)*5/9
          print("The temperature in Celsius Scale is",format(celcius,".2f"),"°C")
while True:
          print("---------------------------------------")
          print("1.Basic Calculator\n2.Area of a Circle \n3.Area of a Triangle \n4.Cirumference Of Circle\n5.Area Of a Rectangle \n6.Volume of aSphere \n7.Area of a Triangle (Base,Per,Hyp)\n8.Celcius to Fahrenheit converter\n9.Fahrenheit to Celsius converter\n10.Exit")
          print("---------------------------------------")
          choice = int(input("Enter choice: "))
          if choice == 1:
                    BasicCalculator()
          elif choice == 2:
                    AreaOfCircle()
          elif choice == 3:
                    AreaOfTriangle()
          elif choice == 4:
                    CirumferenceOfCircle()
          elif choice == 5:
                    AreaOfaRectangle()
          elif choice == 6:
                    VolumeOfSphere()
          elif choice == 7:
                    AreaOfaTriangle()
          elif choice == 8:
                    CelciustoFahrenheit()
          elif choice == 9:
                    FahrenheittoCelsius()
          elif choice == 10:
                    print("Exiting!!!")
                    break