count = 0
import pandas as pd
df = pd.DataFrame(columns=["Bill", "Amount"])



# Run the title of the program
print("Welcome to the Bill Budgeting Program")
print("")
print("This program will help you keep track of your bills and help you budget your money")
print("")

# Ask for users name
print("Please enter your name to get started")
name = input("Name: ")
print("")
print("Hello " + name + "!")
print("")
print ("Lets get started by entering your income")
print("")
print("Please enter the amount of money you make each month")
print("For example: 1000")
print("")
income = input("Income: ")
print("")
print("Thank you for entering your income")
print("")
print("Let's get started with entering your bills")
print("")
print("You can enter as many bills as you would like")
print("When you are finished entering your bills, type 'done'")
print("")
print("Please enter the name of the bill and the amount due")
print("For example: Rent 1000")
print("")
print("Let's get started!")
print("")
while True:
    bill = input("Enter bill: ")
    if bill == "done":
        break
    else:
        count += 1 
        bill = bill.split()
        df = pd.concat([df, pd.DataFrame([{"Bill": bill[0], "Amount": bill[1]}])], ignore_index=True)
        print("")
print("You have entered " + str(count) + " bills")
print("")
print("Here are your bills:")
print("")
print(df)
print("")
print("Would you like to see a summary of your bills?")
print("Please type 'yes' or 'no'")
print("")
summary = input("Summary: ")
if summary == "yes":
    print("")
    print("Here is a summary of your bills:")
    print("")
    print(df.describe())
    print("")
    print("Would you like to see a pie chart of your bills?")
    print("Please type 'yes' or 'no'")
    print("")
    pie = input("Pie Chart: ")
    if pie == "yes":
        import matplotlib.pyplot as plt
        df["Amount"] = df["Amount"].astype(float)
        df.plot(kind="pie", y="Amount", labels=df["Bill"], autopct="%1.1f%%", legend=False)
        plt.axis("equal")
        plt.show()
    else:
        print("Thank you for using the Bill Budgeting Program")
else:
    print("Thank you for using the Bill Budgeting Program")

## Output
# Welcome to the Bill Budgeting Program







