class Account:

    def __init__(self, name, budget, currency, spreadsheet_id=None, id=None):
        self.name = name
        self.budget = budget
        self.currency = currency
        self.spreadsheet_id = spreadsheet_id
        self.id = id
    
    def update_budget(self, budget):
        self.budget = budget
    
    def update_currency(self, currency):
        self.currency = currency