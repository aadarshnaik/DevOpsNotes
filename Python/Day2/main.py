# # Add digits of a number

# x = input("Enter a number: ")
# if (len(x) == 0):
#     print("Enter a number greater than zero")
# else:
#     x = int(x)
#     sum = 0 
#     while x > 0:
#         lastdig = x % 10
#         sum += lastdig
#         x = x // 10
#     print(sum)

# ----------------------------------------
# # BMI Calculator

# w = input("Enter weight in kg: ")
# h = input("Enter height in meters: ")
# BMI = int(w) / (float(h) ** 2)
# BMI = round(BMI)
# print(BMI)

# ---------------------------------------------

# Calculate days months and weeks left if we die at 90

# age = input("What is your age? : ")
# age = int(age)
# days_left = (90 * 365) - (age * 365)
# months_left = (90 * 12) - (age * 12)
# weeks_left = (90 * 52) - (age * 52)
# print(f"Youu have {days_left} days, {weeks_left} weeks and {months_left} months left.")