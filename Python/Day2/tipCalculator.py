print("Welcome to the tip calculator.")
# total = float(input("What was the total bill? : $"))
# tp = input("What percentage of tip would you like to give? 10%, 12%, or 15%? : ")
# person = int(input("How many people to split the bill? :"))
# if (tp == "10"):
#     total *= 1.10
# elif (tp == "12"):
#     total *= 1.12
# elif (tp == "15"):
#     total *= 1.15

# print(f"Each person should pay: ${round(total/person,2)}")


total = float(input("What was the total bill? : $"))
tip = float(input("What percentage of tip would you like to give? 10%, 12%, or 15%? : "))
persons = int(input("How many people to split the bill? :"))
tip_as_percentage = tip / 100
total_tip = total * tip_as_percentage
total_amount = total + total_tip
pay_per_person = total_amount / persons
final_amt = "{:.2f}".format(pay_per_person)
print(f"Each person should pay: {final_amt}")



