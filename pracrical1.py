def calculate_simple_interest(principal, rate, time):
 return (principal * rate * time) / 100
principal = float(input("Enter the principal value: "))
rate = float(input("Enter the interest rate in percentage: "))
time = float(input("Enter the time in year: "))
simple_interest = calculate_simple_interest(principal, rate, time)
print("Interest:", simple_interest)