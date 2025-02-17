print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


tip_amnt = tip/100
total_tip = bill*100
total_bill = total_tip + bill
per_person = total_bill/people
final_amnt = round(per_person,2)
print(f"Each person cotri is:{final_amnt}")