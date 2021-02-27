#5.Write a program which accept one number for user and check whether number is prime or not. 

def Prime(n):
	i=2
	j=0
	while i<n:
		if n%i==0:
			k=1
		i=i+1
	return j
	
def main():
	print("Enter the number")
	a= int(input())
	b= Prime(a)
	
	if b==1:
		print("Not prime")
	else:
		print("prime")
		
if __name__ == "__main__":
	main()