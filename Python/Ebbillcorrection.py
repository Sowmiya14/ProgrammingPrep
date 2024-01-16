consumed_units = int(input("Enter the number of units consumed: "))
if consumed_units <= 100:
    print("The Electricity Bill is Free.")
else:
    if consumed_units <= 200:
        cost_of_usage = (consumed_units - 100) * 2.25
    elif consumed_units <=400:
        cost_of_usage = 100*2.25 + (consumed_units - 200) * 4.50
    elif consumed_units <= 500: 
        cost_of_usage = 100*2.25 + 200*4.50 + (consumed_units - 400) * 6.00
    elif consumed_units <= 600:
        cost_of_usage = 100*2.25 + 200*4.50 + 100*6.00 + (consumed_units - 500) * 8.00
    elif consumed_units <= 800:
        cost_of_usage = 100*2.25 + 200*4.50 + 100*6.00 + 200*8.00 + (consumed_units - 600) * 9.00
    elif consumed_units <= 1000:
        cost_of_usage = 100*2.25 + 200*4.50 + 100*6.00 + 200*8.00 + 200*9.00 + (consumed_units - 800) * 10.00
    else:
        cost_of_usage = 100*2.25 + 200*4.50 + 100*6.00 + 200*8.00 + 200*9.00 + 200*10 + (consumed_units - 200) * 11.00
    print(f"The Electricity Bill is Rs : {cost_of_usage:.2f}.")