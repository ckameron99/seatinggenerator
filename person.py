class Person:
    def __init__(self, name=None, preferences=[]):
        self.name = name.lower()
        self.preferences = [preference.lower() for preference in preferences]

    def addPreference(self, person):
        self.preferences += person.lower()

    def setName(self, name):
        self.name = name.lower()

