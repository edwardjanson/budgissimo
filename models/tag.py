class Tag:

    def __init__(self, name, budget, account, id=None):
        self.name = name
        self.budget = budget
        self.account = account
        self.id = id

    def update_name(self, name):
        self.name = name

    def update_budget(self, budget):
        self.budget = budget