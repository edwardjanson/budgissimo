class Campaign:

    def __init__(self, name, budget, platform, id=None):
        self.name = name
        self.budget = budget
        self.platform = platform
        self.id = id

    def update_name(self, name):
        self.name = name

    def update_budget(self, budget):
        self.budget = budget