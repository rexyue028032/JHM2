import pandas as pd
columns = ['Date','Category','Amount', 'Type']
try:
    df = pd.read_csv('expenses.csv')
except FileNotFoundError:
    df = pd.DataFrame(columns=columns)
df = pd.DataFrame(columns=columns)
print("No existing files,create a new table")

while True:
    print("1. New transaction")
    print("2. Edit transaction")
    print("3. Delete transaction")
    print("4. View summary")
    print("5. Save and exit")
choice = input("Please enter options (1-5): ")
if choice == '1':
    add_transaction()
elif choice == '2':
    edit_transaction()
elif choice == '3':
    delete_transaction()
elif choice == '4':
    view_summary()
elif choice == '5':
    save_and_exit()
    break
else:
    print("Invalid choice, please try again.")

date = input("Enter date (YYYY-MM-DD): ")
category = input("Input category:")
amount = float(input("Enter amount: "))
trans_type = input("Input type(expenditure/income): ")
df.loc[len(df)] = {'Date': date, 'Category': category, 'Amount': amount, 'Type': trans_type}
print("Transaction added successfully!")

index = int(input("Enter the transaction index to edit: "))
print(df.loc[index])
new_date = input("Enter a new date (Enter retains the old value): ") or df.loc[index, 'Date']
df.loc[index] = {'Date': new_date, 'Category': new_category, 'Amount': new_amount, 'Type': new_type}
print("Transaction updated successfully!")

index = int(input("Enter the transaction index to delete: "))
df = df.drop(index).reset_index(drop=True)
print("Transaction deleted successfully!")
print("Transaction deleted successfully!")

total_expenses = df[df['Type'] == 'expenses']['Amount'].sum()
total_income = df[df['Type'] == 'income']['Amount'].sum()
savings = total_income - total_expenses
print(f"Total expenses: {total_expenses}")
print(f"Total income: {total_income}")
print(f"savings: {savinggs}")
if total_expenses == 0 and total_income == 0:print("No relevant information")

df.to_csv('expenses.csv', index=False)
print("The data has been saved!")
break