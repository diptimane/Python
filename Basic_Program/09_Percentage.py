print("Enter the marks of five subjects")
subject1=int(input())
subject2=int(input())
subject3=int(input())
subject4=int(input())
subject5=int(input())
total=subject1+subject2+subject3+subject4+subject5
average=total/5
percentage=(total/500)*100
if average>=90:
	print("grade A")
elif average>=80 and average<90:
	print("grade B")
elif average>=70 and average<80:
	print("grade C")
elif average>=60 and average<70:
	print("grade D")
else:
	print("grade E")
print("The total marks is:",total)
print("The average is:",average)
print("The percentage is:",percentage)
