#2. Write a program which accept one number and display below pattern. 

def Pattern(n):
	for i in range(n):
		for j in range(n):
			print("*",end=" ")
		print("\n")
		
def main():
	print("Enter the number ")
	no = int(input())
	
	Pattern(no)
	
if __name__ == "__main__":
	main()
