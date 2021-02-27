#10. Write a program which accept number from user and return addition of digits in that number. 

def NAdd(n):
	j=0
	while n>0:
		j+=n%10
		n=n//10
	return j
	
def main():
	print("Enter the number")
	no= int(input())
	num= NAdd(no)
	print("Number of digit=",+num)
	
if __name__ == "__main__":
	main()