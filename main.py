import person
import graph
import parser


everyone = graph.Graph()
groups=[]
tables = []

with open("preferences.cvs", "w") as preferences:
    lines = preferences.split(",,")
    for line in lines:
        line = line.split(",")
        everyone.addPerson(person.Person(name=line[0], preferences=line[1:]))

#Turn text edges into references to other nodes as objects
for person in everyone:
    person.objectifyPreferences()

with open("tablenums.csv","w") as tables:
    for tableNum in tables.split(","):
        tables+=graph.Table(tableNum=int(tableNum))

tables.sort()

#insert grouping here

groups.sort()

for group in groups:
    for table in tables:
        if table.numSpaces() >= group.size():
            table.nodes += group.nodes
            break

