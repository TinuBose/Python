
print("print leap year bw 2 given no:")
print("enter start year")
start=int(input())
End=int(input("enter end year"))
print("list leap year")
for year in range(start,End):
    if(year%4==0)and(year%100!=0)or(year%400==0):
        print(year)
