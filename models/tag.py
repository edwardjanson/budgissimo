class Tag:

    def __init__(self, name, budget, campaigns=[], id=None):
        self.name = name
        self.budget = budget
        self.campaigns = campaigns
        self.id = id
    
    def update_budget(self, budget):
        self.budget = budget

    def add_campaign(self, tag):
        self.campaigns.append(tag)
    
    def remove_campaign(self, tag):
        self.campaigns.remove(tag)
    
    def clear_campaigns(self):
        self.campaigns.clear()
    
    def update_monthly_budget(self, budget):
        self.budget.monthly_budget = budget

    def update_daily_budget(self, budget):
        self.budget.daily_budget = budget
    
    def get_campaigns(self):
        return self.campaigns