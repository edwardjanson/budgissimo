class Campaign:

    def __init__(self, name, budget, tags=[], id=None):
        self.name = name
        self.budget = budget
        self.tags = tags
        self.id = id
    
    def update_budget(self, budget):
        self.budget = budget

    def add_tags(self, tag):
        self.tags.append(tag)
    
    def remove_tag(self, tag):
        self.tags.remove(tag)
    
    def clear_tags(self):
        self.tags.clear()