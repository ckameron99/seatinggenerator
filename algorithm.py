import queue

#import graph, person

def getEdgeBetweenness(g):
    Q = queue.Queue()
    S = queue.LifoQueue()

    betweenness = {}#[[0.0 for preference in node.preferences] for node in g.nodes]

    for s in g.nodes:
        betweenness[s] = {}

        for w in s.preferences:
            betweenness[s][w] = 0.0

    delta =  {}#[0.0 for node in g.nodes]

    for s in g.nodes:
        sigma = {}
        distance = {}
        pred = {}

        for v in g.nodes:
            delta[v] = 0.0
            distance[v] = -1
            sigma[v] = 0
            pred[v] = []

        distance[s] = 0
        sigma[s] = 1
        Q.put(s)

        while not Q.empty():
            v = Q.get()
            S.put(v)

            for w in v.preferences:
                if distance[w] == -1:
                    distance[w] = distance[v] + 1
                    Q.put(w)

                if distance[w] == (distance[v] + 1):
                    sigma[w] = sigma[w] + sigma[v]
                    pred[w].append(v)

        while not S.empty():
                w = S.get()
                for v in pred[w]:
                    c = sigma[v] / sigma[w] * (1.0 + delta[w])
                    betweenness[v][w] += c
                    delta[v] += c

    return betweenness