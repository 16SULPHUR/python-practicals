print("\n\n---Arithmatic Operators---\n")
num1=input("Enter Number 1: ")
num2=input("Enter Number 2: ")

print("1) {0}+{1}={2}".format(num1,num2,num1+num2))
print("2) {0}-{1}={2}".format(num1,num2,num1-num2))
print("3) {0}*{1}={2}".format(num1,num2,num1*num2))
print("4) {0}/{1}={2}".format(num1,num2,num1/num2))
print("5) {0}%{1}={2}".format(num1,num2,num1%num2))
print("6) {0}//{1}={2}".format(num1,num2,num1//num2))
print("7) {0}^{1}={2}\n".format(num1,num2,num1**num2))

print("---Assignment Operators---\n")
num1=input("Enter Number 1: ")
num1+=2
print("1) number1+=2 \n=> number1 = {0}\n".format(num1))
num1-=2
print("2) number1-=2 \n=> number1 = {0}\n".format(num1))
num1*=2
print("3) number1*=2 \n=> number1 = {0}\n".format(num1))
num1/=2
print("4) number1/=2 \n=> number1 = {0}\n".format(num1))
num1%=2
print("5) number1%=2 \n=> number1 = {0}\n".format(num1))

print("---Logical Operators---\n")
num1=input("Enter Number 1: ")
num2=input("Enter Number 2: ")

print("1) (number1) and (number2) = {0}".format((num1) and (num2)))
print("2) (number1) or (number2) = {0}".format((num1) or (num2)))
print("3) not (number2) = {0}\n".format( not (num2)))

print("---Comparison Operators---\n")
num1=input("Enter Number 1: ")
num2=input("Enter Number 2: ")
print("1) Is number1 == number2 \t=>\t {0}\n".format(num1==num2))
print("2) Is number1 > number2 \t=>\t {0}\n".format(num1>num2))
print("3) Is number1 < number2 \t=>\t {0}\n".format(num1<num2))
print("4) Is number1 <= number2 \t=>\t {0}\n".format(num1<=num2))
print("5) Is number1 >= number2 \t=>\t {0}\n".format(num1>=num2))
print("6) Is number1 != number2 \t=>\t {0}\n".format(num1!=num2))

print("---Bitwise Operators---\n")
num1=input("Enter Number 1: ")
num2=input("Enter Number 2: ")
print("1) number1 & number2 => {0}".format(num1&num2))
print("2) number1 | number2 => {0}".format(num1|num2))
print("3)  ~ number2 => {0}".format(~num2))
print("4) number1 ^ number2 => {0}".format(num1^num2))
print("5) number1 >> number2 => {0}".format(num1>>num2))
print("6) number1 << number2 => {0}\n".format(num1<<num2))

print("---Identity Operators---\n")
num1=input("Enter Number 1: ")
num2=input("Enter Number 2: ")
print("1) number1 is number2 => {0}".format(num1 is num2))
print("2) number1 is not number2 => {0}".format(num1 is not num2))
