#4.Write a program which accept one number form user and return addition of its factors. 

def FAdd(n):
	i=1
	sum=0
	while n>i:
		if n%i==0:
			sum = sum+i
		i=i+1
	return sum
	
def main():
	print("Enter the number")
	no = int(input())
	print("Sum is", +FAdd(no))
	

if __name__ == "__main__":
	main()