'''
CARSON WERTZ
This program calculates the sales total for a customer at the movie theater by taking
in the start time, day of the week, age, concessions (if any), and VIP membership status.

I certify that this code is mine, and mine alone, in accordance with
GVSU academic honesty policy.

Completed 9/19/2024
'''
# List of all valid showtimes, days, concession sizes, and VIP statuses for error checking.
timeList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dayList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
sizeList = ["S", "M", "L", "-"]
vipStatus = ["Y", "N"]

# Prompts user to enter time of day, day of the week, age, concession sizes (if applicable), and VIP member
# status. Converts day, concession sizes, and VIP status to uppercase letters for compatibility.
# Additionally, checks for errors after each input by referencing the above lists to ensure data is valid.
print("Enter information")
time = int(input("Start Time: "))
if time not in timeList:
    print("Oops! Start time must be 1 - 12.")
    exit()

day = str(input("Day: "))
day = day.upper()
if day not in dayList:
    day = "MON"

age = int(input("Age: "))
if (age < 1) or (age > 110):
    print("Oops! Age must be 1 - 110.")
    exit()

popcorn = str(input("Popcorn: "))
popcorn = popcorn.upper()
if popcorn not in sizeList:
    print("Oops! Popcorn size must be S, M, or L, (- if no purchase)")
    exit()

drink = str(input("Drink: "))
drink = drink.upper()
if drink not in sizeList:
    print("Oops! Drink size must be S, M, or L, (- if no purchase)")
    exit()

vip_status = str(input("VIP (y/n): "))
vip_status = vip_status.upper()
if vip_status not in vipStatus:
    vip_status = str(input("Oops! VIP (y/n): "))
    vip_status = vip_status.upper()
if vip_status not in vipStatus:
    vip_status = "N"

# Calculations for each day. Nested inside each day statement are the calculations of price
# for each time bracket. If the customer is a VIP member, their ticket is assigned to 0.00 (free).
if vip_status == "Y":
    ticket_price = 0.00
elif day == "TUE":
    ticket_price = 5.00
elif (day == "FRI") or (day == "SAT"):
    if time == 11:
        ticket_price = 6.00
    elif (time == 12) or ((time >= 1) and (time <= 5)):
        ticket_price = 11.00
    elif (time >= 6) and (time <= 10):
        ticket_price = 14.00
else:
    if time == 11:
        ticket_price = 6.00
    elif (time == 12) or ((time >= 1) and (time <= 5)):
        ticket_price = 9.00
    elif (time >= 6) and (time <= 10):
        ticket_price = 12.00

# Checks the customer's age and assigns the discount respectively. Checks for VIP status and omits the discount
# if true.
if (vip_status == "Y") or (age < 4):
    ticket_price = 0.00
elif day != "TUE":
    if (age >= 4) and (age <= 12):
        ticket_price = ticket_price - 2.50
    elif (age >= 13) and (age <= 15):
        ticket_price = ticket_price - 1.50

# Checks the size of both the popcorn and drink the customer wants and applies the correct price. Additionally,
# checks if the customer is a VIP member and assigns the discount to both concessions, if applicable.
if popcorn == "-":
    popcorn_price = 0.00
elif popcorn == "S":
    popcorn_price = 6.99
elif popcorn == "M":
    popcorn_price = 8.99
elif popcorn == "L":
    popcorn_price = 12.29
if vip_status == "Y":
    popcorn_price = popcorn_price * .85

if drink == "-":
    drink_price = 0.00
elif drink == "S":
    drink_price = 4.49
elif drink == "M":
    drink_price = 5.49
elif drink == "L":
    drink_price = 6.49
if vip_status == "Y":
    drink_price = drink_price * .85

# Applies sales tax to total.
subtotal = ticket_price + popcorn_price + drink_price
tax = subtotal * .06
total = subtotal + tax

# Outputs the price summary of all items. Additionally, checks if any concession item was not purchased
# and omits from summary.
print("Ticket Price Summary")
print(f"Ticket:\t\t${ticket_price:.2f}")
if popcorn != "-":
    print(f"Popcorn:\t${popcorn_price:.2f}")
if drink != "-":
    print(f"Drink:\t\t${drink_price:.2f}")
print(f"Tax:\t\t${tax:.2f}")
print(f"Total:\t\t${total:.2f}")
