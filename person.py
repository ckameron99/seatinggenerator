class Person:
    def __init__(self, name=None, preferences=[]):
        self.name = name.lower() #may be the crsid not the actual name
        self.preferences = [preference.lower() for preference in preferences]

    def addPreference(self, person):
        self.preferences += person.lower()

    def setName(self, name):
        self.name = name.lower()

    def objectifyPreferences(self, everyone):
        names = self.preferences
        self.preferences = []
        for person in everyone:
            if person.name in names:
                self.preferences += person
        
        if len(names) is not len(self.preferences):
            for name in names:
                if name not in [preference.name for preference in self.preferences]:
                    raise NameError("Person {} asked to sit with {}, who does not appear to exist".format(self.name))


