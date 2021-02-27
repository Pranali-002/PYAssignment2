#7. Write a program which accept one number and display below pattern. 

def Num(n):
	for i in range(n):
		j=1
		while j<=n:
			print(j,end=" ")
			j+=1
		print("\n")
		
def main():
	print("Enter the number")
	no = int(input())
	Num(no)
	
if __name__ == "__main__":
	main()