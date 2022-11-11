class Budget:

    def __init__(self, monthly_budget, daily_budget, amount_spent, id=None):
        self.monthly_budget = monthly_budget
        self.daily_budget = daily_budget
        self.amount_spent = amount_spent
        self.id = id
    
    def update_monthly_budget(self, budget):
        self.monthly_budget = budget

    def update_daily_budget(self, budget):
        self.daily_budget = budget

    def update_amount_spent(self, amount):
        self.amount_spent = amount