def hello():
    name = str(input("Enter your name: "))
    company = str(input("Enter the name of your company: "))
    position = str(input("Enter your position: "))
    if name and position and company:
        # print("Hello " + name + "! Your position at " + company + " is " + position + ".")
        csv_name = str(input("Name of your CSV file: "))
        f = open(csv_name + ".csv","a")
        f.write("Name: " + name + "\n" + "Company: " + company + "\n" + "Position: " + position + "\n\n")
        f.close()
    else:
        print("Please input your personal information")
    return

decision = "y"
while decision == "y":
    hello()
    decision = str(input("Would you like to to this again? (y/n): "))
    if decision == "n":
        print("Thanks for using Storage v0.1!")
        break
