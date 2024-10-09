import pprint
pp = pprint.PrettyPrinter(indent=2, width=20)

expenses_main = {}
prompt = """
***********************************
          Expense Tracker
***********************************
Commands:
add   - add or remove an expense
view  - view expenses
clear - clear expenses
exit  - exit expense tracker
***********************************
"""


def add_expenses():
    """Allows users to add expenses to a dict object. Users should specify category and then enter amount.
    """
    global expenses_main
    while True:
        cmd = input("Enter \'a\' to add expense or any other letter to exit: ")
        if cmd.casefold() != 'a':
            break
        else:
            category = input("Enter name of category: ").casefold()
            amount = float(input("Enter amount: "))
            if category not in expenses_main.keys():
                expenses_main.update({category: [amount]})
            else:
                expenses_main[category].append(amount)
        print()


def view_expenses(wantDetail=True):
    """Allows users to view expenses category-wise. Users can specify if they want a detailed report or not.

    Args:
        wantDetail (bool): when toggled True, generates a detailed report of expenses in the form of a list of expenses, otherwise generates a summarised report that contains total amount spent on each category. Defaults to True.
    """
    global expenses_main
    expenses_temp = {}
    total = 0
    for key in expenses_main.keys():
        category_total = 0
        for expense in expenses_main.get(key):
            category_total += expense
            expenses_temp.update({key: category_total})
        total += category_total
    if wantDetail == True:
        print(f"Total expenses: {total}")
        pp.pprint(expenses_main)
    else:
        print(f"Total expenses: {total}")
        pp.pprint(expenses_temp)


def clear_expenses(keepKeys=False):
    """Allows users to clear expenses. Users can specify if they want to retain the keys or not.

    Args:
        keepKeys (bool): when toggled False, clears entire dict, otherwise retains just the keys. Defaults to False.
    """
    global expenses_main
    if keepKeys == False:
        expenses_main.clear()
        pp.pprint(expenses_main)
    else:
        expenses_main = {key: [0] for key in expenses_main.keys()}
        pp.pprint(expenses_main)


def run_program():
    """Main function that is responsible for the running of expense tracker program. Houses all functions and provides a simple interface for end user.
    """
    print(prompt, end='')
    while True:
        print('\n' + '='*23)
        cmd = input("Enter a command: ")
        print('='*23 + '\n')
        match cmd:
            case 'add':
                add_expenses()
            case 'view':
                detail = input(
                    "Enter \'y\' if you want detailed report or any other letter if not: ")
                if detail.casefold() == 'y':
                    view_expenses(wantDetail=True)
                else:
                    view_expenses(wantDetail=False)
            case 'clear':
                keys = input(
                    "Enter \'y\' if you want to keep keys or any other letter if not: ")
                if keys.casefold() == 'y':
                    clear_expenses(keepKeys=True)
                else:
                    clear_expenses(keepKeys=False)
            case 'exit':
                break
            case _:
                print("Invalid command")


run_program()
