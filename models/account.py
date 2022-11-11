class Account:

    def __init__(self, budget, platforms=[], tags=[], id=None):
        self.budget = budget
        self.platforms = platforms
        self.tags = tags
        self.id = id
    
    def update_budget(self, budget):
        self.budget = budget

    def add_platform(self, platform):
        self.tags.append(platform)
    
    def delete_platform(self, platform):
        self.platforms.remove(platform)
    
    def delete_platforms(self):
        self.platforms.clear()

    def add_tags(self, tag):
        self.tags.append(tag)
    
    def delete_tag(self, tag):
        self.tags.remove(tag)
    
    def delete_tags(self):
        self.tags.clear()