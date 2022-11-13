from calendar import monthrange
from datetime import datetime

class Budget:

    def __init__(self, monthly_budget, amount_spent=None, id=None):
        self.monthly_budget = monthly_budget
        self.daily_budget = self.calculated_daily_budget()
        self.amount_spent = amount_spent
        self.id = id
    
    def update_monthly_budget(self, budget):
        self.monthly_budget = budget

    def update_amount_spent(self, amount):
        self.amount_spent = amount

    def calculated_daily_budget(self):
        now = datetime.now()
        year, month, day, hour = map(int, now.strftime("%Y %m %d %H").split())
        days_in_month = monthrange(year, month)[1]
        days_left_in_month = days_in_month - day
        hours_left_in_day = 24 - hour
        hours_left_in_month = 24 * days_left_in_month + hours_left_in_day

        daily_budget = round(self.monthly_budget / (hours_left_in_month / 24), 2)
        return daily_budget