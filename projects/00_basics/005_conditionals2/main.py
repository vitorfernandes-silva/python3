salary = float(input("Insert your salary: "))

if salary <= 3000:
    print("Junior Programmer")
elif salary > 3000 and salary <= 6000:
    print("Full Programmer")
elif salary > 6000 and salary <= 15000:
    print("Senior Programmer")
else:
    print("Product Manager")