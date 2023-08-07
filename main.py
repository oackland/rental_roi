class smallPockets:
    # create a class with the four blocks

    def __init__(self, income, cash_flow, expenses, coc_roi):
        self.income = income
        self.cash_flow = cash_flow
        self.expenses = expenses
        self.coc_roi = coc_roi

    '''    # create the model of the future value
    # why creating the end first?
    # I found that projecting the result can help me draw the mockup
    '''

    def calculate_coc_roi(self):
        down_payment = 40000
        closing_cost = 3000
        rehab_budget = 7000
        total_initial_investment = down_payment + closing_cost + rehab_budget
        annual_cash_flow = self.cash_flow * 12

        if total_initial_investment != 0:
            self.coc_roi = (annual_cash_flow / total_initial_investment) * 100
        else:
            self.coc_roi = 0

    '''    # once we have the possible result we need to start looking for those
    # possible values if not the math will turn negative'''

    def calc_income(self, income_dict):
        self.income = sum(income_dict.values())

    '''    # if we subtract then we will project our calc_cash_flow
    # lets find those negative because life isn't pink'''

    def cal_expenses(self, expenses_dict):
        self.expenses = sum(expenses_dict.values())

    '''
    now this most complete the math, so we can start working with the user interface
    '''

    def calc_cash_flow(self):
        self.cash_flow = self.income - self.expenses


# <-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# income dict
extra_income = {}
while True:
    income_source = input("Enter income source or (type 'Next' to continue): ")
    if income_source == '':
        continue
    if income_source.lower() == 'next':
        break
    income_amount = None
    while income_amount is None:
        try:
            income_amount = float(input(f"Enter income amount for {income_source}: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    extra_income[income_source] = income_amount
# <-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# expenses dict
extra_expense = {}
while True:
    expense_sour = input("Enter the expense source or (type 'Next' to continue): ")
    if expense_sour == '':
        continue
    if expense_sour.lower() == 'next':
        break
    expense_amount = None
    while expense_amount is None:
        try:
            expense_amount = float(input(f"Enter the expense amount for {expense_sour}: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    extra_expense[expense_sour] = expense_amount

coc_roi = 0

data = smallPockets(0, 0, 0, coc_roi)
data.calc_income(extra_income)
data.cal_expenses(extra_expense)
data.calc_cash_flow()
data.calculate_coc_roi()

print("Income:", f"${data.income}")
print("Cash Flow:", f"${data.cash_flow}")
print("Expenses:", f"${data.expenses}")
print("CoC ROI:", f"{data.coc_roi}%")