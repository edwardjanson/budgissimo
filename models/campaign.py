class Campaign:

    def __init__(self, name, budget, campaign_tags=[], id=None):
        self.name = name
        self.budget = budget
        self.campaign_tags = campaign_tags
        self.id = id
    
    def update_budget(self, budget):
        self.budget = budget

    def add_campaign_tags(self, tag):
        self.campaign_tags.append(tag)
    
    def remove_campaign_tag(self, tag):
        self.campaign_tags.remove(tag)
    
    def clear_campaign_tags(self):
        self.campaign_tags.clear()