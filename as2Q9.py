#9. Write a program which accept number from user and return number of digits in that number. 

def CNumber(n):
	icnt=0
	while n>0:
		icnt += 1
		n //= 10
	return icnt
	
def main():
	print("Enter the number")
	no=int(input())
	print("Number of digits: ", (CNumber(no)))
	
if __name__ == "__main__":
	main()