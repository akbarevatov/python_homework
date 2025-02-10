def invest(amount, rate, years):
    for i in range(years):
        print(f"year {i+1}: ${round(amount*((rate+1)**(i+1)), 2)}")
amount = float(input("Enter the initial amount: "))
rate = float(input("Enter an annual percentage rate: "))
years = int(input("Enter the number of years: "))
invest(amount, rate, years)