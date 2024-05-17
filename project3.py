#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


class Expense:
    def __init__(self, amount, description, category):
        self.amount = amount
        self.description = description
        self.category = category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def view_monthly_summary(self):
        total_expenses = sum(expense.amount for expense in self.expenses)
        print(f"Monthly Expense Summary:")
        print(f"Total Expenses: ${total_expenses:.2f}")

    def view_category_expenses(self):
        category_expenses = {}
        for expense in self.expenses:
            if expense.category in category_expenses:
                category_expenses[expense.category] += expense.amount
            else:
                category_expenses[expense.category] = expense.amount

        print("Category-wise Expenses:")
        for category, amount in category_expenses.items():
            print(f"{category.capitalize()}: ${amount:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            category = input("Enter expense category: ")
            expense = Expense(amount, description, category)
            tracker.add_expense(expense)
            print("Expense added successfully.")

        elif choice == "2":
            tracker.view_monthly_summary()

        elif choice == "3":
            tracker.view_category_expenses()

        elif choice == "4":
            print("Exiting Expense Tracker...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




