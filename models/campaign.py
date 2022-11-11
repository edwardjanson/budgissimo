class Campaign:

    def __init__(self, name, budget, amount_spent=0, campaign_tags=[], id=None):
        self.name = name
        self.budget = budget
        self.amount_spent = amount_spent
        self.campaign_tags = campaign_tags
        self.id = id
    
    def update_budget(self, budget):
        self.budget = budget

    def update_amount_spent(self, amount_spent):
        self.amount_spent = amount_spent

    def add_campaign_tags(self, tag):
        self.campaign_tags.append(tag)
    
    def remove_campaign_tag(self, tag):
        self.campaign_tags.remove(tag)
    
    def clear_campaign_tags(self):
        self.campaign_tags.clear()