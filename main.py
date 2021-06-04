import person
import graph
import parser


everyone = graph.Graph()
tables = []

with open("preferences.cvs", "w") as preferences:
    lines = preferences.split(",,")
    for line in lines:
        line = line.split(",")
        everyone.addPerson(person.Person(name=line[0], preferences=line[1:]))

with open("tablenums.csv","w") as tables:
    for tableNum in tables.split(","):
        tables+=graph.Table(tableNum=int(tableNum))

tables.sort()

