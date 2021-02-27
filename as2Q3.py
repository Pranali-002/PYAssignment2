#3. Write a program which accept one number from user and return its factorial. 

def Factorial(no):
	i=1
	while no>0:
		i=i*no
		no=no-1
	return i

def main():
	print("Enter the number:")
	n = int(input())
	
	print("Factorial ",n,Factorial(n))
	
if __name__ == "__main__":
	main()