def get_data():
    import json
    with open('mutual_connections.txt','r') as infile:
        data = json.load(infile)
    
    return data

import networkx as nx 
import matplotlib.pyplot as plt 
import seaborn as  sns

network = get_data()

G = nx.Graph()

#iterate over all keys in network, add edges for each
for key in network:
    for person in network[key]:
        G.add_edge(key,person)
        


pos=nx.spring_layout(G,scale=100000) #default to scale=1

nx.draw(G,pos,with_labels=True,font_size=5,node_size=1000)

plt.show()

plt.close()
