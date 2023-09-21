print("             Trust Fund Buddy\n")

print("Tatals your monthly spending so that your trust fund doesn't run out")
print("<and your're forced to get a real job.>\n")

print("Please enter the requested, monthly costs. Since you're rich, ignore pennies")
print("and use only dollar amounts.\n")

car = int(input("Lamborghini Tune-Ups: "))
apartment = int(input("Manhattan Apartment: "))
jet = int(input("Private Jet Rental: "))
Gifts = int(input("Gifts: "))
dinning = int(input("Dinning Out: "))
Staff = int(input("Staff <butlers, chef, driver, assistant>: "))
personal = int(input("Personal Guru and Coach: "))
Computer = int(input("Computer Games: "))

print("\nGrand Total: %d\n" %(car + apartment + jet + Gifts + dinning + Staff + personal + Computer))

print("\nPress the enter key to exit.")
