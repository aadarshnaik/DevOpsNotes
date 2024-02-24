# Even or Odd

# num = input("Enter a number: ")

# if int(num) % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

# ---------------------------------------------------------------------------

# Leap Year

# year = int(input("Enter the year: "))

# if year % 4 == 0:
#     if year % 100 == 0 and year % 400 != 0:
#         print("Not a leap year") 
#     print("Leap Year")
# else:
#     print("Not a leap year")

    
# ------------------------------------------------------------

# Python Pizza

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

Total = 0

if size == "S":
    Total = 15
    if add_pepperoni == "Y":
        Total += 2
    if extra_cheese == "Y":
        Total += 1

if size == "M":
    Total = 20
    if add_pepperoni == "Y":
        Total += 3
    if extra_cheese == "Y":
        Total += 1

if size == "L":
    Total = 25
    if add_pepperoni == "Y":
        Total += 3
    if extra_cheese == "Y":
        Total += 1

print(f"Your final bill is: ${Total}")


        