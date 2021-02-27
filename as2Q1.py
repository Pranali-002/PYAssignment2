#1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
#for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
#parameters as number and perform the operation. Write on python program which call all the
#functions from Arithmetic module by accepting the parameters from user. 

import Arithmatics

def main():
	print("Enter first number")
	n1 = int(input())
	print("Enter second number")
	n2 = int(input())
	
	ret1= Arithmatics.Add(n1,n2)  
	ret2= Arithmatics.Sub(n1,n2)
	ret3= Arithmatics.Mul(n1,n2)
	ret4= Arithmatics.Div(n1,n2)
	
	print("Addition is:",ret1)
	print("Substraction is:",ret2)
	print("Multiplication is:", ret3)
	print("Division is:", ret4)
	
if __name__ == "__main__":
	main()