#INTEGERS
num1=100 #assigning a positive integer to num1
print (num1)
num2=-10 #assigning a negative integer to num2
print (num2)
num3= 1_000_000 #seperate the integer with underscore
print (num3)
print (type(num1), type(num2), type(num3)) #print them
num4 = int(5.0345) #converting float to int
num5 = ('65') #converting sting to int
print(num4)
print(num5)
num6 = int ('100', 2) #converting string to 100 to int
print(num6)

num7 = int('3234', 8) #converting string to int 
print(num7)

#BINARY
num8 = 0b111101110101 #assigning binary no to num8
print(num8) #printing num8 in base 10
print(type(num8)) #printing out the type of var num8

num9 = 0b1_001_111_101 #separating binary no with underscore
print(num9)

#OCTAL
num10 = 0o12 #assigning octal no to num10
print(num10) #printing num10 in base 10
print(type(num10)) #type of num10

num11 = 0o12344567 #assigning oct to num11
print(num11) #print num11 in base10
print(type(num11)) #printing out the type of num11

#HEXADECIMALS
num12 = 0x123Afde
print(num12)
print(type(num12))

num13 = 0x1234567adefcb #assigning hex to num13
print(num13)

#FLOAT
num14 = 1.23356734 #assigning a +ve float to num14
print(num14)
print(type(num14))

num15 = 123_234.732_357 #assigning +ve float to num15
print(num15)

num16 = -1234542.12456 #assigning -ve float to num16
print(num16)
num17 = 2e400 #exceeding memory size
print(num17)
num18 = 1e3 #using scientific notation
print(num18)
num19 = 3.14234232e3 #using scientific notation
print(num19)

#float conversion
num20 = float('-5.5') #converting -ve float string to float
print(num20)
num21 = float('5') #converting +ve int string to float
print(num21)
num22 = float('           -5') #converting string with space to float
print(num22)
num23 = float('1e3') #converting scientific notation
print(num23)
num24 = float('-infinity') #converting -infinity to float
print(num24)
num25 = float('inf') #converting inf to float
print(num25)

#ARITHEMETIC OPERATORS
num26 = 1500
num27 = 20
print(num26+num27) #addition
print(num26-num27) #subtraction
print(num26*num27) #multiplication
print(num26/num27)
print(num26%num27) #modulus print out remainder
print(num26**num27) #exponent or power
print(num26//num27) #floor division
print(f'{hex(num26)}') #converting num26 to hex
print(f'{oct(num26)}') #converting num26 to oct
print(f'{bin(num26)}') #converting num26 to bin
print(pow(num27, 3)) #num27^3
print(abs(-12345432)) #absolute
print(round(123.345678)) #round to nearest whole number

              
      
