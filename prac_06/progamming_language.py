"""
estimated time to do the project: 30 min
time actually taken: 20 min
"""

class ProgrammingLanguage:
    def __init__(self, name, typing, relation, year):
        self.name = name
        self.typing = typing
        self.relation = relation
        self.year = year

    def is_dynamic(self):
        return self.typing.lower() == "dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.relation}, First appeared in {self.year}"