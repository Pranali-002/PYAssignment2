#6. Write a program which accept one number and display below pattern. 

def Display(m):
	for icnt in range(m):
		j=icnt+1
		while j<=m:
			print("*",end=" ")
			j+=1
		print("\n")
		
def main():
	print("Enter the number:")
	no = int(input())
	Display(no)
	
if __name__ == "__main__":
	main()